  #!/usr/bin/python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import numpy as np
from math import *
## parametrage raspberry pi
GPIO.setmode(GPIO.BOARD)  #notation board plutôt que BCM

    
m1_pin_bobine_1_1 = 3    #GPIO moteur haut
m1_pin_bobine_1_2 = 5    #GPIO 
m1_pin_bobine_2_1 = 11    #GPIO 
m1_pin_bobine_2_2 = 13    #GPIO 


m2_pin_bobine_1_1 = 8   #GPIO moteur planche
m2_pin_bobine_1_2 = 10    #GPIO 
m2_pin_bobine_2_1 = 16  #GPIO 
m2_pin_bobine_2_2 = 18    #GPIO 

m_standby= [0 , 7, 22] # standby des moteurs

servo_moteur = 12  #GPIO servomoteur

pin_fin_de_course1 = 21; 
pin_fin_de_course2 = 19;
pin_demarrage = 15;
pin_reset = 23;

pin_DEL_red = 24;
pin_DEL_jaune = 26;
pin_DEL_verte = 29;

# configuration des pins en sortie
GPIO.setup(m1_pin_bobine_1_1, GPIO.OUT)
GPIO.setup(m1_pin_bobine_1_2, GPIO.OUT)
GPIO.setup(m1_pin_bobine_2_1, GPIO.OUT)
GPIO.setup(m1_pin_bobine_2_2, GPIO.OUT)
GPIO.setup(m2_pin_bobine_1_1, GPIO.OUT)
GPIO.setup(m2_pin_bobine_1_2, GPIO.OUT)
GPIO.setup(m2_pin_bobine_2_1, GPIO.OUT)
GPIO.setup(m2_pin_bobine_2_2, GPIO.OUT)
GPIO.setup(m_standby[1], GPIO.OUT)
GPIO.setup(m_standby[2], GPIO.OUT)
GPIO.setup(servo_moteur, GPIO.OUT)
# configuration des pins en entree
GPIO.setup(pin_fin_de_course1, GPIO.IN)
GPIO.setup(pin_fin_de_course2, GPIO.IN)
GPIO.setup(pin_demarrage, GPIO.IN)
GPIO.setup(pin_reset, GPIO.IN)
GPIO.setup(pin_DEL_jaune, GPIO.IN)
GPIO.setup(pin_DEL_red, GPIO.IN)
GPIO.setup(pin_DEL_verte, GPIO.IN)
#constante et etat inital
GPIO.output(m_standby[1], 0)
GPIO.output(m_standby[2], 0)

pwm = GPIO.PWM(servo_moteur, 50) #servomoteur
pwm.start(7) #servomoteur

attente= 0.005 #définir et fixer en second, controle la vitesse des moteurs (plus attente grande, plus vitesse faible)
conv = 51 # conversion taille de la case - nombre de pas en pas/cm

conv_pix = 0.016 #conv de pixel en cm (depend de la hauteur de la camera)

def fin_de_course(m): #fonction qui ramene les moteurs en fin de course
    if m == 1 :#moteur 1
        GPIO.output(m_standby[m], 1)
        while GPIO.input(pin_fin_de_course1):
            
            for i in range(0, 4):# envoie des signaux de commandes au moteur
                prochainStep(3 - (i % 4),m)
                time.sleep(attente)
        GPIO.output(m_standby[m], 0)
    else:#moteur 2
        GPIO.output(m_standby[m], 1)
        while GPIO.input(pin_fin_de_course2):
            for i in range(0, 4):
                prochainStep(3 - (i % 4),m)
                time.sleep(attente)
        GPIO.output(m_standby[m], 0)
        
def calcul_angle(angle, ang ): #bas de la grille par rapport a l'horizontale ang est l'angle par pas de 90°
    if (-45<angle and angle<0) :
        angle = 360 - ang -angle
    else:
        angle = 360 - ang -angle - 90
    return angle

def conv_cote(largeur,longueur):#conversion de la taille de pixel a cm (moyenne de la largeur et longueur de la grille)
    return (float(largeur + longueur))*conv_pix/(9*2) 

def position_stylo(posi): #gère la position du stylo (0 stylo levé, 1 stylo baissé)    
    if (posi == 1):
        pwm.ChangeDutyCycle(12)
        time.sleep(0.6)
    if (posi == 0):
        pwm.ChangeDutyCycle(7)
        time.sleep(0.6)
    time.sleep(0.2)
    
    
