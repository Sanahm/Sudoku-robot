import numpy as np
import cv2

#Cette fonction applique un filtre gaussien pour supprimer le bruit de l'image originale
#Elle effectue ensuite un seuillage automatique sur l'image puis la retourne
def threshholding(image):
	#blur = cv2.GaussianBlur(image,(5,5),0)
	#th3,thresh = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
	#enlever les commentaires sur les deux lignes suivantes si la qualité d'image de base est mauvaise et commenter les deux lignes au dessus
	img = cv2.medianBlur(image,5)
	thresh = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,21,2)
	print(cv2.THRESH_BINARY)
	return thresh

#Cette fcn retourne le negatif de l'image prise en paramètre
def negative(image):
	return 255 - image

#Cette fonction permet de detecter la grille de sudoku sur une image où la grille est blanche sur un fond noir d'où la fcn negative()
#Cette fcn retourne un tuple ((x, y), (l, h), alpha) où (x, y) sont les coordonnées du centre du rectangle d'approximation de la grille, (l, h) la largeur et la hauteur du rectangle et alpha son angle
#Le tuple rect modelise un rectangle
#Cette fonction retourne egalement une matrice contenant les vrais coins de la grille de sudoku [[coord bas],[cood gauche],[coord haut],[coord droit]]
def grid_detection(image):
	img, contours, hierarchy = cv2.findContours(image,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	cnt = contours[0]
	leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
	left = np.array([leftmost[0],leftmost[1]])
	rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
	right = np.array([rightmost[0],rightmost[1]])
	topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
	top = np.array([topmost[0],topmost[1]])
	bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])
	bot = np.array([bottommost[0],bottommost[1]])
	grid = np.array([bot,left,top,right])
	rect = cv2.minAreaRect(cnt)
	print(rect)
	return rect, grid

#Cette fcn permet, à partir du tuple de la fonction grid_detection(), de retourner les coordonnées des 4 coins du rectangle
def grid_model(rect):
	box = cv2.boxPoints(rect)
	box = np.int0(box)
	return box

#Cette fonction permet de tracer le rectangle qui approxime la grille sur l'image à partir des coordonnées des 4 coins
def draw_model(image,box):
	return cv2.drawContours(image,[box],0,(255,255,255),2)

img = cv2.imread('im2.jpg',0)
thresh = threshholding(img)
thresh_neg = negative(thresh)
kernel = np.ones((5,5),np.uint8)
thresh_neg = cv2.morphologyEx(thresh_neg, cv2.MORPH_OPEN, kernel) #supprime les petites zones qui passent au dessus du seuil mais qui ne font pas partie de la grille
rect, grid = grid_detection(thresh_neg)
box = grid_model(rect)


image = draw_model(thresh_neg, box)
pts1 = np.float32(grid)
pts2 = np.float32([[0,2000],[0,0],[2000,0],[2000,2000]])
M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(thresh,M,(2000,2000))

cv2.imwrite('sudokuresdst.png',dst)
cv2.imwrite('sudokures.png',thresh_neg)










