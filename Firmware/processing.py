#!/usr/bin/python
# -*- coding: utf-8 -*-
import cv2
import numpy as np
from matplotlib import pyplot as plt
from random import *
from solver import *

def xyproject(img,axis):
    """Take an image and a axis( 0 or 1) and return the normalized projection of the image on the specified axe
    Paramters:
    ----------
    img : input image
    axis : 0 for x projection and 1 for y projection
    returns
    -------
    Array of projection
    """
    if(img.shape[axis] == 0):
        return None
    return np.sum(img,axis)/img.shape[axis]





def binarize(img,flag):
    """ Take an image and a flag and return the binarized image according to the flag specified
    Parameters:
    -----------
    img: input image
    flag: if cv2.THRESH_OTSU then the binarisation is done with OTSU method
          if either cv2.ADAPTIVE_THRESH_MEAN_C or cv2.ADAPTIVE_THRESH_GAUSSIAN_C then an adaptive method
          is used.
    Returns:
    --------
    retval: the value of the threshold( default value = 0)
    imB: binarized image (default value = None)
    PLEASE REFER TO THE OPENCV DOC FOR MORE INFORMATIONS
    """
    retval = 0
    imB = None
    if(flag == cv2.THRESH_BINARY):
        retval,imB = cv2.threshold(img,0,255,cv2.THRESH_BINARY)
    if(flag == cv2.THRESH_OTSU):
        retval,imB = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    if(flag == cv2.ADAPTIVE_THRESH_GAUSSIAN_C):
        imB = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,7,2)
    if(flag == cv2.ADAPTIVE_THRESH_MEAN_C):
        imB = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,7,2)
    return retval,imB





def HoughSort(lines,eps_rho,eps_theta):
    """ Take the vector <lines> return by HoughLine() and sort it.
    To best understand use it to see its effect
    """
    lines = lines[0][lines[0][:][:,0].argsort()]
    for i in range(lines.shape[0]):
        j=i-1
        while(j>=0):
            if(abs(lines[j][0]-lines[j+1][0])<eps_rho and abs(lines[j][1]-lines[j+1][1])>eps_theta):
                #then, in this case sort by following theta
                if(lines[j][1]>lines[j+1][1]):
                    lines[j][0],lines[j+1][0] = lines[j+1][0],lines[j][0]
                    lines[j][1],lines[j+1][1] = lines[j+1][1],lines[j][1]
            j -= 1
    return lines




def StatSort(stats):
    """
    Once you get the coordinate of each case, you have to order it because to do not lose the position
    of each case on the sudoku image
    """
    stats = stats[stats[:,1].argsort()] #on trie par rapport a la 2e colonne
    for j in range(9):#puis par rapport a la 1ere par bloc de 9(pour comprendre essayer d'afficher stats sans tri)
        t = stats[9*j:j*9+9,:]
        t = t[t[:,0].argsort()]
        stats[9*j:j*9+9,:] = t
    return stats



             
