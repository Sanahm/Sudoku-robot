#!/usr/bin/python
# -*- coding: utf-8 -*-
from Capture import *
import numpy as np
import math
import cv2
import os

def adaptativeThresholding(image):
    """Applique un filtre médian et effectue un seuillage binaire adaptatif sur l'image
    __________
    Parameters :
    image : image en niveau de gris
    __________
    Return :
    tresh : image binarisée
    """
    img = cv2.medianBlur(image,5)
    thresh = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,21,2)
    return thresh

def normalThresholding(image):
    """Applique un filtre gaussien et effectue un seuillage binaire suivant la méthode de Otsu sur l'image
    __________
    Parameters :
    image : image en niveau de gris
    __________
    Return :
    thresh : image binarisée
    """
    ret,thresh = cv2.threshold(image,120,255,cv2.THRESH_TRUNC)
    th3,threshNormal = cv2.threshold(thresh,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    return threshNormal

def negative(image):
    """Retourne le negatif de l'image prise en paramètre
    """
    return 255 - image

def order_points(pts):
    """Réarrange les coins d'un quadrilatère dont les coordonnées sont contenues dans une matrice (4,2) de cette façon : [[bas-gauche],[haut-gauche],[haut-droit],[bas-droit]]
    __________
    Parameters :
    pts: matrice (4,2) contenant les coordonnées des coins
    __________
    Return :
    rect : matrice (4,2) contenant les coordonnées des coins ordonnées
    """
    rect = np.zeros((4, 2))

    s = pts.sum(axis = 1)
    rect[1] = pts[np.argmin(s)] # le coin supérieur gauche a la plus faible somme sur ses cooordonnées
    rect[3] = pts[np.argmax(s)] # le coin inférieur droit a la plus grande somme sur ses cooordonnées

    diff = np.diff(pts, axis = 1)
    rect[2] = pts[np.argmin(diff)] # le coin supérieur droit a la plus petite différence sur ses cooordonnées
    rect[0] = pts[np.argmax(diff)] # le coin inférieur gauche a la plus grande différence sur ses cooordonnées

    return rect


def grille_detection(img):
    """Detecte la grille de sudoku sur une image où la grille est blanche sur un fond noir
    __________
    Parameters :
    img : image binaire
    __________
    Return :
    rect : tuple ((x, y), (l, h), alpha) où (x, y) sont les coordonnées du centre du rectangle d'approximation de la grille, (l, h) la largeur et la hauteur du rectangle et alpha son angle
    grille : une matrice contenant les coordonnées des coins de la grille de sudoku [[bas-gauche],[haut-gauche],[haut-droit],[bas-droit]]
    """
    # Recherche des contours
    (contours,_) = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # Sélection du plus grand contour en terme d'aire
    max_area = 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > max_area:
                max_area = area
                best_cnt = cnt
    # Approximation du contour par un polynôme selon l'algorithme de Douglas–Peucker
    epsilon = 0.1 * cv2.arcLength(best_cnt, True)
    approx = cv2.approxPolyDP(best_cnt, epsilon, True)
    app=[]
    for i in range(0,len(approx)):
        app.append(approx[i][0])
    grid = np.array(app)
    grille = order_points(grid)
    # Recherche du rectangle orienté qui s'adapte le mieux au contour en terme d'aire
    rect = cv2.minAreaRect(best_cnt)
    return rect, grille

def processNormal(img):
    """Applique le traitement normal (image de bonne qualité) sur l'image et effectue le redressement de perspective 
    __________
    Parameters :
    img : image en niveau de gris
    __________
    Return :
    rect : tuple ((x, y), (l, h), alpha) où (x, y) sont les coordonnées du centre du rectangle d'approximation de la grille, (l, h) la largeur et la hauteur du rectangle et alpha son angle
    dst : la grille de sudoku
    """
    # On applique le seuillage normal 
    threshNormal = normalThresholding(img)
    thresh_neg = negative(threshNormal)
    # On détecte la grille
    rect, grid = grille_detection(thresh_neg)
    rect = list(rect)
    ##box = grid_model(rect)
    # pts1 contient les coordonnées des coins du polynôme d'approximation de la grille au nombre de 4
    pts1 = np.float32(grid) 
    pts2 = np.float32([[0,512],[0,0],[512,0],[512,512]])
    # Redressage de la grille
    M = cv2.getPerspectiveTransform(pts1,pts2)
    dst = cv2.warpPerspective(threshNormal,M,(512,512))
    return rect, dst

def processAdaptative(img):
    """Applique le traitement adaptatif (image de mauvaise qualité) sur l'image et effectue le redressement de perspective
    __________
    Parameters :
    img : image en niveau de gris
    __________
    Return :
    rect : tuple ((x, y), (l, h), alpha) où (x, y) sont les coordonnées du centre du rectangle d'approximation de la grille, (l, h) la largeur et la hauteur du rectangle et alpha son angle
    median : la grille de sudoku
    """
    # On applique un premier seuillage qui passe en blanc tout les pixels de niveau de gris supérieur à 120, les autres sont conservés
    ret,threshAdapt = cv2.threshold(img,120,255,cv2.THRESH_TRUNC)
    # On applique le seuillage adaptatif
    threshAdapt = adaptativeThresholding(threshAdapt)
    # On applique un filtre médian afin de supprimer les petits artefacts du seuillage adaptatif
    threshMedian = cv2.medianBlur(threshAdapt,7)
    thresh_neg = negative(threshMedian)
    thresh_neg = negative(threshMedian)
    # On détecte la grille
    rect, grid = grille_detection(thresh_neg)
    rect = list(rect)
    ##box = grid_model(rect) #box contient les coordonnées des 4 coins du rectancle d'approximation de la grille qui minimise l'aire
    # pts1 contient les coordonnées des coins du polynôme d'approximation de la grille au nombre de 4
    pts1 = np.float32(grid)
    pts2 = np.float32([[0,512],[0,0],[512,0],[512,512]])
    # Redressage de la grille
    M = cv2.getPerspectiveTransform(pts1,pts2)
    dst = cv2.warpPerspective(threshAdapt,M,(512,512))
    # On applique un filtre médian afin de supprimer les petits artefacts du seuillage adaptatif
    median = cv2.medianBlur(dst,3)
    th,median = cv2.threshold(median,254,255,cv2.THRESH_BINARY)
    return rect, median

def grid_model(rect):
    """
    Cette fcn permet, à partir du tuple de la fonction grille_detection(), de retourner les coordonnées des 4 coins du rectangle
    """
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    return box

def draw_model(image,box):
    """
    Cette fonction permet de tracer le rectangle qui approxime la grille sur l'image à partir des coordonnées des 4 coins
    """
    return cv2.drawContours(image,[box],0,(255,255,255),2)

def isGridOK(im):
    """Juge si la grille de sudoku semble être bonne en vérifiant la proportion de pixels noir dans l'image
    __________
    Parameters :
    img : grille sudoku (image binaire)
    __________
    Return :
    booleen : True si la grille est OK False sinon
    """
    ret, imageBinaire = cv2.threshold(im,254,255,cv2.THRESH_BINARY)
    s = 0
    for i in range (0,len(imageBinaire)):
        for j in range (0,len(imageBinaire[0])):
            if(imageBinaire[i,j] == 0):
                s += 1
    pourcentageNoir = (s/(len(imageBinaire)*len(imageBinaire[0])))*100
    print(pourcentageNoir)
    if(pourcentageNoir>5 and pourcentageNoir <25):
        return True
    else :
        return False

def threshHold(image):
    # Remarque : 
    # En l'état cette fonction n'est plus utile car seul le processNormal est utilisé. Elle est donc equivalente à la fonction processNormal()
    # Cependant dans des conditions d'éclairage mauvaise il peut être utile d'appliquer le processAdaptative et de comparer les resultats pour ne conserver que le meilleur

    """Applique tout les traitement sur l'image et retourne la grille avec ses infos
    __________
    Parameters :
    img : image à traiter
    __________
    Return :
    rectNorm: tuple ((x, y), (l, h), alpha) où (x, y) sont les coordonnées du centre du rectangle d'approximation de la grille, (l, h) la largeur et la hauteur du rectangle et alpha son angle
    norm : la grille de sudoku redressée
    """
    #rectAdapt, adapt = processAdaptative(image)
    rectNorm, norm = processNormal(image)
    return rectNorm, norm