def marche_avant(attente, nb_pas,m): # effectue une marche avant du moteur choisi avec le nombre de pas voulu (multiple de 4)
    nombre_de_pas = int(nb_pas)
    GPIO.output(m_standby[m], 1)
    for i in range(0, nombre_de_pas):
        prochainStep(i % 4,m)
        time.sleep(attente)
    GPIO.output(m_standby[m], 0)

def marche_arriere(attente, nb_pas,m): # effectue une marche arriere du moteur choisi avec le nombre de pas voulu (multiple de 4)
    nombre_de_pas = int(nb_pas)
    GPIO.output(m_standby[m], 1)
    for i in range(0, nombre_de_pas):
        prochainStep(3 - (i % 4),m)
        time.sleep(attente)
    GPIO.output(m_standby[m], 0)

def reglage_pins(pin1, pin2, pin3, pin4, m): # envoie les commandes au driver suivant le moteur

    if (m == 1):
        GPIO.output(m1_pin_bobine_1_1, pin1)
        GPIO.output(m1_pin_bobine_1_2, pin2)
        GPIO.output(m1_pin_bobine_2_1, pin3)
        GPIO.output(m1_pin_bobine_2_2, pin4)
    if (m == 2):
        GPIO.output(m2_pin_bobine_1_1, pin1)
        GPIO.output(m2_pin_bobine_1_2, pin2)
        GPIO.output(m2_pin_bobine_2_1, pin3)
        GPIO.output(m2_pin_bobine_2_2, pin4)

def prochainStep(numero,m):#Code a envoyer au driver
    if (numero == 0):
        reglage_pins(1, 0, 1, 0,m)
    if (numero == 1):
        reglage_pins(0, 1, 1, 0,m)
    if (numero == 2):
        reglage_pins(0, 1, 0, 1,m)
    if (numero == 3):
        reglage_pins(1, 0, 0, 1,m)
     
