import numpy as np
from matplotlib import pyplot as plt
import cv2
from random import *

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
def binarization(img,wx,wy,R,k):
    lx,ly = img.shape
    shape = (lx+2*wx,ly+2*wy)
    imCpExt = np.zeros(shape)
    imCpExt[wx:lx+wx,wy:ly+wy] = img
    imCpExt[wx:lx+wx,0:wy] = img[:,0:wy]
    imCpExt[wx:lx+wx,ly+wy:ly+2*wy] = img[:,ly-wy:ly]
    imCpExt[0:wx,:] = imCpExt[wx:2*wx,:]
    imCpExt[lx+wx:lx+2*wx,:] = imCpExt[lx:lx+wx,:]
    I = np.zeros(shape)
    m = np.zeros(img.shape)
    s = np.zeros(img.shape)
    t = np.zeros(img.shape)
    for x in range(0,lx+2*wx):
        for y in range(0,ly+2*wy):
            I[x][y] = np.sum(imCpExt[:x+1,:y+1])
    for x in range(0,lx):
        for y in range(0,ly):
            m[x][y] = (I[x+wx][y+wy] + I[x-wx][y-wy] - I[x+wx][y-wy] - I[x-wx][y+wy])/(4*wx*wy)
            s[x][y] = np.sqrt(abs(np.sum(imCpExt[x-wx:x+wx,y-wy:y+wy]**2 - m[x][y]**2)/(4*wx*wy)))
            t[x][y] = m[x][y]*(1+k*(s[x][y]/R - 1)) #threshold
            if img[x][y]<= t[x][y]:
                img[x][y] = 0
            else:
                img[x][y] = 255
    print(imCpExt)
    return img

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
    if(flag == cv2.THRESH_OTSU):
        retval,imB = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    if(flag == cv2.ADAPTIVE_THRESH_GAUSSIAN_C):
        imB = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,7,2)
    if(flag == cv2.ADAPTIVE_THRESH_MEAN_C):
        imB = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,7,2)
    return retval,imB

def tri_insertion(lines,eps_rho,esp_theta):
    for i in range(lines.shape[0]):
        j=i-1
        while(j>=0):
            if(abs(lines[j][0][0]-lines[j+1][0][0])>eps_rho and abs(lines[j][0][1]-lines[j+1][0][1])<eps_theta):
                #then, in this case sort by following rho
                if(lines[j][0][0]>lines[j+1][0][0]):
                    lines[j][0][0],lines[j+1][0][0]=lines[j+1][0][0],lines[j][0][0]
                    lines[j][0][1],lines[j+1][0][1]=lines[j+1][0][1],lines[j][0][1]
            if(abs(lines[j][0][0]-lines[j+1][0][0])<eps_rho and abs(lines[j][0][1]-lines[j+1][0][1])>eps_theta):
                #then, in this case sort by following theta
                if(lines[j][0][1]>lines[j+1][0][1]):
                    lines[j][0][0],lines[j+1][0][0]=lines[j+1][0][0],lines[j][0][0]
                    lines[j][0][1],lines[j+1][0][1]=lines[j+1][0][1],lines[j][0][1]
            if(abs(lines[j][0][0]-lines[j+1][0][0])>eps_rho and abs(lines[j][0][1]-lines[j+1][0][1])>eps_theta):
                if(lines[j][0][0]>lines[j+1][0][0]):
                    lines[j][0][0],lines[j+1][0][0]=lines[j+1][0][0],lines[j][0][0]
                    lines[j][0][1],lines[j+1][0][1]=lines[j+1][0][1],lines[j][0][1]
            j -= 1


def tri_stat(stat,eps):
    for i in range(stat.shape[0]):
        j = i-1
        while(j>=0):
            if(abs(stat[j][1]-stat[j+1][1]) < eps and stat[j][0] > stat[j+1][0]):
                stat[j][0],stat[j][1],stat[j][2],stat[j][3],stat[j+1][0],stat[j+1][1],\
                stat[j+1][2],stat[j+1][3] = stat[j+1][0],stat[j+1][1],stat[j+1][2],\
                stat[j+1][3],stat[j][0],stat[j][1],stat[j][2],stat[j][3]            
            j -=1

def StDev(im):
    mean = cv2.mean(im)[0]
    stdev = cv2.mean(np.square(im-mean))[0]
    return stdev



             
def ExtractBoxes(imBinarized,connexity,thresh):
    """ Take a binarized image thresholded and search the eventual boxes inside using thresh
    Parameters:
    -----------
    imBinarized: input image
    connexity : 4 or 8 (refer to cv2.connectedComponentsWithStats(...) doc)
    thresh : array of 1x2= (thresh_min_x,thresh_min_y,thresh_max_x,thresh_max_y) which means that the
            researched boxes should be at least thresh_min_x large and thresh_min_y height and at most
            thresh_max large and thresh_max_y height
    Returns:
    --------
    stat: an array of Nx5 where N means the number of boxes found and 5, 5 rows according to
           cv2.connectedComponentsWithStats(...) doc.
           
    PLEASE REFER TO THE OPENCV DOC FOR MORE INFORMATIONS
    """
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
    return stat

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
        imR = img[stat[i][1]:stat[i][1]+stat[i][3],stat[i][0]:stat[i][0]+stat[i][2]]
        imR = cv2.resize(imR,imgFlat,interpolation=method)
        imBox[i] = np.reshape(imR,imgFlat[0]*imgFlat[1])
    return imBox


#def Houg            
    