def ExtractBoxes(imBinarized,connexity=None,thresh=None):
    """ Take a binarized image thresholded and search the eventual boxes inside using thresh
    Parameters:
    -----------
    imBinarized: input image
    connexity : 4 or 8 (refer to cv2.connectedComponentsWithStats(...) doc)
    thresh : array of 1x2= (thresh_min_x,thresh_min_y,thresh_max_x,thresh_max_y) which means that the
            researched boxes should be at least thresh_min_x large and thresh_min_y height and at most
            thresh_max large and thresh_max_y height

            
    the parmeters connexity and thresh will be used if specified otherwise findContours(...) method will be used!
    Returns:
    --------
    stat: an array of Nx5 where N means the number of boxes found and 5, 5 rows according to
           cv2.connectedComponentsWithStats(...) or findContours(...) doc.
           
    PLEASE REFER TO THE OPENCV DOC FOR MORE INFORMATIONS
    """
    try:
        output = cv2.connectedComponentsWithStats(imBinarized,connexity)
        stat = output[2] #contains the boxes found
        #now we are going to delete the boxes which do not respect the thresh
        k = 0
        l = 0
        while( k < stat.shape[0]):
            if( stat[k][2] < thresh[0] or stat[k][3] < thresh[1] or stat[k][2] > thresh[2] or stat[k][3] > thresh[3]):
                #then delete it
                stat = np.delete(stat,k,axis=0)
            else:
                #ignore
                k += 1
        return StatSort(stat)
    except:
        """ If opencv function connectedComponentsWithStats() not found or if only one argument
            is given, then findContours() method will be used!
            for example, opencv2 don't embed the previous method cv2.connectedComponentsWithStats(...)
        """
        (cnts,_) = cv2.findContours(imBinarized.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:81] #permet de trier par ordre décroissant de l'aire des cases détectées
        #l = cv2.drawContours(im, [cnts[1]], -1, (255, 0, 0), 3)
        stats = np.zeros((81,5),int)
        T = []
        for i in range(len(cnts)):
            cnts[i] = cv2.approxPolyDP(cnts[i],eps_rho,True)
            cnts[i] = cnts[i][cnts[i][:,0][:,0][:].argsort()] #pour trier selon la colonne des y (afficher stat pour comprendre)
            if(len(cnts[i]) != 4):
                continue
            x,y,h,w = cv2.boundingRect(cnts[i])
            T.append(x+1)#l'abscisse de la case
            T.append(y+1)#son ordonnee
            T.append(min(h,w)-2)#sa hauteur les -2 c'est uniquement pour eviter de prendre les pixels noirs du contour
            T.append(min(h,w)-2)#sa largeur
            T.append(T[2]*T[3])#l'aire totale du contour
            stats[i] = T
            T = [] #T.clear()
        return StatSort(stats)