def rotation_et_deplacement(taille , angle, sens):# Déplacement des moteurs pour tracer un trait d'un tier d'une case de la grille suivant le sens voulu et l'angle
    trait = taille * conv / 3. # tous les chiffres sont composés de traits de même taille.
                                # la variable taille correspond au coté d'une case. trait correspond à un tier d'une case en pas
    nb_pas = 4 # nombre de pas minimum
    angle = angle * pi / 180 # conversion en radian
    traitm1 = cos(angle) * trait # nombre de pas total que doit effectuer le moteur 1
    traitm2 = sin(angle) * trait # nombre de pas total que doit effectuer le moteur 2
    
    
    # les moteurs avancent l'un après l'autre et le moteur avec le plus petit traitm doit faire seulement 4 pas (ou zero si trait paralelle a un axe des moteurs) alors
    #que l'autre moteur fera par exemple 8 pas (correspondant à un angle de 27° dans l'exemple pour traitm2 le plus petit)
    # ainsi le trait est tracé en escalier => evolution en implementant les threads (à faire)
    if (abs(traitm1) < abs(traitm2)):#si traitm1<traitm2 alors le moteur 1 doit faire 4 pas (ou 0 si traitm1 = 0)
        if (round(traitm1) == 0):
            pasm1 = 0
            pasm2 = round(sens*traitm2)
        else:
            pasm1 = round( nb_pas*traitm1*sens/abs(traitm1))# = 4 (avec le sens)
            pasm2 = round( nb_pas*traitm2*sens/abs(traitm1))# > 4 (avec le sens)
            
            
    else:
        if (round(traitm2) == 0):
            pasm2 = 0
            pasm1 = round(traitm1*sens)
        else:
            pasm1 = round( nb_pas*traitm1*sens/abs(traitm2))
            pasm2 = round( nb_pas*traitm2*sens/abs(traitm2))
           
    if(abs(pasm1) > trait):# le nombre de pas à effectuer ne doit pas etre plus grand que la variable trait (cas des petits angles)
        pasm1 = round(trait*pasm1/abs(pasm1))
        pasm2 = 0
    if(abs(pasm2) > trait):
        pasm2 = round(trait*pasm2/abs(pasm2))
        pasm1 = 0

    if abs(pasm1) < abs(pasm2) : #choix de fonctionnement dans la boucle while
        
        p =1
    else :
        
        p=2

    if pasm1 < 0: #permet de définir le sens des moteurs dans le boucle while car les fonctions marche_avant et marche_arriere ne prend que des entiers positifs
        sensm1 =-1
        pasm1 = abs(pasm1)
    else:
        sensm1 = 1
    if pasm2 < 0:
        sensm2 =-1
        pasm2 = abs(pasm2)
    else:
        sensm2 = 1
    
    depl = 0 # variable qui compte le nombre de pas effectué
    pas_err =0 # permet de compter le nombre de pas non effectué car si un des moteurs fait 4 pas l'autre peut en faire 13 or les moteurs ne font que
    #des multiples de 4 pas ainsi le moteur fera 12 pas et il y aura un pas d'erreur
    while (depl < trait-3):# test du nombre de pas effectué (-3 permet de s'affranchir à la fin du fait qu'il peut manquer 4 pas sans refaire une itération)
        
        
        if p == 1:# si pasm1<pasm2 alors pasm1 = 4 ou 0 donc pas besoin de tester les erreurs de pas sur pasm1
    
            
            if (sensm1 < 0): #selon le sens voulu
                marche_arriere(attente, pasm1,1)
            else:
                marche_avant(attente, pasm1, 1)
            
            pas_attente = pasm1# contribution du nombre de pas du moteur 1 a ajouter a depl
            
        
            pas_dep = pasm2 + pas_err #pasm2 avec les erreurs precedentes s'il y en a
            pas_err = pas_dep%nb_pas # compris entre 0 et 3 erreurs de pas à conserver
            pas_dep = pas_dep - pas_err #deplacement du moteur 2 avec un nombre de pas multiple de 4

            if (sensm2 > 0): #inversion par rapport au moteur 1 car c'est la feuille qui bouge
                marche_arriere(attente, pas_dep,2)
            else:
                marche_avant(attente, pas_dep, 2)
            
                

        else:# si pasm1>pasm2 alors pasm2 = 4 ou 0 donc pas besoin de tester les erreurs de pas sur pasm2
       
            if (sensm2 > 0): #inversion par rapport au moteur 1 car c la feuille qui bouge
                marche_arriere(attente, pasm2,2)
            else:
                marche_avant(attente, pasm2, 2)                


            pas_attente = pasm2
            
            
      
            pas_dep = pasm1 + pas_err
            pas_err = pas_dep%nb_pas
            pas_dep = pas_dep - pas_err
            if (sensm1 < 0): 
                marche_arriere(attente, pas_dep,1)
            else:
                marche_avant(attente, pas_dep, 1)
            
            
                
        depl = depl + sqrt(pas_dep*pas_dep+pas_attente*pas_attente) # calcul du nombre de pas effectué (hypotenuse)
        if p ==1:
            if(abs((trait -depl)*sin(angle)) < pasm2): # permet de determiner s'il reste moins de pasm2 à parcourir et réajuster le pasm2 afin que
                #depl ne dépasse pas trait
                pasm2 = abs(round(sin(angle)*(trait - depl)))
        else:
            if(abs((trait -depl)*cos(angle)) < pasm1):#idem dans le cas pasm1>pasm2 pour pasm1
                pasm1 = abs(round(cos(angle)*(trait - depl)))

        
        

def trait_hori(taille, angle, sens):#tracer un trait horizontal
    rotation_et_deplacement(taille , angle, sens)

def trait_verti(taille, angle, sens):#tracer un trait vertical
    rotation_et_deplacement(taille , angle + 90, sens)

def write_one(taille,angle):# ecriture du chiffre un avec l'utilisation du stylo, le stylo revient toujours au meme endroit
    trait_hori(taille, angle, 1)
    position_stylo(1)
    trait_verti(2*taille, angle, 1)
    position_stylo(0)
    trait_verti(2*taille, angle, -1)
    trait_hori(taille, angle, -1)

def write_two(taille,angle):
    
    trait_hori(taille, angle, 1)
    position_stylo(1)
    trait_hori(taille, angle, -1)
    trait_verti(taille, angle, 1)
    trait_hori(taille, angle, 1)
    trait_verti(taille, angle, 1)
    trait_hori(taille, angle, -1)
    position_stylo(0)
    trait_verti(2*taille, angle, -1)

def write_three(taille,angle):
    position_stylo(1)
    trait_hori(taille, angle, 1)
    trait_verti(taille, angle, 1)
    trait_hori(taille, angle, -1)
    trait_hori(taille, angle, 1)
    trait_verti(taille, angle, 1)    
    trait_hori(taille, angle, -1)
    position_stylo(0)
    trait_verti(2*taille, angle, -1) 

def write_four(taille,angle):
    
    trait_hori(taille, angle, 1)
    position_stylo(1)
    trait_verti(2*taille, angle, 1)
    trait_verti(taille, angle, -1)
    trait_hori(taille, angle, -1)
    trait_verti(taille, angle, 1)
    position_stylo(0)
    trait_verti(2*taille, angle, -1) 


