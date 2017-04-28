from picamera.array import PiRGBArray
import picamera
import time
import cv2
import numpy as np

l = 480
L = 480


# initialisation de la camra
camera = picamera.PiCamera()
camera.resolution = (l, L)
camera.framerate = 30
camera.hflip = True
rawCapture = PiRGBArray(camera, size=(l, L))
time.sleep(0.1)
 
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        # Recuperation de la matrice décrivant l'image dans la frame
        image = frame.array

        # Conversion de l'image en hsv
        hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
        # Conservation des pixels d'interêt ie dans lal bonne plage de couleur
        thresh = cv2.inRange(hsv,np.array((60, 50, 40)), np.array((120, 85, 100)))
        # Recherche des contours
        (contours,_)  = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
        # Sélection du contour ayant la plus grande aire
        max_area = 1
        best_cnt = 1
        for cnt in contours:
                area = cv2.contourArea(cnt)
                if area > max_area:
                        max_area = area
                        best_cnt = cnt
        # Calcul des coordonnées du centre de gravité du contours le plus grand
        M = cv2.moments(best_cnt)
        cx,cy = int(M['m10']/M['m00']), int(M['m01']/M['m00'])
        # Ajout d'un cercle sur l'image centré sur le centre de gravité
        cv2.circle(image,(cx,cy),10,(0,0,255),2)
        # Ajout d'un cercle au centre de l'image qui permet de bien situé le centre de l'image
        cv2.circle(image,(l/2,L/2),10,(0,0,255),2)
        # Affichage de la valeur en HSV de la couleur du pixel au centre de l'image.
        print(hsv[l/2][L/2])
        # Affichage de l'image
        cv2.imshow("Frame", image)
        key = cv2.waitKey(1) & 0xFF
        rawCapture.truncate(0)
 
	# Si l'utilisateur presse la touche q on sort de la boucle
        if key == ord("q"):
        	break


