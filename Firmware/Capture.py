#!/usr/bin/python
# -*- coding: utf-8 -*-
import picamera

def capture():
    camera = picamera.PiCamera()
    camera.rotation = 180
    camera.start_preview()
    raw_input("Press enter to continue")
    camera.stop_preview()
    camera.capture('rawImage.jpg')

#capture()