def write_five(taille,angle):
    position_stylo(1)
    trait_hori(taille, angle, 1)
    trait_verti(taille, angle, 1)
    trait_hori(taille, angle, -1)
    trait_verti(taille, angle, 1)
    trait_hori(taille, angle, 1)
    position_stylo(0)
    trait_verti(2*taille, angle, -1)
    trait_hori(taille,angle,-1)

def write_six(taille,angle):
    trait_hori(taille, angle, 1)
    trait_verti(2*taille, angle, 1)
    position_stylo(1)
    trait_hori(taille, angle, -1)
    trait_verti(2*taille, angle, -1)
    trait_hori(taille, angle, 1)
    trait_verti(taille, angle, 1)
    trait_hori(taille, angle, -1)
    position_stylo(0)
    trait_verti(taille, angle, -1) 

def write_seven(taille,angle):
    trait_hori(taille, angle, 1)
    position_stylo(1)
    trait_verti(2*taille, angle, 1)
    trait_hori(taille, angle, -1)
    position_stylo(0)
    trait_verti(2*taille, angle, -1) 

def write_heigt(taille,angle):
    position_stylo(1)
    trait_hori(taille, angle, 1)
    trait_verti(taille, angle, 1)
    trait_hori(taille, angle, -1)
    trait_verti(taille, angle, -1)
    trait_verti(2*taille, angle, 1)
    trait_hori(taille, angle, 1)
    trait_verti(2*taille, angle, -1)
    position_stylo(0)
    trait_hori(taille,angle,-1)

def write_nine(taille,angle):
    position_stylo(1)
    trait_hori(taille, angle, 1)
    trait_verti(2*taille, angle, 1)
    trait_hori(taille, angle, -1)
    trait_verti(taille, angle, -1)
    trait_hori(taille, angle, 1)
    position_stylo(0)
    trait_verti(taille, angle, -1)
    trait_hori(taille, angle, -1) 

options = { #bibliotheque des chiffres
                1 : write_one,
                2 : write_two,
                3 : write_three,
                4 : write_four,
                5 : write_five,
                6 : write_six,
                7 : write_seven,
                8 : write_heigt,
                9 : write_nine,

}

def number_write(taille, angle, number): #fonction d'écriture des chiffres (la taille est legerement diminuée pour eviter les imperfections d'écriture
    taille = taille * 0.8
    options[number](taille,angle)

