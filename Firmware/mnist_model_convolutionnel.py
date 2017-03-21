from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import time
from datetime import timedelta
import math
from processing import *
#from database import *

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
    
    layerShape = layer.get_shape()
    numFeatures = layerShape[1:4].num_elements()
    flattenedLayer = tf.reshape(layer,[-1,numFeatures])
    return flattenedLayer,numFeatures

def FullyConnectLayer(inputs,numOfinput,numOfOutput,useRelu=True):
    
    weights = CreateNewWeights(shape = [numOfinput,numOfOutput])
    biases = CreateNewBiases(length = numOfOutput)

    layer = tf.matmul(inputs,weights)+biases
    if(useRelu):
        layer = tf.nn.relu(layer)
    return layer

def optimizefor(num_of_iteration):
    avg_cost = 0
    for i in range(num_of_iteration):
        x_batch,y_batch = data.train.next_batch(batch_size)
        feed_dict_train = {x:x_batch, y_true:y_batch}
        session.run(optimizer,feed_dict=feed_dict_train)
        avg_cost += session.run(cost_function,feed_dict=feed_dict_train)/num_of_iteration
    return avg_cost

def print_accuracy(data,session):
    feed_dict = {x:data.images, y:data.labels, y_cls:data.cls}
    acc = session.run(accuracy,feed_dict=feed_dict)
    print("Accuracy:{0:.1%}".format(acc))

# Counter for total number of iterations performed so far.
total_iterations = 0

def optimize(num_iterations):
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

data = input_data.read_data_sets("C:/Users/kevin/Documents/Sudoku-robot/Firmware/tensor/",one_hot=True)
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

init = tf.global_variables_initializer()
saver = tf.train.Saver()
session = tf.Session()
session.run(init)
#optimize(4000)
saver.restore(session,"C:/Users/kevin/Documents/Sudoku-robot/Firmware/tensor/tensor_v1")
feed_dict = {x:(255-imBox)/255}
feed_dict1 = {x:(255-imBox1)/255}
feed_dict2 = {x:(255-imBox2)/255}
feed_dict3 = {x:(255-imBox3)/255}
recogn = session.run(y_pred_cls,feed_dict).reshape((9,9))
recogn1 = session.run(y_pred_cls,feed_dict1).reshape((9,9))
recogn2 = session.run(y_pred_cls,feed_dict2).reshape((9,9))
recogn3 = session.run(y_pred_cls,feed_dict3).reshape((9,9))
#recogn = np.ceil((recogn+recogn1)/2)
#recogn = recogn.astype(int)
#path = saver.save(session,"/tmp/tensor/tensor_v1")
#print("model path is: %s" % path)

##tf.add_to_collection("accuracy",accuracy)
##tf.add_to_collection("y_pred_cls",y_pred_cls)
##tf.add_to_collection("predictions",predictions)
##tf.add_to_collection("connectedLayer1",connectedLayer1)
##tf.add_to_collection("connectedLayer2",connectedLayer2)

##for iteration in range(training_iteration):
##    total_batch = int(mnist.train.num_examples/batch_size)
##    avg_cost = optimizefor(total_batch)
##    acc = session.run(accuracy)
##    if iteration % display_step == 0:
##        print("Iteration:",'%04d' % (iteration +1), "cost=", "{:.9f}".format(avg_cost))    
##
##print_accuracy(mnist.test,session)

cv2.imshow('nk',img)