im = cv2.imread('C:/Users/Mohamed/Documents/2ASicom/Sudoku-robot/Firmware/images/sud5.jpg')#,cv2.IMREAD_GRAYSCALE)
img = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
lx,ly = img.shape #image weidth and heigth
#plt.plot(px)
#plt.show()
#fig, axes = plt.subplots(2,2)
ret,imB = binarize(img,cv2.THRESH_OTSU)
px = 255 - xyproject(img,axis = 0)
py = 255 - xyproject(img,axis = 1)
pxB = 255 - xyproject(imB,axis = 0)
pyB = 255 - xyproject(imB,axis = 1)

##edges = cv2.Canny(img,50,150,apertureSize = 3)
##print(img.shape[1])
##print(img.shape)
##minLineLength = img.shape[1]-1
##maxLineGap = 10
##lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
##for x1,y1,x2,y2 in lines[0]:
##    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
edges = cv2.Canny(img,50,150,apertureSize = 3)  
lines = cv2.HoughLines(edges,1,np.pi/180,110)
eps_rho = int(min(lx/9,ly/9)/2)
eps_theta = np.pi/8
def HoughGrid(lines,eps_rho,eps_theta):
    tri_insertion(lines,eps_rho,eps_theta)
    grid = np.zeros((20,2)) #sudoku's grid have 20 lines. 2 =>(rho,theta)
    j = 0
    for i in range(lines.shape[0]):
        if(lines[i][0][0] < 0 or lines[i][0][1] < 0):
            continue
        if(abs(lines[i][0][0] - grid[j-1][0]) > eps_rho or abs(lines[i][0][1] - grid[j-1][1]) > eps_theta):
            grid[j] = lines[i][0]
            j +=1
        else:
            grid[j-1] = (grid[j-1] + lines[i][0])/2
    return grid



        
##for i in range(lines.shape[0]):
##    rho = lines[i][0][0]
##    theta = lines[i][0][1]
##    a = np.cos(theta)
##    b = np.sin(theta)
##    x0 = a*rho
##    y0 = b*rho
##    x1 = int(x0 + 1000*(-b))
##    y1 = int(y0 + 1000*(a))
##    x2 = int(x0 - 1000*(-b))
##    y2 = int(y0 - 1000*(a))
##    cv2.line(im,(x1,y1),(x2,y2),(0,0,255),2)
##    cv2.imshow('hjb',im)
##cv2.imwrite("hough1.png",im)
##    while(1):
##        k = cv2.waitKey(1) & 0xFF
##        if(k==ord('c')):
##            cv2.destroyAllWindows()
##            break
    
stat = ExtractBoxes(imB,connexity = 8,thresh=(lx/18,ly/18,lx/3,ly/3))
tri_stat(stat,lx/18)
##fig,axis = plt.subplots(9,9)
##fig.subplots_adjust(hspace=0.3, wspace=0.3)
I = (imB/255)*img
imBox = ExtractBoxImage(stat,I,(28,28),cv2.INTER_CUBIC)
imBox1 = ExtractBoxImage(stat,I,(28,28),cv2.INTER_AREA)
imBox2 = ExtractBoxImage(stat,I,(28,28),cv2.INTER_LINEAR)
imBox3 = ExtractBoxImage(stat,I,(28,28),cv2.INTER_LANCZOS4)
mat = np.array([StDev(imBox[i]) for i in range(imBox.shape[0])]).reshape((9,9))
mean_stdev = cv2.mean(mat)[0]
alpha = 0.7
mat = (mat > mean_stdev*alpha)*1 #pour convertir bool -> int
##for i in range(imBox.shape[0]):
##    cv2.imwrite('C:/Users/Mohamed/Documents/2ASicom/Sudoku-robot/Firmware/images/tests/box '+str(i)+'.png',imBox[i].reshape((28,28)))
##for i,ax in enumerate(axis.flat):
##    ax.imshow(imBox[i].reshape((28,28)),cmap='gray')
##    ax.set_xticks([])
##    ax.set_yticks([])
##plt.show()
                                                                

##for i in range(stat.shape[0]):
##    cv2.rectangle(im,(stat[i][0],stat[i][1]),(stat[i][0]+stat[i][2],stat[i][1]+stat[i][3]),\
##                  (randint(0,255),randint(0,255),randint(0,255)),2)
##    cv2.imshow('hjb',im)
##    while(1):
##        k = cv2.waitKey(1) & 0xFF
##        if(k==ord('c')):
##            cv2.destroyAllWindows()
##            break

#cv2.imwrite('C:/Users/Mohamed/Documents/2ASicom/Sudoku-robot/Firmware/images/test.png',img)
##cv2.imshow('sud1',imB)
##cv2.waitKey(0)
##cv2.destroyAllWindows()
#plt.subplots_adjust(-0.1,-0.1)
##plt.subplot(221),plt.imshow(img,cmap="gray"),plt.title("image de la grille")
##plt.subplot(222),plt.plot(px),plt.title("projection img sur x"),plt.xlabel("x"),plt.ylabel("nbre pixel")
##plt.subplot(224),plt.plot(py),plt.title("projection img sur y"),plt.xlabel("y"),plt.ylabel("nbre pixel")
##plt.subplot(223),plt.plot(pxB),plt.title("projection imB sur x")
##plt.subplot(224),plt.plot(pyB),plt.title("projection imB sur y")
##plt.show()
##cv2.imshow('sud1',imB)
##cv2.waitKey(0)
##cv2.destroyAllWindows()
