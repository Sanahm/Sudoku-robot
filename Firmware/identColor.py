#!/usr/bin/python
# -*- coding: utf-8 -*-
import picamera
import cv2

def identColor():
    camera = picamera.PiCamera()
    camera.resolution = (1080,1080)
    camera.start_preview()
    raw_input("Press enter to continue")
    camera.stop_preview()
    camera.capture('ident.jpg')
    im = cv2.imread('ident.jpg')
    hsv = cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
    print(hsv[540][540])

identColor()
    