def ExtractBoxImage(boxes,img,imgFlat,method):
    """ Take the input image and extract image from boxes returned by function ExtractBoxes(...)
    Parameters:
    -----------
    img: input image
    boxes: ExtractBoxes(...)
    imgFlat: tuple of size =2 . For each image will be flattened into a 1D array of imgFlat[0]*imgFlat[1]
    Returns:
    --------
    imBox: an array of Nx28x28 where N means the number of boxes found and 28x28 the size of the box image
           resized
    PLEASE REFER TO THE ExtractBoxes(...) FUNCTION FOR MORE INFORMATIONS
    """
    imBox = np.zeros((boxes.shape[0],imgFlat[0]*imgFlat[1]),dtype = img.dtype)
    for i in range(imBox.shape[0]):
        if(stat[i][3]<imgFlat[0]/2 or stat[i][2]<imgFlat[1]/2 ):
            continue
        imR = img[boxes[i][1]:boxes[i][1]+boxes[i][3],boxes[i][0]:boxes[i][0]+boxes[i][2]]
        ret,imR = binarize(cv2.resize(imR,imgFlat,interpolation=method),cv2.THRESH_BINARY)
        (cnt,_) =cv2.findContours(255-imR.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cnt = sorted(cnt, key = cv2.contourArea, reverse = True)
        if(len(cnt) !=0):
            imRR = np.ones((28,28))*255
            x,y,h,w = cv2.boundingRect(cnt[0])
            pix = 1 #si c'est desaxé de plus de 1 pixels on corrige (le cas ou le chiffre dans la case n'est pas au milieu)
            if(h > (3.0/4)*imgFlat[0] or w > (3.0/4)*imgFlat[1]):#souvent les chiffres sont de grandes tailles ce qui fausse la detection
                
                ret,tmp = binarize(cv2.resize(imR[y:y+w,x:x+h],None,fx=0.6,fy=0.6,interpolation=method),cv2.THRESH_BINARY)
                #l'idee est donc de redimensioner la taille du chiffre: on extrait le chiffre, on le resize et on le reinjecte dans une image noire (imRR)
                w,h = tmp.shape
                imRR[imgFlat[1]/2 - w/2:imgFlat[1]/2 - w/2 + w,imgFlat[0]/2 - h/2:imgFlat[0]/2 - h/2 + h] = tmp #NB -w/2 + w != w/2 ==> arrondi (calcul scientifique)
                imR = imRR
                #print 'dbg'
                
            elif(abs(x+h/2 - imgFlat[0]/2) > pix or abs(y+w/2 - imgFlat[1]/2) > pix):#souvent les chiffres sont pas centres dans la case
                #l'idee est d'extraire le chiffre de calculer le shift et le recentrer :) ah Mohamed tu cherches loin 
                tmp = imR[y:y+w,x:x+h]
                w,h = tmp.shape
                imRR[imgFlat[1]/2 - w/2:imgFlat[1]/2 - w/2 + w,imgFlat[0]/2 - h/2:imgFlat[0]/2 - h/2 + h] = tmp #NB -w/2 + w != w/2 ==> arrondi (calcul scientifique)
                imR = imRR
                #print 'dbg'
        imBox[i] = np.reshape(imR,imgFlat[0]*imgFlat[1])
    return imBox


def HoughGrid(lines,eps_rho,eps_theta):
    """
    take <line> return by HoughLine() and sort it in order to let only the lines of the grid
    Remind that Hough method return all 3-points alignment on image so some of lines won't be a part of the desired
    line
    """
    lines = HoughSort(lines,eps_rho,eps_theta)
    grid = np.zeros((20,2)) #sudoku's grid have 20 lines. 2 =>(rho,theta)
    j = 0
    eps = 1e-2
    for i in range(lines.shape[0]):
        if(lines[i][0] <= 0 or lines[i][1] < 0):
            continue
        elif(abs(lines[i][0] - grid[j-1][0]) > eps_rho or (abs(lines[i][1] - grid[j-1][1]) > eps_theta and lines[i][1] > eps)):
            if abs(lines[i][1] < eps): lines[i][1] = 0
            elif (abs(lines[i][1]-np.pi/2) < eps): lines[i][1] = np.pi/2
            elif (abs(lines[i][1]-np.pi) < eps): lines[i][1] = np.pi
            else: continue
            grid[j] = lines[i]
            j +=1
            #if j == 20: break
        elif(abs(lines[i][0] - grid[j-1][0]) < eps_rho and abs(lines[i][1] - grid[j-1][1]) < eps_theta ):
            if abs(lines[i][1] < eps): lines[i][1] = 0
            elif (abs(lines[i][1]-np.pi/2) < eps): lines[i][1] = np.pi/2
            elif (abs(lines[i][1]-np.pi) < eps): lines[i][1] = np.pi
            else: continue
            grid[j-1] = (grid[j-1] + lines[i])/2
        else:
            continue

    return grid,lines

def EstimatedGrid(grid):
    """
    return the estimated grid (and save it as hough.png)
    """
    imC = (im>=0)*255
    for i in range(grid.shape[0]):
        rho = grid[i][0]
        theta = grid[i][1]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))
        cv2.line(imC,(x1,y1),(x2,y2),(0,0,0),2)
    #cv2.imwrite('hough.png',imC)
    I = cv2.cvtColor(np.array(imC,'uint8'),cv2.COLOR_BGR2GRAY)/255
    return I




im = cv2.imread('./Grille.png')#,cv2.IMREAD_GRAYSCALE)

#Grille.png is the image return by "pretraitement(thresholding)"
img = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
lx,ly = img.shape #image width and heigth
ret,imB = binarize(img,cv2.THRESH_OTSU)


edges = cv2.Canny(img,50,150,apertureSize = 3)  
lines = cv2.HoughLines(edges,1,np.pi/180,110)
eps_rho = int(min(lx/9,ly/9)/2)
eps_theta = np.pi/8
grid,lines = HoughGrid(lines,eps_rho,eps_theta)
I = EstimatedGrid(grid)

#I*imB juste pour rehausser les lignes qui peuvent ne pas être en noir et corriger les artefacts (voir rapport)
stat = ExtractBoxes(imB*I)#,connexity = 8,thresh=(lx/18,ly/18,lx/3,ly/3)) if you use connectedComponent

imBox = ExtractBoxImage(stat,imB,(28,28),cv2.INTER_CUBIC)
imBox1 = ExtractBoxImage(stat,imB,(28,28),cv2.INTER_AREA)
imBox2 = ExtractBoxImage(stat,imB,(28,28),cv2.INTER_LINEAR)
imBox3 = ExtractBoxImage(stat,imB,(28,28),cv2.INTER_LANCZOS4)

##Remind that INTER_CUBIC,INTER_AREA,INTER_LINEAR, INTER_LANCZOS4 that is the
##type of interpolation used to resize image to 28x28 pixels



