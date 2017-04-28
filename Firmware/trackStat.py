#!/usr/bin/python
# -*- coding: utf-8 -*-
from Capture import *
from picamera.array import PiRGBArray
import picamera
import time
import cv2
import numpy as np
from thresholding import *

def trackStat(downColor, upColor, downColor2, upColor2):
    """Prend une photo et retourne les coordonnées des centres de gravité des deux plus gros objets dont la couleur
        codée en HSV se situe dans l'espace definit par les coordonnées downColor et upColor pour le premier objet 
        et downColor2 et upColor2 pour le deuxième
	__________
	Parameters :
	downColor : 3-uplet de les coordonnées représentent la couleur basse pour le premier objet
	upColor : 3-uplet de les coordonnées représentent la couleur haute pour le premier objet
	downColor2 : 3-uplet de les coordonnées représentent la couleur basse pour le deuxième objet
	upColor2 : 3-uplet de les coordonnées représentent la couleur haute pour le deuxième objet
	__________
	Return :
	a : 2-uplet ie les coordonnées du centre de gravité du premier objet
	a : 2-uplet ie les coordonnées du centre de gravité du deuxième objet
	"""
    l = 1280
    L = 1024

    # initialisation de la camera
    camera = picamera.PiCamera()
    camera.resolution = (l, L)
    rawCapture = PiRGBArray(camera, size=(l, L))
    time.sleep(0.1)
    # Prise de la photo
    camera.capture(rawCapture, format="bgr")
    image = rawCapture.array
    # Conversion de l'image en HSV
    hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    # Conservation des pixels de la bonne couleur 
    thresh = cv2.inRange(hsv,np.array(downColor), np.array(upColor))
    thresh2 = cv2.inRange(hsv,np.array(downColor2), np.array(upColor2))
    # Recherche des contours
    (contours,_)  = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    (contours2,_)  = cv2.findContours(thresh2,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    # Conservation du contour ayant la plus grande aire pour la première couleur
    max_area = 1
    best_cnt = 1
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > max_area:
            max_area = area
            best_cnt = cnt
	# Conservation du contour ayant la plus grande aire pour la deuxième couleur
    max_area2 = 0
    best_cnt2 = 1        
    for cnt in contours2:
        area = cv2.contourArea(cnt)
        if area > max_area2:
            max_area2 = area
            best_cnt2 = cnt
    # Calcul des coordonnées du centre de gravité du contours le plus grand (best_cnt)
    M = cv2.moments(best_cnt)
    cx,cy = int(M['m10']/M['m00']), int(M['m01']/M['m00'])
    # Calcul des coordonnées du centre de gravité du contours le plus grand (best_cnt2)
    M2 = cv2.moments(best_cnt2)
    cx2,cy2= int(M2['m10']/M2['m00']), int(M2['m01']/M2['m00'])
    # Ajout de deux cercles sur l'image centrés sur les centres de gravités
    cv2.circle(image,(cx,cy),10,(0,0,255),2)
    cv2.circle(image,(cx2,cy2),10,(0,255,0),2)
    a = [cx,cy]
    b = [cx2,cy2]
    cv2.imwrite('test.png',image)
    return a, b 


print(trackStat((155, 120, 90), (180, 155, 190), (60, 50, 40),(120, 85, 100)))

