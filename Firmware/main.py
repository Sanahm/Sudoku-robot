from thresholding import *
from solver import *
from control_motor import *
t1=time.clock()
pwm.start(7)
capture()
t2=time.clock()
im = cv2.imread('rawImage.jpg',0)

rect, grille = threshHold(im)

cv2.imwrite('Grille.png',grille)
try:
    from mnist_model_convolutionnel import *
except:
    print("unable to recognize number make sure that the image is readable\n")



taille = conv_cote(rect[1][0],rect[1][1])
angle = calcul_angle(rect[2],ang)


try:
    mat = np.array(resolver(np.int_(recogn2).tolist()))
except:
    try:
        mat = np.array(resolver(np.int_(recogn1).tolist()))
    except:
        try:
            mat = np.array(resolver(np.int_(recogn3).tolist()))
        except:
            mat = np.array(resolver(np.int_(recogn).tolist()))

coin =calc_coin(angle)
print("Placer le stylo sur le coin " + str(coin))
raw_input("Press enter to continue")
t3 = time.clock()
print(t3-t1,t3-t2)
deplacement(mat,recogn,taille,coin,angle)




pwm.stop()
GPIO.cleanup()
t4 = time.clock()
print(t4-t1)
