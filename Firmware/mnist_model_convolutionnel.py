#!/usr/bin/python
# -*- coding: utf-8 -*-
import cv2
from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import time
from datetime import timedelta
import math
from processing import *
from database import *

def CreateNewWeights(shape):
    """
    permet de créer rapidement une matrice de poids selon le shape spécifié. La matrice(ou vecteur) de retour
    est de taille shape et contient des valeurs qui suivent la loi normale tronquée (truncated_normal)
    stddev = écart type   
    """
    return tf.Variable(tf.truncated_normal(shape,stddev=0.05))



def CreateNewBiases(length):
    """
    permet de créer rapidement un vecteur de biais de taille length suivant la loi
    uniforme
    """
    
    return tf.Variable(tf.constant(0.05,shape=[length]))



def CreateNewConvolutionalLayer(inputs, numOfInputChannel, filterSize, numOfFilters, usePooling=True):
    """
    This function allow to create a new convolutional layer.
    Parameters:
    -----------
    inputs: the input image. it is a 4-dimension tensor(you know that image is a 3-dim matrix if you consider channels
    so just imagine a list of image: t's 4-dim):
                    1 - the image number
                    2 - Y-axis of each image
                    3 - X-axis of each image
                    4 - channels of each image
    numOfInputChannel: the number of input channels
    filterSize: the filter size
    numOfFilters: number of filter
    usePooling: if true, use 2x2 max-pooling

    Return:
    -------
    layer : the output layer (4-dim)
    weights: the tensor of weights that has been used    
    """
    
    shape = [filterSize, filterSize,numOfInputChannel, numOfFilters]
    weights = CreateNewWeights(shape = shape)
    biases = CreateNewBiases(length = numOfFilters)
    
    layer = tf.nn.conv2d(input = inputs,
                         filter = weights,
                         strides = [1,1,1,1],
                         padding ='SAME')
    layer += biases
    if(usePooling):
        layer = tf.nn.max_pool(value = layer,
                               ksize = [1,2,2,1],
                               strides = [1,2,2,1],
                               padding = 'SAME')
        
    layer = tf.nn.relu(layer)
    return layer,weights



def FlattenLayer(layer):
    """
    Allow you to quick flatten a layer as the layer is a 4-dim tensor, we need to
    reduce the 4-dim to 2-dim which will be use as the input of the function
    FullyConnectLayer(...)
    Parameters:
    -----------
    layer: the 4-dim tensor
    Return:
    -------
    flattenedLayer: 2-dim tensor
    numFeatures: the number of features = img_height * img_width * num_channels
    """
    
    layerShape = layer.get_shape()
    numFeatures = layerShape[1:4].num_elements()
    flattenedLayer = tf.reshape(layer,[-1,numFeatures])
    return flattenedLayer,numFeatures




def FullyConnectLayer(inputs,numOfinput,numOfOutput,useRelu=True):
    """
    Return layer = inputs*weights + biases where weights is a matrix of dim [numOfinput,numOfOutput]
    and biases of dim numOfOutput
    """
    weights = CreateNewWeights(shape = [numOfinput,numOfOutput])
    biases = CreateNewBiases(length = numOfOutput)

    layer = tf.matmul(inputs,weights)+biases
    if(useRelu):
        layer = tf.nn.relu(layer)
    return layer



# Counter for total number of iterations performed so far.
total_iterations = 0



def optimize(num_iterations):
    """
    Run optimization on trainning database.
    Parameters:
    -----------
    num_iterations : the number of iteration to converge the model
    Returns:
    --------
    Accuracy each iteration
    """
    # Ensure we update the global variable rather than a local copy.
    global total_iterations

    # Start-time used for printing time-usage below.
    start_time = time.time()

    for i in range(total_iterations,
                   total_iterations + num_iterations):

        # Get a batch of training examples.
        # x_batch now holds a batch of images and
        # y_true_batch are the true labels for those images.
        x_batch, y_true_batch = data.train.next_batch(train_batch_size)

        # Put the batch into a dict with the proper names
        # for placeholder variables in the TensorFlow graph.
        feed_dict_train = {x: x_batch,
                           y_true: y_true_batch}

        # Run the optimizer using this batch of training data.
        # TensorFlow assigns the variables in feed_dict_train
        # to the placeholder variables and then runs the optimizer.
        session.run(optimizer, feed_dict=feed_dict_train)

        # Print status every 100 iterations.
        if i % 100 == 0:
            # Calculate the accuracy on the training-set.
            acc = session.run(accuracy, feed_dict=feed_dict_train)

            # Message for printing.
            msg = "Optimization Iteration: {0:>6}, Training Accuracy: {1:>6.1%}"

            # Print it.
            print(msg.format(i + 1, acc))

    # Update the total number of iterations performed.
    total_iterations += num_iterations

    # Ending time.
    end_time = time.time()

    # Difference between start and end-times.
    time_dif = end_time - start_time

    # Print the time-usage.
    print("Time usage: " + str(timedelta(seconds=int(round(time_dif)))))



