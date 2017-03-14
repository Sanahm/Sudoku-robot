import numpy as np
import cv2
import os
from prepross import *
import random as rd
path = 'C:/Users/Mohamed/Documents/2ASicom/Sudoku-robot/Ressources/database/'
class base(object):
  def __init__(self,train,test,validation = 0):
    self.train = train
    self.test = test
    self.validation = validation
    

class DataSet(object):

  def __init__(self,
               images,
               labels):
    """Construct a DataSet.
    one_hot arg is used only if fake_data is true.  `dtype` can be either
    `uint8` to leave the input as `[0, 255]`, or `float32` to rescale into
    `[0, 1]`.
    """
    assert len(labels) == len(images)
    self._num_examples = len(images)
    self._images = images
    self._labels = labels
    self._epochs_completed = 0
    self._index_in_epoch = 0

  @property
  def images(self):
    return self._images

  @property
  def labels(self):
    return self._labels

  @property
  def num_examples(self):
    return self._num_examples

  @property
  def epochs_completed(self):
    return self._epochs_completed

  def next_batch(self, batch_size):
    """Return the next `batch_size` examples from this data set."""
    start = self._index_in_epoch
    self._index_in_epoch += batch_size
    if self._index_in_epoch > self._num_examples:
      # Finished epoch
      self._epochs_completed += 1
      # Shuffle the data
      perm = np.arange(self._num_examples)
      np.random.shuffle(perm)
      self._images = self._images[perm]
      self._labels = self._labels[perm]
      # Start next epoch
      start = 0
      self._index_in_epoch = batch_size
      assert batch_size <= self._num_examples
    end = self._index_in_epoch
    return self._images[start:end], self._labels[start:end]

def to_one_hot(labels, num_classes):
  """Convert class labels from scalars to one-hot vectors."""
  num_labels = labels.shape[0]
  index_offset = np.arange(num_labels) * num_classes
  labels_one_hot = np.zeros((num_labels, num_classes))
  labels_one_hot.flat[index_offset + labels.ravel()] = 1
  return labels_one_hot


images = []
labels = []
eps = 0.1*255
for file in os.listdir(path):
    label = [int(s) for s in list(file) if s.isdigit()][0]
    labels.append(label)
    image = 255 - cv2.cvtColor(cv2.imread(path+file),cv2.COLOR_BGR2GRAY) #inverser l'image
    ret,image = binarize(image,cv2.THRESH_OTSU)
    images.append(np.reshape(image/255,image.shape[0]*image.shape[1])) #puis convertir [0,255] ->[0,1]

num_classes = 10 #chiffres de 0 à 9              
labels = to_one_hot(np.array(labels),num_classes)
images = np.array(images)
test = DataSet(images,labels)

path = 'C:/Users/Mohamed/Documents/2ASicom/Sudoku-robot/Ressources/data/'
images = []
labels = []
image_label = []
tab = np.zeros(10)
for file in os.listdir(path):
    label = [int(s) for s in list(file) if s.isdigit()][0]
    tab[label] +=1
    #labels.append(label)
    image = 255 - cv2.cvtColor(cv2.imread(path+file),cv2.COLOR_BGR2GRAY) #inverser l'image
    #ret,image = binarize(image,cv2.THRESH_OTSU)
    #images.append(np.reshape(image/255,image.shape[0]*image.shape[1])) #puis convertir [0,255] ->[0,1]
    image_label.append((image,label))

num_classes = 10 #chiffres de 0 à 9
rd.shuffle(image_label)
for i in range(len(image_label)):
    images.append(np.reshape(image_label[i][0]/255,image_label[i][0].shape[0]*image_label[i][0].shape[1]))
    labels.append(image_label[i][1])
labels = to_one_hot(np.array(labels),num_classes)
images = np.array(images)

train = DataSet(images,labels)
data = base(train,test)