def deplacement(mat,recogn,taille,coin,angle):#deplacement de case en case avec ecriture des chiffres quand il le faut. (deplacement en serpent)
    n = 1;#initialisation du nombre de case parcouru (81 en tout)
    if coin == 1: #si le coin ou est positionné le stylo est le coin 1
        trait_verti(2.5*taille,angle,-1) #On se positionne à dans la case à un tier du bas de la case et un tier
                                          #du coté gauche de la case (pareil pour toutes les cases)
        trait_hori(taille, angle, 1)
        raw_input("Verify and press enter to continue")
        i = 0 #premiere case en haut a gauche
        j = 0
        if(recogn[i][j] == 0):   # si 0 alors case vide, il faut ecrire un chiffre          
            number_write(taille, angle, mat[i][j])
        j=1
        trait_hori(3*taille, angle, 1)#deplacement à la case suivante
        while n < 81:
            
    

            if(recogn[i][j] == 0):            
                number_write(taille, angle, mat[i][j])
                
            if ((j !=8 and j != 0)):# si on est sur un bord alors il faut passer à la ligne d'en dessous

                if(i%2 == 0):# ligne paire, on se deplace vers la droite
                    trait_hori(3*taille, angle, 1)
                    j=j+1
                else:#ligne impaire , on se deplace vers la gauche
                    trait_hori(3*taille, angle, -1)
                    j=j-1
            else:# passage à la ligne en dessous
                trait_verti(3*taille,angle,-1)#desente d'une ligne
                i = i+1 #incrémentation des lignes
                if(i>8): break #si on depasse le nombre de ligne, on sort de la boucle afin d'éviter d'écrire de nouveau chiffre
                if(recogn[i][j] == 0): #on reteste la case dans le else sinon à la prochaine iteration on repasse dans le else            
                    number_write(taille, angle, mat[i][j])
                if(i%2 == 0):
                    trait_hori(3*taille, angle, 1)
                    j=j+1
                else:
                    trait_hori(3*taille, angle, -1)
                    j=j-1
                n = n+1
                
            n = n+1
            
            
    if coin == 2: #demarrage au coin 2 en haut a droite
        trait_verti(2.5*taille,angle,-1)
        trait_hori(2*taille, angle, -1)
        raw_input("Press enter to continue")

        i = 0
        j = 8
        if(recogn[i][j] == 0):            
            number_write(taille, angle, mat[i][j])
        j=7
        trait_hori(3*taille, angle, -1)
        while n < 81:
            
       

            if(recogn[i][j] == 0):            
                number_write(taille, angle, mat[i][j])
                
            if (j !=8 and j != 0):

                if(i%2 == 0):
                    trait_hori(3*taille, angle, -1)
                    j=j-1
                else:
                    trait_hori(3*taille, angle, 1)
                    j=j+1
            else:
                trait_verti(3*taille,angle,-1)
                i = i+1
                if(i>8): break
                if(recogn[i][j] == 0):            
                    number_write(taille, angle, mat[i][j])
                if(i%2 == 0):
                    trait_hori(3*taille, angle, -1)
                    j=j-1
                else:
                    trait_hori(3*taille, angle, 1)
                    j=j+1
                n = n+1
            n = n+1
            
    if coin == 3:
        trait_verti(0.5*taille,angle,1)
        trait_hori(taille, angle, 1)
        raw_input("Press enter to continue")

        i = 8
        j = 0
        if(recogn[i][j] == 0):           
            number_write(taille, angle, mat[i][j])
        j=1
        trait_hori(3*taille, angle, 1)
        while n < 81:
     
            #print(i,j,n)
           
            if(recogn[i][j] == 0):            
                number_write(taille, angle, mat[i][j])
                
            if (j !=8 and j != 0):

                if(i%2 == 0):
                    trait_hori(3*taille, angle, 1)
                    j=j+1
                else:
                    trait_hori(3*taille, angle, -1)
                    j=j-1
            else:
                trait_verti(3*taille,angle,1)
                i = i-1
                if(i<0): break
                if(recogn[i][j] == 0):            
                    number_write(taille, angle, mat[i][j])
                if(i%2 == 0):
                    trait_hori(3*taille, angle, 1)
                    j=j+1
                else:
                    trait_hori(3*taille, angle, -1)
                    j=j-1
                n = n+1
            n = n+1
            
            

    if coin == 4:
        trait_verti(0.5*taille,angle,1)
        trait_hori(2*taille, angle, -1)
        raw_input("Press enter to continue")

        i = 8
        j = 8
        if(recogn[i][j] == 0):            
            number_write(taille, angle, mat[i][j])
        j=7
        trait_hori(3*taille, angle, -1)
        while n < 81:
            
     

            if(recogn[i][j] == 0):            
                number_write(taille, angle, mat[i][j])
                
            if (j !=8 and j != 0):

                if(i%2 == 0):
                    trait_hori(3*taille, angle, -1)
                    j=j-1
                else:
                    trait_hori(3*taille, angle, 1)
                    j=j+1
            else:
                trait_verti(3*taille,angle,1)
                i = i-1
                if(i<0): break
                if(recogn[i][j] == 0):            
                    number_write(taille, angle, mat[i][j])
                if(i%2 == 0):
                    trait_hori(3*taille, angle, -1)
                    j=j-1
                else:
                    trait_hori(3*taille, angle, 1)
                    j=j+1
                n = n+1
            n = n+1
            

def calc_coin(angle): # renvoi le coin sur lequel le stylo doit etre positionné (stylo initalement tout a gauche, le coin et aussi toujours celui le plus a gauche)
    #coin 1 en haut a gauche de la grille
    #coin 2 en haut a droite
    #coin 3 en bas à gauche
    #coin 4 en bas à droite
    angle = angle%360
    if (angle <=90 and angle >0):
        coin = 1
    elif (angle <=180 and angle >90):
        coin = 2
    elif (angle <=270 and angle >180):
        coin = 4
    else:
        coin = 3
    return coin




def track():#fonction de controle des moteurs avec tracking grace à la camera (a faire)
    a,b = trackStat((155, 120, 90), (180, 155, 190), (60, 50, 40),(120, 85, 100)) 
    #a point rouge, b point vert
    # ([894, 366], [793, 884])

#intialisation des moteurs en position de démarrage    
position_stylo(0)
fin_de_course(1)
fin_de_course(2)



#### a decommenter pour test ####
##pwm.stop()
##GPIO.cleanup()