# Split the test-set into smaller batches of this size.
test_batch_size = 22 #256








def print_test_accuracy():
    """
    Allow you to print the accuracy of the model in test database after optimisation
    """
    # Number of images in the test-set.
    num_test = len(data.test.images)

    # Allocate an array for the predicted classes which
    # will be calculated in batches and filled into this array.
    cls_pred = np.zeros(shape=num_test, dtype=np.int)

    # Now calculate the predicted classes for the batches.
    # We will just iterate through all the batches.
    # There might be a more clever and Pythonic way of doing this.

    # The starting index for the next batch is denoted i.
    i = 0

    while i < num_test:
        # The ending index for the next batch is denoted j.
        j = min(i + test_batch_size, num_test)

        # Get the images from the test-set between index i and j.
        images = data.test.images[i:j, :]

        # Get the associated labels.
        labels = data.test.labels[i:j, :]

        # Create a feed-dict with these images and labels.
        feed_dict = {x: images,
                     y_true: labels}

        # Calculate the predicted class using TensorFlow.
        cls_pred[i:j] = session.run(y_pred_cls, feed_dict=feed_dict)

        # Set the start-index for the next batch to the
        # end-index of the current batch.
        i = j

    # Convenience variable for the true class-numbers of the test-set.
    cls_true = data.test.cls

    # Create a boolean array whether each image is correctly classified.
    correct = (cls_true == cls_pred)

    # Calculate the number of correctly classified images.
    # When summing a boolean array, False means 0 and True means 1.
    correct_sum = correct.sum()

    # Classification accuracy is the number of correctly classified
    # images divided by the total number of images in the test-set.
    acc = float(correct_sum) / num_test

    # Print the accuracy.
    msg = "Accuracy on Test-Set: {0:.1%} ({1} / {2})"
    print(msg.format(acc, correct_sum, num_test))






    
#definition de quelques paramètres importants
learning_rate = 0.3
training_iteration = 10
batch_size = 100
display_step = 2
img_size = 28 #la taille des images dans MNIST est de 28 pixels
img_size_flat = img_size*img_size #28x28 pixels, la matrice 2D l'image est transformée en un vecteur
img_shape = (img_size,img_size) #qui sera réutilisé plus tard pour convertir le vecteur en image
num_classes = 10 #10 classes possibles 0-9
num_channels = 1
filter1_size = 5
filter2_size = 5
num_filter1 = 16
num_filter2 = 36
train_batch_size = 42 #256#22


#***************************************************************************#
#       DEFINITION DU MODEL: ICI RESEAUX DE NEURONES COVOLUTIFS             #
#          DEFINITION OF MODEL: HERE IS CONVOLUTIVE NETWORK                 #
#***************************************************************************#






#data = input_data.read_data_sets("/home/pi/Documents/Sudoku/tensor/",one_hot=True)
data.test.cls = np.array([label.argmax() for label in data.test.labels])
x = tf.placeholder("float",[None, img_size_flat],name='x')
x_reshape = tf.reshape(x,shape = [-1,img_size,img_size,num_channels], name='x_reshape')

y_true = tf.placeholder(dtype=tf.float32, shape=[None,10], name='y_true')
y_true_cls = tf.argmax(y_true,dimension=1)


#First convolutional layer

layerConv1,weightsConv1 = CreateNewConvolutionalLayer(inputs = x_reshape,
                                                      numOfInputChannel = num_channels,
                                                      filterSize = filter1_size,
                                                      numOfFilters = num_filter1,
                                                      usePooling = True)
#Second convolutional layer

layerConv2,weightsConv2 = CreateNewConvolutionalLayer(inputs = layerConv1,
                                                      numOfInputChannel = num_filter1,
                                                      filterSize = filter2_size,
                                                      numOfFilters = num_filter2,
                                                      usePooling = True)

#Flatten Layer

flattenedLayer,numFeatures = FlattenLayer(layerConv2)

#Fully-Connected Layer 1

firstConnectedLayerSize = 128
connectedLayer1 = FullyConnectLayer(inputs = flattenedLayer,
                                    numOfinput = numFeatures,
                                    numOfOutput = firstConnectedLayerSize,
                                    useRelu = True)


#Fully-Connected Layer 2

secondConnectedLayerSize = 10 #==> num_classes
connectedLayer2 = FullyConnectLayer(inputs = connectedLayer1,
                                    numOfinput = firstConnectedLayerSize,
                                    numOfOutput = secondConnectedLayerSize,
                                    useRelu = True)


#So here we have the output of our graph and we are going to determine thre predicted classe

y_pred = tf.nn.softmax(connectedLayer2)
y_pred_cls = tf.argmax(y_pred, dimension = 1)

#Now were are going to define the cost function to be optimize

cost_function = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=connectedLayer2, labels=y_true))
#or you can use the EQM = sum((y_pred-y_true)^2)/N where N is the number of input images
#cost_function = tf.reduce_mean(tf.square(y_pred-y_true)) #EQM

#Definition of optimization method. Here we use AdamOptimizer but you can use GradientDescendOptimizer is you use
#for exemple the EQM

#optimizer = tf.train.AdamOptimizer(learning_rate = 1e-4).minimize(cost_function)
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost_function)


#Performance Measures

predictions = tf.equal(y_pred_cls,y_true_cls) #vector of boolean that show the matched and unmatched prediction

accuracy = tf.reduce_mean(tf.cast(predictions,tf.float32))






#***************************************************************************#
#              NOW WE ARE GOING TO START TRAINING OUR MODEL                 #
#***************************************************************************#




init = tf.global_variables_initializer()
saver = tf.train.Saver()
session = tf.Session()
session.run(init)
#optimize(4000) #if you want to train the model so uncomment this
#saver.save(session,"./tensor/tensor_v1.0") and this to save it in the specifief directory

#I had already train a model so I have just restore it here

saver.restore(session,"./tensor/tensor_v1.0") #Allow you to restore previous trained session
feed_dict = {x:(255-imBox)/255} #charge imBox which contains the cases of sudoku image with interpolation bicubic
feed_dict1 = {x:(255-imBox1)/255} # inter_area
feed_dict2 = {x:(255-imBox2)/255} # linear
feed_dict3 = {x:(255-imBox3)/255} #lanczos4
recogn = session.run(y_pred_cls,feed_dict).reshape((9,9))
re = session.run(connectedLayer2,feed_dict)
rem = np.zeros(re.shape[0])
decision = 0
for i in range(re.shape[0]):
    rem[i] = re[i][re[i].argmax()]
s = sum(rem)
for k in range(1,4):

    imBox = ExtractBoxImage(ExtractBoxes(np.rot90(imB*I,k)),np.rot90(imB,k),(28,28),cv2.INTER_CUBIC)
    feed_dict = {x:(255-imBox)/255}
    re = session.run(connectedLayer2,feed_dict)
    for i in range(re.shape[0]):
        rem[i] = re[i][re[i].argmax()]
    if(sum(rem)>s):
        s = sum(rem)
        decision = k
if(decision >= 0):

    #I try different interpolations to see the result (bicubic, bilinear,lanczos4,area) see opencv doc for more info
    imBox = ExtractBoxImage(ExtractBoxes(np.rot90(imB*I,decision)),np.rot90(imB,decision),(28,28),cv2.INTER_CUBIC)
    imBox1 = ExtractBoxImage(ExtractBoxes(np.rot90(imB*I,decision)),np.rot90(imB,decision),(28,28),cv2.INTER_AREA)
    imBox2 = ExtractBoxImage(ExtractBoxes(np.rot90(imB*I,decision)),np.rot90(imB,decision),(28,28),cv2.INTER_LINEAR)
    imBox3 = ExtractBoxImage(ExtractBoxes(np.rot90(imB*I,decision)),np.rot90(imB,decision),(28,28),cv2.INTER_LANCZOS4)
    feed_dict = {x:(255-imBox)/255}
    feed_dict1 = {x:(255-imBox1)/255}
    feed_dict2 = {x:(255-imBox2)/255}
    feed_dict3 = {x:(255-imBox3)/255}
    recogn = session.run(y_pred_cls,feed_dict).reshape((9,9))
    recogn1 = session.run(y_pred_cls,feed_dict1).reshape((9,9))
    recogn2 = session.run(y_pred_cls,feed_dict2).reshape((9,9))
    recogn3 = session.run(y_pred_cls,feed_dict3).reshape((9,9))
ang = 90*decision


#This is for just in case you want to add imBox to database so you can improve (feed) your database

###np.int_(recogn).tolist()
##print(recogn)
##print(recogn1)
##print(recogn2)
##print(recogn3)
##res = input("Do you want to save in the database?[Y/N]\n")
##if(res == "Y"):
##    res = input("What recogn do you want to save?[1,2,3,4]")
##    if(res == "1"):
##        for i in range(len(imBox)):
##            cv2.imwrite("./database/"+str(recogn[i/9][i%9])+"aa"+str(i)+".png",imBox[i].reshape((28,28)))
##    res = input("What recogn do you want to save?[1,2,3,4]")
##    if(res == "2"):
##        for i in range(len(imBox)):
##            cv2.imwrite("./database/"+str(recogn1[i/9][i%9])+"bb"+str(i)+".png",imBox1[i].reshape((28,28)))
##    res = input("What recogn do you want to save?[1,2,3,4]")
##    if(res == "3"):
##        for i in range(len(imBox)):
##            cv2.imwrite("./database/"+str(recogn2[i/9][i%9])+"cc"+str(i)+".png",imBox2[i].reshape((28,28)))
##    res = input("What recogn do you want to save?[1,2,3,4]")
##    if(res == "4"):
##        for i in range(len(imBox)):
##            cv2.imwrite("./database/"+str(recogn3[i/9][i%9])+"dd"+str(i)+".png",imBox3[i].reshape((28,28)))
##else:
##    pass


