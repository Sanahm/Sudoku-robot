Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Optimization Iteration:      1, Training Accuracy:  23.3%
Optimization Iteration:    101, Training Accuracy:  33.3%
Optimization Iteration:    201, Training Accuracy:   6.7%
Optimization Iteration:    301, Training Accuracy:  13.3%
Optimization Iteration:    401, Training Accuracy:  10.0%
Optimization Iteration:    501, Training Accuracy:  13.3%
Optimization Iteration:    601, Training Accuracy:  16.7%
Optimization Iteration:    701, Training Accuracy:  10.0%
Optimization Iteration:    801, Training Accuracy:   6.7%
Optimization Iteration:    901, Training Accuracy:   6.7%
Optimization Iteration:   1001, Training Accuracy:  10.0%
Optimization Iteration:   1101, Training Accuracy:  16.7%
Optimization Iteration:   1201, Training Accuracy:  16.7%
Optimization Iteration:   1301, Training Accuracy:  13.3%
Traceback (most recent call last):
  File "C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py", line 277, in <module>
    optimize(4000)
  File "C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py", line 104, in optimize
    session.run(optimizer, feed_dict=feed_dict_train)
  File "C:\python35\lib\site-packages\tensorflow\python\client\session.py", line 766, in run
    run_metadata_ptr)
  File "C:\python35\lib\site-packages\tensorflow\python\client\session.py", line 964, in _run
    feed_dict_string, options, run_metadata)
  File "C:\python35\lib\site-packages\tensorflow\python\client\session.py", line 1014, in _do_run
    target_list, options, run_metadata)
  File "C:\python35\lib\site-packages\tensorflow\python\client\session.py", line 1021, in _do_call
    return fn(*args)
  File "C:\python35\lib\site-packages\tensorflow\python\client\session.py", line 1003, in _run_fn
    status, run_metadata)
KeyboardInterrupt
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Optimization Iteration:      1, Training Accuracy:  21.4%
Optimization Iteration:    101, Training Accuracy:  42.9%
Optimization Iteration:    201, Training Accuracy:  90.5%
Optimization Iteration:    301, Training Accuracy:  97.6%
Optimization Iteration:    401, Training Accuracy: 100.0%
Optimization Iteration:    501, Training Accuracy: 100.0%
Optimization Iteration:    601, Training Accuracy: 100.0%
Optimization Iteration:    701, Training Accuracy: 100.0%
Optimization Iteration:    801, Training Accuracy: 100.0%
Optimization Iteration:    901, Training Accuracy: 100.0%
Optimization Iteration:   1001, Training Accuracy: 100.0%
Optimization Iteration:   1101, Training Accuracy: 100.0%
Optimization Iteration:   1201, Training Accuracy: 100.0%
Optimization Iteration:   1301, Training Accuracy: 100.0%
Optimization Iteration:   1401, Training Accuracy: 100.0%
Optimization Iteration:   1501, Training Accuracy: 100.0%
Optimization Iteration:   1601, Training Accuracy: 100.0%
Optimization Iteration:   1701, Training Accuracy: 100.0%
Optimization Iteration:   1801, Training Accuracy: 100.0%
Optimization Iteration:   1901, Training Accuracy: 100.0%
Optimization Iteration:   2001, Training Accuracy: 100.0%
Optimization Iteration:   2101, Training Accuracy: 100.0%
Optimization Iteration:   2201, Training Accuracy: 100.0%
Optimization Iteration:   2301, Training Accuracy: 100.0%
Optimization Iteration:   2401, Training Accuracy: 100.0%
Optimization Iteration:   2501, Training Accuracy: 100.0%
Optimization Iteration:   2601, Training Accuracy: 100.0%
Optimization Iteration:   2701, Training Accuracy: 100.0%
Optimization Iteration:   2801, Training Accuracy: 100.0%
Optimization Iteration:   2901, Training Accuracy: 100.0%
Optimization Iteration:   3001, Training Accuracy: 100.0%
Optimization Iteration:   3101, Training Accuracy: 100.0%
Optimization Iteration:   3201, Training Accuracy: 100.0%
Optimization Iteration:   3301, Training Accuracy: 100.0%
Optimization Iteration:   3401, Training Accuracy: 100.0%
Optimization Iteration:   3501, Training Accuracy: 100.0%
Optimization Iteration:   3601, Training Accuracy: 100.0%
Optimization Iteration:   3701, Training Accuracy: 100.0%
Optimization Iteration:   3801, Training Accuracy: 100.0%
Optimization Iteration:   3901, Training Accuracy: 100.0%
Time usage: 1:07:38
>>> recogn
array([[5, 3, 0, 0, 7, 0, 0, 0, 0],
       [6, 0, 0, 1, 9, 5, 0, 0, 0],
       [0, 9, 8, 0, 0, 0, 0, 6, 0],
       [8, 0, 0, 0, 6, 0, 0, 0, 3],
       [4, 0, 0, 8, 0, 3, 0, 0, 1],
       [7, 0, 0, 0, 2, 0, 0, 0, 6],
       [0, 6, 0, 0, 0, 0, 2, 8, 0],
       [0, 0, 0, 4, 1, 9, 0, 0, 5],
       [0, 0, 0, 0, 8, 0, 0, 7, 9]], dtype=int64)
>>> cv2.imshow('n',img)
>>> print_test_accuracy()
Accuracy on Test-Set: 93.9% (124 / 132)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Traceback (most recent call last):
  File "C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py", line 204, in <module>
    data.test.cls = np.array([label.argmax() for label in data.test.labels])
NameError: name 'data' is not defined
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Extracting /tmp/tensorflow\train-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\train-labels-idx1-ubyte.gz
Extracting /tmp/tensorflow\t10k-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\t10k-labels-idx1-ubyte.gz
>>> cv2.imshow('n',img)
>>> recogn
array([[0, 0, 0, 0, 4, 0, 0, 0, 0],
       [0, 0, 2, 6, 0, 7, 1, 0, 0],
       [8, 7, 1, 0, 0, 0, 6, 9, 4],
       [0, 6, 0, 0, 0, 0, 0, 4, 0],
       [2, 0, 5, 9, 9, 6, 7, 0, 8],
       [0, 8, 0, 0, 0, 0, 0, 2, 0],
       [6, 5, 8, 0, 0, 0, 4, 7, 1],
       [0, 0, 9, 4, 0, 8, 5, 0, 0],
       [0, 0, 0, 0, 7, 0, 0, 0, 0]], dtype=int64)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Extracting /tmp/tensorflow\train-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\train-labels-idx1-ubyte.gz
Extracting /tmp/tensorflow\t10k-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\t10k-labels-idx1-ubyte.gz
>>> cv2.imshow('n',img)
>>> recogn
array([[0, 0, 6, 0, 5, 4, 9, 0, 0],
       [1, 0, 0, 0, 6, 0, 0, 4, 2],
       [7, 0, 0, 0, 8, 9, 0, 0, 0],
       [0, 7, 0, 0, 0, 5, 0, 8, 1],
       [0, 5, 0, 8, 4, 0, 6, 0, 0],
       [4, 0, 2, 0, 0, 0, 0, 0, 0],
       [0, 3, 4, 0, 0, 0, 1, 0, 0],
       [9, 0, 0, 8, 0, 0, 0, 5, 0],
       [0, 0, 0, 4, 0, 0, 3, 0, 7]], dtype=int64)
>>> recogn1
array([[0, 0, 6, 0, 5, 4, 9, 0, 0],
       [1, 0, 0, 0, 6, 0, 0, 4, 2],
       [7, 0, 0, 0, 8, 9, 0, 0, 0],
       [0, 7, 0, 0, 0, 5, 0, 8, 1],
       [0, 5, 0, 8, 4, 0, 6, 0, 0],
       [4, 0, 2, 0, 0, 0, 0, 0, 0],
       [0, 3, 4, 0, 0, 0, 1, 0, 0],
       [9, 0, 0, 8, 0, 0, 0, 5, 0],
       [0, 0, 0, 4, 0, 0, 3, 0, 7]], dtype=int64)
>>> recogn2
array([[0, 0, 6, 0, 5, 4, 9, 0, 0],
       [1, 0, 0, 0, 6, 0, 0, 4, 2],
       [7, 0, 0, 0, 8, 9, 0, 0, 0],
       [0, 7, 0, 0, 0, 5, 0, 8, 1],
       [0, 5, 0, 8, 4, 0, 6, 0, 0],
       [4, 0, 2, 0, 0, 0, 0, 0, 0],
       [0, 3, 4, 0, 0, 0, 1, 0, 0],
       [9, 0, 0, 8, 0, 0, 0, 5, 0],
       [0, 0, 0, 4, 0, 0, 3, 0, 7]], dtype=int64)
>>> recogn3
array([[0, 0, 6, 0, 5, 4, 9, 0, 0],
       [1, 0, 0, 0, 6, 0, 0, 4, 2],
       [7, 0, 0, 0, 8, 9, 0, 0, 0],
       [0, 7, 0, 0, 0, 5, 0, 8, 1],
       [0, 5, 0, 8, 4, 0, 6, 0, 0],
       [4, 0, 2, 0, 0, 0, 0, 0, 0],
       [0, 3, 4, 0, 0, 0, 1, 0, 0],
       [9, 0, 0, 8, 0, 0, 0, 5, 0],
       [0, 0, 0, 4, 0, 0, 8, 0, 7]], dtype=int64)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Extracting /tmp/tensorflow\train-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\train-labels-idx1-ubyte.gz
Extracting /tmp/tensorflow\t10k-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\t10k-labels-idx1-ubyte.gz
>>> cv2.imshow('n',img)
>>> recogn1
array([[4, 0, 0, 0, 3, 0, 0, 0, 5],
       [0, 0, 0, 9, 0, 2, 0, 0, 0],
       [0, 0, 6, 0, 7, 0, 3, 0, 0],
       [0, 5, 0, 3, 0, 4, 0, 3, 0],
       [3, 0, 8, 0, 0, 0, 6, 0, 4],
       [0, 9, 0, 7, 0, 3, 0, 8, 0],
       [0, 0, 5, 0, 4, 0, 3, 0, 0],
       [0, 0, 0, 3, 0, 9, 0, 0, 0],
       [2, 0, 0, 0, 3, 0, 0, 0, 8]], dtype=int64)
>>> recogn
array([[4, 0, 0, 0, 3, 0, 0, 0, 5],
       [0, 0, 0, 9, 0, 2, 0, 0, 0],
       [0, 0, 6, 0, 7, 0, 3, 0, 0],
       [0, 5, 0, 3, 0, 4, 0, 3, 0],
       [3, 0, 8, 0, 0, 0, 6, 0, 4],
       [0, 9, 0, 7, 0, 3, 0, 8, 0],
       [0, 0, 5, 0, 4, 0, 3, 0, 0],
       [0, 0, 0, 3, 0, 9, 0, 0, 0],
       [2, 0, 0, 0, 3, 0, 0, 0, 8]], dtype=int64)
>>> recogn3
array([[4, 0, 0, 0, 3, 0, 0, 0, 5],
       [0, 0, 0, 9, 0, 2, 0, 0, 0],
       [0, 0, 6, 0, 7, 0, 3, 0, 0],
       [0, 5, 0, 3, 0, 4, 0, 3, 0],
       [3, 0, 8, 0, 0, 0, 6, 0, 4],
       [0, 9, 0, 7, 0, 3, 0, 8, 0],
       [0, 0, 5, 0, 4, 0, 3, 0, 0],
       [0, 0, 0, 3, 0, 9, 0, 0, 0],
       [2, 0, 0, 0, 3, 0, 0, 0, 8]], dtype=int64)
>>> recogn2
array([[4, 0, 0, 0, 3, 0, 0, 0, 5],
       [0, 0, 0, 9, 0, 2, 0, 0, 0],
       [0, 0, 6, 0, 7, 0, 3, 0, 0],
       [0, 5, 0, 3, 0, 4, 0, 3, 0],
       [3, 0, 8, 0, 0, 0, 6, 0, 4],
       [0, 9, 0, 7, 0, 3, 0, 8, 0],
       [0, 0, 5, 0, 4, 0, 3, 0, 0],
       [0, 0, 0, 3, 0, 9, 0, 0, 0],
       [2, 0, 0, 0, 3, 0, 0, 0, 8]], dtype=int64)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Extracting /tmp/tensorflow\train-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\train-labels-idx1-ubyte.gz
Extracting /tmp/tensorflow\t10k-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\t10k-labels-idx1-ubyte.gz
>>> cv2.imshow('n',img)
>>> recogn
array([[4, 0, 0, 0, 0, 0, 0, 0, 9],
       [0, 0, 0, 5, 0, 8, 0, 0, 0],
       [7, 9, 0, 3, 0, 2, 0, 8, 1],
       [0, 5, 0, 6, 0, 9, 0, 4, 0],
       [0, 0, 4, 0, 3, 0, 1, 0, 0],
       [0, 2, 0, 1, 0, 4, 0, 5, 0],
       [6, 8, 0, 4, 0, 3, 0, 7, 5],
       [0, 0, 0, 9, 0, 6, 0, 0, 0],
       [9, 0, 0, 0, 0, 0, 0, 0, 3]], dtype=int64)
>>> recogn1
array([[4, 0, 0, 0, 0, 0, 0, 0, 9],
       [0, 0, 0, 5, 0, 8, 0, 0, 0],
       [7, 9, 0, 3, 0, 2, 0, 8, 1],
       [0, 5, 0, 6, 0, 9, 0, 4, 0],
       [0, 0, 4, 0, 3, 0, 1, 0, 0],
       [0, 2, 0, 1, 0, 4, 0, 5, 0],
       [6, 8, 0, 4, 0, 3, 0, 7, 5],
       [0, 0, 0, 9, 0, 6, 0, 0, 0],
       [9, 0, 0, 0, 0, 0, 0, 0, 3]], dtype=int64)
>>> recogn1-recogn
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> recogn1-recogn2
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> recogn1-recogn3
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Traceback (most recent call last):
  File "C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py", line 8, in <module>
    from prepross import *
  File "C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\prepross.py", line 237, in <module>
    mat = np.array([StDev(imBox[i]) for i in range(imBox.shape[0])]).reshape((9,9))
ValueError: total size of new array must be unchanged
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Extracting /tmp/tensorflow\train-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\train-labels-idx1-ubyte.gz
Extracting /tmp/tensorflow\t10k-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\t10k-labels-idx1-ubyte.gz
>>> recogn
array([[0, 0, 1, 9, 0, 0, 1, 0, 7],
       [0, 0, 4, 8, 1, 0, 1, 0, 0],
       [1, 1, 0, 0, 1, 7, 1, 0, 4],
       [4, 1, 4, 4, 0, 4, 7, 1, 0],
       [7, 0, 0, 0, 0, 1, 5, 1, 4],
       [6, 0, 4, 0, 0, 4, 0, 4, 7],
       [1, 4, 0, 1, 1, 0, 4, 6, 1],
       [0, 0, 1, 0, 0, 4, 4, 7, 0],
       [0, 4, 7, 7, 1, 0, 0, 4, 1]], dtype=int64)
>>> cv2.imshow('n',img)
>>> recogn2
array([[0, 0, 1, 9, 0, 0, 1, 0, 7],
       [0, 0, 4, 8, 1, 0, 1, 0, 0],
       [1, 1, 0, 0, 1, 7, 1, 0, 4],
       [4, 1, 4, 4, 0, 4, 7, 1, 0],
       [7, 0, 0, 0, 0, 1, 5, 1, 4],
       [6, 0, 4, 0, 0, 1, 0, 4, 7],
       [1, 4, 0, 1, 1, 0, 4, 6, 1],
       [0, 0, 1, 0, 0, 4, 4, 7, 0],
       [0, 4, 7, 7, 1, 0, 0, 4, 1]], dtype=int64)
>>> recogn3
array([[0, 0, 1, 9, 0, 0, 1, 0, 7],
       [0, 0, 4, 8, 1, 0, 1, 0, 0],
       [1, 1, 0, 0, 1, 7, 1, 0, 4],
       [4, 1, 4, 4, 0, 4, 7, 1, 0],
       [7, 0, 0, 0, 0, 1, 5, 1, 4],
       [6, 0, 4, 0, 0, 4, 0, 4, 7],
       [1, 4, 0, 1, 1, 0, 4, 6, 1],
       [0, 0, 1, 0, 0, 4, 4, 7, 0],
       [0, 4, 7, 7, 1, 0, 0, 4, 1]], dtype=int64)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Extracting /tmp/tensorflow\train-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\train-labels-idx1-ubyte.gz
Extracting /tmp/tensorflow\t10k-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\t10k-labels-idx1-ubyte.gz
>>> recogn
array([[0, 0, 1, 9, 0, 0, 1, 0, 7],
       [0, 0, 4, 8, 1, 0, 1, 0, 0],
       [1, 1, 0, 0, 1, 7, 1, 0, 4],
       [4, 1, 4, 4, 0, 4, 7, 1, 0],
       [7, 0, 0, 0, 0, 1, 5, 1, 4],
       [6, 0, 4, 0, 0, 4, 0, 4, 7],
       [1, 4, 0, 1, 1, 0, 4, 6, 1],
       [0, 0, 1, 0, 0, 4, 4, 7, 0],
       [0, 4, 7, 7, 1, 0, 0, 4, 1]], dtype=int64)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Extracting /tmp/tensorflow\train-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\train-labels-idx1-ubyte.gz
Extracting /tmp/tensorflow\t10k-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\t10k-labels-idx1-ubyte.gz
>>> cv2.imshow('n',img)
>>> recogn
array([[8, 1, 9, 0, 6, 0, 0, 2, 7],
       [7, 2, 0, 8, 0, 5, 0, 0, 6],
       [0, 0, 0, 7, 0, 1, 9, 0, 9],
       [0, 0, 5, 0, 3, 0, 2, 0, 0],
       [4, 0, 0, 0, 0, 0, 5, 0, 8],
       [0, 0, 7, 9, 9, 0, 1, 0, 9],
       [0, 0, 0, 3, 0, 6, 0, 0, 0],
       [3, 7, 0, 4, 0, 9, 0, 8, 1],
       [6, 4, 9, 0, 0, 0, 0, 5, 9]], dtype=int64)
>>> recogn1
array([[8, 1, 9, 0, 6, 0, 0, 2, 7],
       [7, 2, 0, 8, 0, 5, 0, 0, 5],
       [0, 0, 0, 7, 0, 1, 9, 0, 9],
       [0, 0, 5, 0, 3, 0, 2, 0, 0],
       [4, 0, 0, 0, 0, 0, 5, 0, 8],
       [0, 0, 7, 9, 9, 0, 1, 0, 9],
       [0, 0, 0, 3, 0, 6, 0, 0, 0],
       [3, 7, 0, 4, 0, 9, 0, 8, 1],
       [6, 4, 9, 0, 0, 0, 0, 5, 9]], dtype=int64)
>>> recogn2
array([[8, 1, 9, 0, 6, 0, 0, 2, 7],
       [7, 2, 0, 8, 0, 5, 0, 0, 6],
       [0, 0, 0, 7, 0, 1, 9, 0, 9],
       [0, 0, 5, 0, 3, 0, 2, 0, 0],
       [4, 0, 0, 0, 0, 0, 5, 0, 8],
       [0, 0, 7, 9, 9, 0, 1, 0, 9],
       [0, 0, 0, 3, 0, 6, 0, 0, 0],
       [3, 7, 0, 4, 0, 9, 0, 8, 1],
       [6, 4, 9, 0, 0, 0, 0, 5, 9]], dtype=int64)
>>> recogn3
array([[8, 1, 9, 0, 6, 0, 0, 2, 7],
       [7, 2, 0, 8, 0, 5, 0, 0, 6],
       [0, 0, 0, 7, 0, 1, 9, 0, 9],
       [0, 0, 6, 0, 3, 0, 2, 0, 0],
       [4, 0, 0, 0, 0, 0, 5, 0, 8],
       [0, 0, 7, 9, 9, 0, 1, 0, 9],
       [0, 0, 0, 3, 0, 6, 0, 0, 0],
       [3, 7, 0, 4, 0, 9, 0, 8, 1],
       [6, 4, 9, 0, 0, 0, 0, 5, 9]], dtype=int64)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Extracting /tmp/tensorflow\train-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\train-labels-idx1-ubyte.gz
Extracting /tmp/tensorflow\t10k-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\t10k-labels-idx1-ubyte.gz
>>> recogn
array([[8, 1, 9, 0, 6, 0, 0, 2, 7],
       [7, 2, 0, 8, 0, 5, 0, 1, 6],
       [0, 0, 0, 7, 9, 1, 9, 0, 9],
       [0, 3, 5, 0, 3, 0, 2, 0, 0],
       [4, 0, 1, 0, 0, 0, 5, 0, 8],
       [0, 0, 7, 9, 9, 0, 1, 9, 9],
       [0, 0, 9, 3, 0, 6, 0, 0, 0],
       [3, 7, 0, 4, 0, 9, 0, 8, 1],
       [6, 4, 9, 0, 1, 0, 0, 5, 9]], dtype=int64)
>>> cv2.imshow('kjn',img)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Extracting /tmp/tensorflow\train-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\train-labels-idx1-ubyte.gz
Extracting /tmp/tensorflow\t10k-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\t10k-labels-idx1-ubyte.gz
>>> recogn
array([[8, 1, 9, 4, 6, 9, 8, 2, 7],
       [7, 2, 9, 8, 0, 5, 0, 1, 6],
       [4, 6, 9, 7, 9, 1, 9, 3, 9],
       [9, 3, 5, 9, 3, 9, 2, 0, 9],
       [4, 4, 1, 9, 0, 9, 5, 9, 8],
       [0, 0, 7, 9, 9, 9, 1, 9, 9],
       [9, 2, 9, 3, 9, 6, 9, 0, 8],
       [3, 7, 9, 4, 4, 9, 0, 8, 1],
       [6, 4, 9, 0, 1, 9, 0, 5, 9]], dtype=int64)
>>> cv2.imshow('kjn',img)
>>> recogn2
array([[8, 1, 9, 0, 6, 0, 0, 2, 7],
       [7, 2, 0, 8, 0, 5, 0, 1, 6],
       [0, 0, 0, 7, 9, 1, 9, 0, 9],
       [0, 3, 5, 0, 3, 0, 2, 0, 0],
       [4, 0, 1, 0, 0, 0, 5, 0, 8],
       [0, 0, 7, 9, 9, 0, 1, 9, 9],
       [0, 0, 9, 3, 0, 6, 0, 0, 0],
       [3, 7, 0, 4, 0, 9, 0, 8, 1],
       [6, 4, 9, 0, 1, 0, 0, 5, 9]], dtype=int64)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Extracting /tmp/tensorflow\train-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\train-labels-idx1-ubyte.gz
Extracting /tmp/tensorflow\t10k-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\t10k-labels-idx1-ubyte.gz
>>> recogn
array([[8, 1, 0, 0, 6, 0, 0, 2, 7],
       [7, 2, 0, 8, 0, 5, 0, 1, 6],
       [0, 0, 0, 7, 0, 1, 0, 0, 0],
       [0, 0, 6, 0, 3, 0, 2, 0, 0],
       [4, 0, 1, 0, 0, 0, 5, 0, 8],
       [0, 0, 7, 0, 9, 0, 1, 0, 0],
       [0, 0, 0, 3, 0, 6, 0, 0, 0],
       [3, 7, 0, 4, 0, 9, 0, 8, 1],
       [6, 4, 0, 0, 1, 0, 0, 5, 9]], dtype=int64)
>>> cv2.imshow('kjn',img)
>>> recogn1-recogn
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> recogn1-recogn2
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> recogn3
array([[8, 1, 0, 0, 6, 0, 0, 2, 7],
       [7, 2, 0, 8, 0, 5, 0, 1, 6],
       [0, 0, 0, 7, 0, 1, 0, 0, 0],
       [0, 0, 6, 0, 3, 0, 2, 0, 0],
       [4, 0, 1, 0, 0, 0, 5, 0, 8],
       [0, 0, 7, 0, 9, 0, 1, 0, 0],
       [0, 0, 0, 3, 0, 6, 0, 0, 0],
       [3, 7, 0, 4, 0, 9, 0, 8, 1],
       [6, 4, 0, 0, 1, 0, 0, 5, 9]], dtype=int64)
>>> recogn1-recogn3
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Extracting /tmp/tensorflow\train-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\train-labels-idx1-ubyte.gz
Extracting /tmp/tensorflow\t10k-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\t10k-labels-idx1-ubyte.gz
>>> cv2.imshow('kjn',img)
>>> recogn
array([[1, 7, 8, 6, 0, 4, 5, 0, 9],
       [0, 9, 6, 8, 2, 0, 3, 1, 4],
       [3, 2, 0, 1, 5, 9, 8, 0, 6],
       [2, 4, 9, 3, 0, 6, 9, 9, 0],
       [9, 0, 7, 0, 4, 8, 6, 5, 3],
       [6, 0, 3, 7, 0, 5, 1, 4, 2],
       [8, 3, 0, 5, 7, 0, 4, 6, 1],
       [7, 7, 1, 0, 6, 3, 2, 9, 0],
       [0, 6, 2, 9, 8, 1, 0, 3, 5]], dtype=int64)
>>> recogn1
array([[1, 7, 8, 6, 0, 4, 5, 0, 9],
       [0, 9, 6, 8, 2, 0, 3, 1, 4],
       [3, 2, 0, 1, 5, 9, 8, 0, 6],
       [2, 4, 9, 3, 0, 9, 9, 9, 0],
       [9, 0, 7, 0, 4, 8, 6, 5, 3],
       [6, 0, 3, 7, 0, 5, 1, 4, 2],
       [8, 3, 0, 5, 7, 0, 4, 6, 1],
       [7, 5, 1, 0, 6, 3, 2, 9, 0],
       [0, 6, 2, 9, 8, 1, 0, 3, 5]], dtype=int64)
>>> recogn2
array([[1, 7, 8, 6, 0, 4, 5, 0, 9],
       [0, 9, 6, 8, 2, 0, 3, 1, 4],
       [3, 2, 0, 1, 5, 9, 8, 0, 6],
       [2, 4, 9, 3, 0, 6, 9, 9, 0],
       [9, 0, 7, 0, 4, 8, 6, 5, 3],
       [6, 0, 3, 7, 0, 5, 1, 4, 2],
       [8, 3, 0, 5, 7, 0, 4, 6, 1],
       [7, 5, 1, 0, 6, 3, 2, 9, 0],
       [0, 6, 2, 9, 8, 1, 0, 3, 5]], dtype=int64)
>>> recogn3
array([[1, 7, 8, 6, 0, 4, 5, 0, 9],
       [0, 9, 6, 8, 2, 0, 3, 1, 4],
       [3, 2, 0, 1, 5, 9, 8, 0, 6],
       [2, 4, 9, 3, 0, 6, 9, 9, 0],
       [9, 0, 7, 0, 4, 8, 6, 5, 3],
       [6, 0, 3, 7, 0, 5, 1, 4, 2],
       [8, 3, 0, 5, 7, 0, 4, 6, 1],
       [7, 7, 1, 0, 6, 3, 2, 9, 0],
       [0, 6, 2, 9, 8, 1, 0, 3, 5]], dtype=int64)
>>> cv2.imshow('jh',imBox[29].reshape((28,28)))
>>> cv2.imshow('jh',imBox[32].reshape((28,28)))
>>> cv2.imshow('jh',imBox[33].reshape((28,28)))
>>> cv2.imshow('jh',imBox[34].reshape((28,28)))
>>> plt.imshow('jh',imBox[34].reshape((28,28)))
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    plt.imshow('jh',imBox[34].reshape((28,28)))
  File "C:\python35\lib\site-packages\matplotlib\pyplot.py", line 3029, in imshow
    **kwargs)
  File "C:\python35\lib\site-packages\matplotlib\__init__.py", line 1819, in inner
    return func(ax, *args, **kwargs)
  File "C:\python35\lib\site-packages\matplotlib\axes\_axes.py", line 4920, in imshow
    resample=resample, **kwargs)
  File "C:\python35\lib\site-packages\matplotlib\image.py", line 597, in __init__
    **kwargs
  File "C:\python35\lib\site-packages\matplotlib\image.py", line 109, in __init__
    cm.ScalarMappable.__init__(self, norm, cmap)
  File "C:\python35\lib\site-packages\matplotlib\cm.py", line 201, in __init__
    self.cmap = get_cmap(cmap)
  File "C:\python35\lib\site-packages\matplotlib\cm.py", line 158, in get_cmap
    if name in cmap_d:
TypeError: unhashable type: 'numpy.ndarray'
>>> plt.imshow(imBox[34].reshape((28,28)))
<matplotlib.image.AxesImage object at 0x000000088388D048>
>>> plt.show()
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Traceback (most recent call last):
  File "C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py", line 8, in <module>
    from prepross import *
  File "C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\prepross.py", line 237, in <module>
    mat = np.array([StDev(imBox[i]) for i in range(imBox.shape[0])]).reshape((9,9))
ValueError: total size of new array must be unchanged
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Traceback (most recent call last):
  File "C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py", line 8, in <module>
    from prepross import *
  File "C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\prepross.py", line 167, in <module>
    img = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
cv2.error: C:\projects\opencv-python\opencv\modules\imgproc\src\color.cpp:7456: error: (-215) scn == 3 || scn == 4 in function cv::ipp_cvtColor

>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Extracting /tmp/tensorflow\train-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\train-labels-idx1-ubyte.gz
Extracting /tmp/tensorflow\t10k-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\t10k-labels-idx1-ubyte.gz
>>> recogn
array([[4, 0, 0, 0, 0, 0, 0, 0, 9],
       [0, 0, 0, 5, 0, 8, 0, 0, 0],
       [7, 9, 0, 3, 0, 2, 0, 8, 1],
       [0, 5, 0, 6, 0, 9, 0, 4, 0],
       [0, 0, 4, 0, 3, 0, 1, 0, 0],
       [0, 2, 0, 1, 0, 4, 0, 5, 0],
       [6, 8, 0, 4, 0, 3, 0, 7, 5],
       [0, 0, 0, 9, 0, 6, 0, 0, 0],
       [9, 0, 0, 0, 0, 0, 0, 0, 3]], dtype=int64)
>>> cv2.imshow('nk',img)
>>> recogn1
array([[4, 0, 0, 0, 0, 0, 0, 0, 9],
       [0, 0, 0, 5, 0, 8, 0, 0, 0],
       [7, 9, 0, 3, 0, 2, 0, 8, 1],
       [0, 5, 0, 6, 0, 9, 0, 4, 0],
       [0, 0, 4, 0, 3, 0, 1, 0, 0],
       [0, 2, 0, 1, 0, 4, 0, 5, 0],
       [6, 8, 0, 4, 0, 3, 0, 7, 5],
       [0, 0, 0, 9, 0, 6, 0, 0, 0],
       [9, 0, 0, 0, 0, 0, 0, 0, 3]], dtype=int64)
>>> recogn1-recogn
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> recogn1-recogn2
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> recogn1-recogn3
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Extracting /tmp/tensorflow\train-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\train-labels-idx1-ubyte.gz
Extracting /tmp/tensorflow\t10k-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\t10k-labels-idx1-ubyte.gz
>>> recogn
array([[4, 0, 0, 0, 1, 0, 0, 0, 5],
       [0, 0, 0, 9, 0, 2, 0, 0, 0],
       [0, 0, 6, 0, 7, 0, 3, 0, 0],
       [0, 5, 0, 3, 0, 4, 0, 1, 0],
       [1, 0, 8, 0, 0, 0, 6, 0, 4],
       [0, 9, 0, 7, 0, 1, 0, 8, 0],
       [0, 0, 5, 0, 4, 0, 1, 0, 0],
       [0, 0, 0, 1, 0, 9, 0, 0, 0],
       [2, 0, 0, 0, 3, 0, 0, 0, 8]], dtype=int64)
>>> cv2.imshow('nk',img)
>>> recogn1-recogn
array([[ 0,  0,  0,  0,  0,  0,  0,  0,  0],
       [ 0,  0,  0,  0,  0,  0,  0,  0,  0],
       [ 0,  0,  0,  0,  0,  0,  0,  0,  0],
       [ 0,  0,  0,  0,  0,  0,  0,  0,  0],
       [ 0,  0, -2,  0,  0,  0,  0,  0,  0],
       [ 0,  0,  0,  0,  0,  0,  0, -2,  0],
       [ 0,  0,  0,  0,  0,  0,  0,  0,  0],
       [ 0,  0,  0,  0,  0,  0,  0,  0,  0],
       [ 0,  0,  0,  0,  0,  0,  0,  0, -2]], dtype=int64)
>>> recogn1
array([[4, 0, 0, 0, 1, 0, 0, 0, 5],
       [0, 0, 0, 9, 0, 2, 0, 0, 0],
       [0, 0, 6, 0, 7, 0, 3, 0, 0],
       [0, 5, 0, 3, 0, 4, 0, 1, 0],
       [1, 0, 6, 0, 0, 0, 6, 0, 4],
       [0, 9, 0, 7, 0, 1, 0, 6, 0],
       [0, 0, 5, 0, 4, 0, 1, 0, 0],
       [0, 0, 0, 1, 0, 9, 0, 0, 0],
       [2, 0, 0, 0, 3, 0, 0, 0, 6]], dtype=int64)
>>> recogn2
array([[4, 0, 0, 0, 1, 0, 0, 0, 5],
       [0, 0, 0, 9, 0, 2, 0, 0, 0],
       [0, 0, 6, 0, 7, 0, 3, 0, 0],
       [0, 5, 0, 3, 0, 4, 0, 1, 0],
       [1, 0, 6, 0, 0, 0, 6, 0, 4],
       [0, 9, 0, 7, 0, 1, 0, 6, 0],
       [0, 0, 5, 0, 4, 0, 1, 0, 0],
       [0, 0, 0, 1, 0, 9, 0, 0, 0],
       [2, 0, 0, 0, 3, 0, 0, 0, 6]], dtype=int64)
>>> recogn2-recogn1
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> recogn3-recogn
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> print_test_accuracy()
Accuracy on Test-Set: 48.0% (4799 / 10000)
>>> recogn
array([[4, 0, 0, 0, 1, 0, 0, 0, 5],
       [0, 0, 0, 9, 0, 2, 0, 0, 0],
       [0, 0, 6, 0, 7, 0, 3, 0, 0],
       [0, 5, 0, 3, 0, 4, 0, 1, 0],
       [1, 0, 8, 0, 0, 0, 6, 0, 4],
       [0, 9, 0, 7, 0, 1, 0, 8, 0],
       [0, 0, 5, 0, 4, 0, 1, 0, 0],
       [0, 0, 0, 1, 0, 9, 0, 0, 0],
       [2, 0, 0, 0, 3, 0, 0, 0, 8]], dtype=int64)
>>> cv2.imshow('nk',img)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Extracting /tmp/tensorflow\train-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\train-labels-idx1-ubyte.gz
Extracting /tmp/tensorflow\t10k-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\t10k-labels-idx1-ubyte.gz
>>> recogn
array([[0, 0, 6, 0, 5, 4, 9, 0, 0],
       [1, 0, 0, 0, 6, 0, 0, 4, 2],
       [7, 0, 0, 0, 8, 9, 0, 0, 0],
       [0, 7, 0, 0, 0, 5, 0, 8, 1],
       [0, 5, 0, 3, 4, 0, 6, 0, 0],
       [4, 0, 2, 0, 0, 0, 0, 0, 0],
       [0, 3, 4, 0, 0, 0, 1, 0, 0],
       [9, 0, 0, 8, 0, 0, 0, 5, 0],
       [0, 0, 0, 4, 0, 0, 3, 0, 7]], dtype=int64)
>>> cv2.imshow('nk',img)
>>> recogn1 - recogn
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> recogn1 - recogn2
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> recogn1 - recogn3
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Extracting /tmp/tensorflow\train-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\train-labels-idx1-ubyte.gz
Extracting /tmp/tensorflow\t10k-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\t10k-labels-idx1-ubyte.gz
>>> recogn
array([[0, 0, 0, 0, 4, 0, 0, 0, 0],
       [0, 0, 2, 6, 0, 7, 1, 0, 0],
       [8, 7, 1, 0, 0, 0, 6, 9, 4],
       [0, 6, 0, 0, 0, 0, 0, 4, 0],
       [2, 0, 5, 9, 0, 6, 7, 0, 8],
       [0, 8, 0, 0, 0, 0, 0, 2, 0],
       [6, 5, 8, 0, 0, 0, 4, 7, 1],
       [0, 0, 9, 4, 0, 8, 5, 0, 0],
       [0, 0, 0, 0, 7, 0, 0, 0, 0]], dtype=int64)
>>> cv2.imshow('nk',img)
>>> recogn - recogn1
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> recogn - recogn2
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> recogn - recogn3
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Extracting /tmp/tensorflow\train-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\train-labels-idx1-ubyte.gz
Extracting /tmp/tensorflow\t10k-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\t10k-labels-idx1-ubyte.gz
>>> recogn
array([[5, 3, 0, 0, 7, 0, 0, 0, 0],
       [6, 0, 0, 1, 9, 5, 0, 0, 0],
       [0, 9, 8, 0, 0, 0, 0, 6, 0],
       [8, 0, 0, 0, 6, 0, 0, 0, 3],
       [4, 0, 0, 8, 0, 3, 0, 0, 1],
       [7, 0, 0, 0, 2, 0, 0, 0, 6],
       [0, 6, 0, 0, 0, 0, 2, 8, 0],
       [0, 0, 0, 4, 1, 9, 0, 0, 5],
       [0, 0, 0, 0, 8, 0, 0, 7, 9]], dtype=int64)
>>> cv2.imshow('nk',img)
>>> recogn1 - recogn
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> recogn1 - recogn2
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> recogn1 - recogn3
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Extracting /tmp/tensorflow\train-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\train-labels-idx1-ubyte.gz
Extracting /tmp/tensorflow\t10k-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\t10k-labels-idx1-ubyte.gz
>>> recogn
array([[5, 6, 7, 2, 0, 3, 4, 9, 0],
       [1, 8, 0, 9, 6, 4, 5, 7, 3],
       [4, 9, 3, 8, 7, 5, 1, 2, 6],
       [3, 1, 6, 4, 8, 9, 2, 5, 7],
       [0, 5, 9, 1, 2, 6, 3, 8, 4],
       [2, 4, 8, 3, 5, 0, 9, 0, 1],
       [9, 2, 4, 6, 3, 8, 7, 1, 5],
       [6, 0, 1, 5, 4, 2, 0, 3, 9],
       [8, 3, 5, 7, 0, 1, 6, 4, 2]], dtype=int64)
>>> cv2.imshow('nk',img)
>>> recogn1 - recogn
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> recogn1 - recogn2
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> recogn1 - recogn3
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Extracting /tmp/tensorflow\train-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\train-labels-idx1-ubyte.gz
Extracting /tmp/tensorflow\t10k-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\t10k-labels-idx1-ubyte.gz
>>> cv2.imshow('nk',img)
>>> recogn
array([[0, 0, 6, 0, 0, 0, 0, 0, 0],
       [0, 0, 5, 2, 0, 0, 6, 0, 3],
       [0, 0, 4, 0, 7, 8, 0, 2, 9],
       [2, 0, 9, 0, 5, 4, 3, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 3, 9, 5, 0, 7, 0, 4],
       [6, 1, 0, 3, 2, 0, 8, 0, 0],
       [4, 0, 2, 0, 0, 5, 1, 0, 0],
       [0, 0, 0, 0, 0, 0, 9, 0, 0]], dtype=int64)
>>> recogn1
array([[0, 0, 6, 0, 0, 0, 0, 0, 0],
       [0, 0, 8, 2, 0, 0, 6, 0, 3],
       [0, 0, 4, 0, 7, 8, 0, 2, 9],
       [2, 0, 9, 0, 8, 4, 3, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 3, 9, 5, 0, 7, 0, 4],
       [6, 1, 0, 3, 2, 0, 8, 0, 0],
       [4, 0, 2, 0, 0, 5, 1, 0, 0],
       [0, 0, 0, 0, 0, 0, 9, 0, 0]], dtype=int64)
>>> recogn1 - recogn2
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 3, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 3, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> recogn1 - recogn
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 3, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 3, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> recogn - recogn2
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> recogn1 - recogn3
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Extracting /tmp/tensorflow\train-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\train-labels-idx1-ubyte.gz
Extracting /tmp/tensorflow\t10k-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\t10k-labels-idx1-ubyte.gz
>>> recogn
array([[4, 0, 0, 0, 0, 0, 0, 0, 6],
       [0, 0, 1, 0, 0, 0, 2, 0, 0],
       [0, 5, 0, 9, 0, 3, 0, 4, 0],
       [1, 0, 0, 0, 6, 0, 0, 0, 9],
       [0, 7, 0, 0, 0, 0, 0, 8, 0],
       [3, 0, 0, 5, 0, 7, 0, 0, 1],
       [0, 9, 0, 4, 0, 8, 0, 1, 0],
       [0, 0, 5, 0, 0, 0, 7, 0, 0],
       [2, 0, 0, 0, 0, 0, 0, 0, 4]], dtype=int64)
>>> cv2.imshow('nk',img)
>>> recogn - recogn1
array([[ 0,  0,  0,  0,  0,  0,  0,  0, -2],
       [ 0,  0,  0,  0,  0,  0,  0,  0,  0],
       [ 0,  0,  0,  0,  0,  0,  0,  0,  0],
       [ 0,  0,  0,  0,  0,  0,  0,  0,  0],
       [ 0,  0,  0,  0,  0,  0,  0,  0,  0],
       [ 0,  0,  0,  0,  0,  0,  0,  0,  0],
       [ 0,  0,  0,  0,  0,  0,  0,  0,  0],
       [ 0,  0,  0,  0,  0,  0,  0,  0,  0],
       [ 0,  0,  0,  0,  0,  0,  0,  0,  0]], dtype=int64)
>>> recogn1
array([[4, 0, 0, 0, 0, 0, 0, 0, 8],
       [0, 0, 1, 0, 0, 0, 2, 0, 0],
       [0, 5, 0, 9, 0, 3, 0, 4, 0],
       [1, 0, 0, 0, 6, 0, 0, 0, 9],
       [0, 7, 0, 0, 0, 0, 0, 8, 0],
       [3, 0, 0, 5, 0, 7, 0, 0, 1],
       [0, 9, 0, 4, 0, 8, 0, 1, 0],
       [0, 0, 5, 0, 0, 0, 7, 0, 0],
       [2, 0, 0, 0, 0, 0, 0, 0, 4]], dtype=int64)
>>> recogn2
array([[4, 0, 0, 0, 0, 0, 0, 0, 6],
       [0, 0, 1, 0, 0, 0, 2, 0, 0],
       [0, 5, 0, 9, 0, 3, 0, 4, 0],
       [1, 0, 0, 0, 6, 0, 0, 0, 9],
       [0, 7, 0, 0, 0, 0, 0, 8, 0],
       [3, 0, 0, 5, 0, 7, 0, 0, 1],
       [0, 9, 0, 4, 0, 8, 0, 1, 0],
       [0, 0, 5, 0, 0, 0, 7, 0, 0],
       [2, 0, 0, 0, 0, 0, 0, 0, 4]], dtype=int64)
>>> recogn2 - recogn
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> recogn3-recogn1
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Extracting /tmp/tensorflow\train-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\train-labels-idx1-ubyte.gz
Extracting /tmp/tensorflow\t10k-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\t10k-labels-idx1-ubyte.gz
>>> recogn
array([[0, 0, 4, 0, 0, 0, 7, 0, 0],
       [6, 7, 0, 0, 0, 0, 0, 9, 3],
       [3, 0, 0, 7, 0, 0, 0, 5, 0],
       [0, 0, 9, 4, 5, 0, 0, 3, 0],
       [4, 0, 0, 9, 0, 7, 0, 0, 6],
       [0, 1, 0, 0, 6, 3, 2, 0, 0],
       [0, 8, 0, 0, 0, 1, 0, 0, 4],
       [5, 4, 0, 0, 0, 0, 0, 6, 1],
       [0, 0, 2, 0, 0, 0, 8, 0, 0]], dtype=int64)
>>> recogn - recogn1
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> recogn - recogn2
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> recogn - recogn3
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Traceback (most recent call last):
  File "C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py", line 8, in <module>
    from prepross import *
  File "C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\prepross.py", line 237, in <module>
    mat = np.array([StDev(imBox[i]) for i in range(imBox.shape[0])]).reshape((9,9))
ValueError: total size of new array must be unchanged
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Extracting /tmp/tensorflow\train-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\train-labels-idx1-ubyte.gz
Extracting /tmp/tensorflow\t10k-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\t10k-labels-idx1-ubyte.gz
Traceback (most recent call last):
  File "C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py", line 283, in <module>
    recogn = session.run(y_pred_cls,feed_dict).reshape((9,9))
ValueError: total size of new array must be unchanged
>>> cv2.imshow('nk',img)
>>> cv2.imshow('nk',imB)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Extracting /tmp/tensorflow\train-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\train-labels-idx1-ubyte.gz
Extracting /tmp/tensorflow\t10k-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\t10k-labels-idx1-ubyte.gz
Traceback (most recent call last):
  File "C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py", line 283, in <module>
    recogn = session.run(y_pred_cls,feed_dict).reshape((9,9))
ValueError: total size of new array must be unchanged
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Extracting /tmp/tensorflow\train-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\train-labels-idx1-ubyte.gz
Extracting /tmp/tensorflow\t10k-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\t10k-labels-idx1-ubyte.gz
Traceback (most recent call last):
  File "C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py", line 283, in <module>
    recogn = session.run(y_pred_cls,feed_dict).reshape((9,9))
ValueError: total size of new array must be unchanged
>>> cv2.imshow('nk',255-img)
>>> img.mean
<built-in method mean of numpy.ndarray object at 0x000000EB95BBA580>
>>> img.min
<built-in method min of numpy.ndarray object at 0x000000EB95BBA580>
>>> img.argmin()
664
>>> img.mean()
223.04096348153084
>>> img.min()
0
>>> I = (img>img.mean()/2)*img
>>> cv2.imshow('nk',I)
>>> I = (img<img.mean()/2)*255
>>> cv2.imshow('nk',I)
>>> I = (img>img.mean()/2)*255
>>> cv2.imshow('nk',I)
>>> I = (img>img.mean())*255
>>> cv2.imshow('nk',I)
>>> I = (img<10)*255
>>> cv2.imshow('nk',I)
>>> I
array([[  0,   0,   0, ...,   0,   0,   0],
       [  0,   0,   0, ...,   0,   0,   0],
       [  0,   0, 255, ...,   0,   0,   0],
       ..., 
       [  0,   0,   0, ...,   0,   0,   0],
       [  0,   0,   0, ...,   0,   0,   0],
       [  0,   0,   0, ...,   0,   0,   0]])
>>> I = (img<100)*255
>>> cv2.imshow('nk',I)
>>> I = (img<100)*0
>>> cv2.imshow('nk',I)
>>> I = (img<100)*1
>>> I
array([[0, 0, 0, ..., 0, 0, 0],
       [0, 0, 1, ..., 0, 0, 0],
       [0, 1, 1, ..., 1, 0, 0],
       ..., 
       [0, 0, 1, ..., 0, 0, 0],
       [0, 0, 0, ..., 0, 0, 0],
       [0, 0, 0, ..., 0, 0, 0]])
>>> cv2.imshow('nk',I*255)
>>> I = (img>100)*1
>>> cv2.imshow('nk',I*255)
>>> I
array([[1, 1, 1, ..., 1, 1, 1],
       [1, 1, 0, ..., 1, 1, 1],
       [1, 0, 0, ..., 0, 1, 1],
       ..., 
       [1, 1, 0, ..., 1, 1, 1],
       [1, 1, 1, ..., 1, 1, 1],
       [1, 1, 1, ..., 1, 1, 1]])
>>> cv2.imshow('nk',I*255)
>>> cv2.imshow('nk',I*200)
>>> cv2.imshow('nk',img)
>>> img
array([[255, 247, 255, ..., 254, 253, 253],
       [247, 122,  71, ..., 133, 246, 255],
       [255,  61,   0, ...,  62, 255, 255],
       ..., 
       [252, 129,  57, ..., 217, 241, 255],
       [255, 250, 255, ..., 245, 255, 255],
       [250, 250, 254, ..., 255, 255, 255]], dtype=uint8)
>>> cv2.imshow('nk',I*200)
>>> cv2.imshow('nk',I*100)
>>> img<15
array([[False, False, False, ..., False, False, False],
       [False, False, False, ..., False, False, False],
       [False, False,  True, ..., False, False, False],
       ..., 
       [False, False, False, ..., False, False, False],
       [False, False, False, ..., False, False, False],
       [False, False, False, ..., False, False, False]], dtype=bool)
>>> img<70
array([[False, False, False, ..., False, False, False],
       [False, False, False, ..., False, False, False],
       [False,  True,  True, ...,  True, False, False],
       ..., 
       [False, False,  True, ..., False, False, False],
       [False, False, False, ..., False, False, False],
       [False, False, False, ..., False, False, False]], dtype=bool)
>>> img<70 *1
array([[False, False, False, ..., False, False, False],
       [False, False, False, ..., False, False, False],
       [False,  True,  True, ...,  True, False, False],
       ..., 
       [False, False,  True, ..., False, False, False],
       [False, False, False, ..., False, False, False],
       [False, False, False, ..., False, False, False]], dtype=bool)
>>> (img<70)*1
array([[0, 0, 0, ..., 0, 0, 0],
       [0, 0, 0, ..., 0, 0, 0],
       [0, 1, 1, ..., 1, 0, 0],
       ..., 
       [0, 0, 1, ..., 0, 0, 0],
       [0, 0, 0, ..., 0, 0, 0],
       [0, 0, 0, ..., 0, 0, 0]])
>>> cv2.imshow('nk',(img<70)*1)
>>> cv2.imshow('nk',255*(img<70)*1)
>>> plt.imshow('nk',255*(img<70)*1)
Traceback (most recent call last):
  File "<pyshell#149>", line 1, in <module>
    plt.imshow('nk',255*(img<70)*1)
  File "C:\python35\lib\site-packages\matplotlib\pyplot.py", line 3029, in imshow
    **kwargs)
  File "C:\python35\lib\site-packages\matplotlib\__init__.py", line 1819, in inner
    return func(ax, *args, **kwargs)
  File "C:\python35\lib\site-packages\matplotlib\axes\_axes.py", line 4920, in imshow
    resample=resample, **kwargs)
  File "C:\python35\lib\site-packages\matplotlib\image.py", line 597, in __init__
    **kwargs
  File "C:\python35\lib\site-packages\matplotlib\image.py", line 109, in __init__
    cm.ScalarMappable.__init__(self, norm, cmap)
  File "C:\python35\lib\site-packages\matplotlib\cm.py", line 201, in __init__
    self.cmap = get_cmap(cmap)
  File "C:\python35\lib\site-packages\matplotlib\cm.py", line 158, in get_cmap
    if name in cmap_d:
TypeError: unhashable type: 'numpy.ndarray'
>>> plt.imshow(255*(img<70)*1,gray='true')
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    plt.imshow(255*(img<70)*1,gray='true')
  File "C:\python35\lib\site-packages\matplotlib\pyplot.py", line 3029, in imshow
    **kwargs)
  File "C:\python35\lib\site-packages\matplotlib\__init__.py", line 1819, in inner
    return func(ax, *args, **kwargs)
  File "C:\python35\lib\site-packages\matplotlib\axes\_axes.py", line 4920, in imshow
    resample=resample, **kwargs)
  File "C:\python35\lib\site-packages\matplotlib\image.py", line 597, in __init__
    **kwargs
  File "C:\python35\lib\site-packages\matplotlib\image.py", line 130, in __init__
    self.update(kwargs)
  File "C:\python35\lib\site-packages\matplotlib\artist.py", line 859, in update
    raise AttributeError('Unknown property %s' % k)
AttributeError: Unknown property gray
>>> plt.imshow(255*(img<70)*1)
<matplotlib.image.AxesImage object at 0x000000EB973B7F60>
>>> plt.show()
Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    plt.show()
  File "C:\python35\lib\site-packages\matplotlib\pyplot.py", line 252, in show
    return _show(*args, **kw)
  File "C:\python35\lib\site-packages\matplotlib\backend_bases.py", line 192, in __call__
    self.mainloop()
  File "C:\python35\lib\site-packages\matplotlib\backends\backend_tkagg.py", line 74, in mainloop
    Tk.mainloop()
  File "C:\python35\lib\tkinter\__init__.py", line 405, in mainloop
    _default_root.tk.mainloop(n)
KeyboardInterrupt
>>> plt.imshow(255*(img>img.mean)*1,cmap = True)
Traceback (most recent call last):
  File "<pyshell#153>", line 1, in <module>
    plt.imshow(255*(img>img.mean)*1,cmap = True)
TypeError: unorderable types: int() > builtin_function_or_method()
>>> plt.imshow(255*(img>img.mean)*1,cmap = 1)
Traceback (most recent call last):
  File "<pyshell#154>", line 1, in <module>
    plt.imshow(255*(img>img.mean)*1,cmap = 1)
TypeError: unorderable types: int() > builtin_function_or_method()
>>> plt.imshow(255*(img>img.mean)*1,cmap=1)
Traceback (most recent call last):
  File "<pyshell#155>", line 1, in <module>
    plt.imshow(255*(img>img.mean)*1,cmap=1)
TypeError: unorderable types: int() > builtin_function_or_method()
>>> plt.imshow(255*(img>img.mean)*1,cmap=0)
Traceback (most recent call last):
  File "<pyshell#156>", line 1, in <module>
    plt.imshow(255*(img>img.mean)*1,cmap=0)
TypeError: unorderable types: int() > builtin_function_or_method()
>>> plt.imshow(255*(img>img.mean)*1)
Traceback (most recent call last):
  File "<pyshell#157>", line 1, in <module>
    plt.imshow(255*(img>img.mean)*1)
TypeError: unorderable types: int() > builtin_function_or_method()
>>> plt.imshow(255*(img>img.mean())*1,cmap = True)
Traceback (most recent call last):
  File "<pyshell#158>", line 1, in <module>
    plt.imshow(255*(img>img.mean())*1,cmap = True)
  File "C:\python35\lib\site-packages\matplotlib\pyplot.py", line 3029, in imshow
    **kwargs)
  File "C:\python35\lib\site-packages\matplotlib\__init__.py", line 1819, in inner
    return func(ax, *args, **kwargs)
  File "C:\python35\lib\site-packages\matplotlib\axes\_axes.py", line 4920, in imshow
    resample=resample, **kwargs)
  File "C:\python35\lib\site-packages\matplotlib\image.py", line 597, in __init__
    **kwargs
  File "C:\python35\lib\site-packages\matplotlib\image.py", line 109, in __init__
    cm.ScalarMappable.__init__(self, norm, cmap)
  File "C:\python35\lib\site-packages\matplotlib\cm.py", line 201, in __init__
    self.cmap = get_cmap(cmap)
  File "C:\python35\lib\site-packages\matplotlib\cm.py", line 166, in get_cmap
    % (name, ', '.join(sorted(cmap_d.keys()))))
ValueError: Colormap True is not recognized. Possible values are: Accent, Accent_r, Blues, Blues_r, BrBG, BrBG_r, BuGn, BuGn_r, BuPu, BuPu_r, CMRmap, CMRmap_r, Dark2, Dark2_r, GnBu, GnBu_r, Greens, Greens_r, Greys, Greys_r, OrRd, OrRd_r, Oranges, Oranges_r, PRGn, PRGn_r, Paired, Paired_r, Pastel1, Pastel1_r, Pastel2, Pastel2_r, PiYG, PiYG_r, PuBu, PuBuGn, PuBuGn_r, PuBu_r, PuOr, PuOr_r, PuRd, PuRd_r, Purples, Purples_r, RdBu, RdBu_r, RdGy, RdGy_r, RdPu, RdPu_r, RdYlBu, RdYlBu_r, RdYlGn, RdYlGn_r, Reds, Reds_r, Set1, Set1_r, Set2, Set2_r, Set3, Set3_r, Spectral, Spectral_r, Wistia, Wistia_r, YlGn, YlGnBu, YlGnBu_r, YlGn_r, YlOrBr, YlOrBr_r, YlOrRd, YlOrRd_r, afmhot, afmhot_r, autumn, autumn_r, binary, binary_r, bone, bone_r, brg, brg_r, bwr, bwr_r, cool, cool_r, coolwarm, coolwarm_r, copper, copper_r, cubehelix, cubehelix_r, flag, flag_r, gist_earth, gist_earth_r, gist_gray, gist_gray_r, gist_heat, gist_heat_r, gist_ncar, gist_ncar_r, gist_rainbow, gist_rainbow_r, gist_stern, gist_stern_r, gist_yarg, gist_yarg_r, gnuplot, gnuplot2, gnuplot2_r, gnuplot_r, gray, gray_r, hot, hot_r, hsv, hsv_r, inferno, inferno_r, jet, jet_r, magma, magma_r, nipy_spectral, nipy_spectral_r, ocean, ocean_r, pink, pink_r, plasma, plasma_r, prism, prism_r, rainbow, rainbow_r, seismic, seismic_r, spectral, spectral_r, spring, spring_r, summer, summer_r, terrain, terrain_r, viridis, viridis_r, winter, winter_r
>>> plt.imshow(255*(img>img.mean())*1,cmap = 1)
Traceback (most recent call last):
  File "<pyshell#159>", line 1, in <module>
    plt.imshow(255*(img>img.mean())*1,cmap = 1)
  File "C:\python35\lib\site-packages\matplotlib\pyplot.py", line 3029, in imshow
    **kwargs)
  File "C:\python35\lib\site-packages\matplotlib\__init__.py", line 1819, in inner
    return func(ax, *args, **kwargs)
  File "C:\python35\lib\site-packages\matplotlib\axes\_axes.py", line 4920, in imshow
    resample=resample, **kwargs)
  File "C:\python35\lib\site-packages\matplotlib\image.py", line 597, in __init__
    **kwargs
  File "C:\python35\lib\site-packages\matplotlib\image.py", line 109, in __init__
    cm.ScalarMappable.__init__(self, norm, cmap)
  File "C:\python35\lib\site-packages\matplotlib\cm.py", line 201, in __init__
    self.cmap = get_cmap(cmap)
  File "C:\python35\lib\site-packages\matplotlib\cm.py", line 166, in get_cmap
    % (name, ', '.join(sorted(cmap_d.keys()))))
ValueError: Colormap 1 is not recognized. Possible values are: Accent, Accent_r, Blues, Blues_r, BrBG, BrBG_r, BuGn, BuGn_r, BuPu, BuPu_r, CMRmap, CMRmap_r, Dark2, Dark2_r, GnBu, GnBu_r, Greens, Greens_r, Greys, Greys_r, OrRd, OrRd_r, Oranges, Oranges_r, PRGn, PRGn_r, Paired, Paired_r, Pastel1, Pastel1_r, Pastel2, Pastel2_r, PiYG, PiYG_r, PuBu, PuBuGn, PuBuGn_r, PuBu_r, PuOr, PuOr_r, PuRd, PuRd_r, Purples, Purples_r, RdBu, RdBu_r, RdGy, RdGy_r, RdPu, RdPu_r, RdYlBu, RdYlBu_r, RdYlGn, RdYlGn_r, Reds, Reds_r, Set1, Set1_r, Set2, Set2_r, Set3, Set3_r, Spectral, Spectral_r, Wistia, Wistia_r, YlGn, YlGnBu, YlGnBu_r, YlGn_r, YlOrBr, YlOrBr_r, YlOrRd, YlOrRd_r, afmhot, afmhot_r, autumn, autumn_r, binary, binary_r, bone, bone_r, brg, brg_r, bwr, bwr_r, cool, cool_r, coolwarm, coolwarm_r, copper, copper_r, cubehelix, cubehelix_r, flag, flag_r, gist_earth, gist_earth_r, gist_gray, gist_gray_r, gist_heat, gist_heat_r, gist_ncar, gist_ncar_r, gist_rainbow, gist_rainbow_r, gist_stern, gist_stern_r, gist_yarg, gist_yarg_r, gnuplot, gnuplot2, gnuplot2_r, gnuplot_r, gray, gray_r, hot, hot_r, hsv, hsv_r, inferno, inferno_r, jet, jet_r, magma, magma_r, nipy_spectral, nipy_spectral_r, ocean, ocean_r, pink, pink_r, plasma, plasma_r, prism, prism_r, rainbow, rainbow_r, seismic, seismic_r, spectral, spectral_r, spring, spring_r, summer, summer_r, terrain, terrain_r, viridis, viridis_r, winter, winter_r
>>> plt.imshow(255*(img>img.mean())*1,cmap ='gray')
<matplotlib.image.AxesImage object at 0x000000EB98D082E8>
>>> plt.show()

 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Traceback (most recent call last):
  File "C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py", line 8, in <module>
    from prepross import *
  File "C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\prepross.py", line 228, in <module>
    stat = ExtractBoxes(I,connexity = 8,thresh=(lx/18,ly/18,lx/3,ly/3))
  File "C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\prepross.py", line 129, in ExtractBoxes
    output = cv2.connectedComponentsWithStats(imBinarized,connexity)
cv2.error: C:\projects\opencv-python\opencv\modules\imgproc\src\connectedcomponents.cpp:349: error: (-215) iDepth == CV_8U || iDepth == CV_8S in function cv::connectedComponents_sub1

>>> I
Traceback (most recent call last):
  File "<pyshell#162>", line 1, in <module>
    I
NameError: name 'I' is not defined
>>> I = (img>img.mean())*255
Traceback (most recent call last):
  File "<pyshell#163>", line 1, in <module>
    I = (img>img.mean())*255
NameError: name 'img' is not defined
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\prepross.py 
>>> I = (img>img.mean())*255
>>> I
array([[255, 255, 255, ..., 255, 255, 255],
       [255,   0,   0, ...,   0, 255, 255],
       [255,   0,   0, ...,   0, 255, 255],
       ..., 
       [255,   0,   0, ...,   0, 255, 255],
       [255, 255, 255, ..., 255, 255, 255],
       [255, 255, 255, ..., 255, 255, 255]])
>>> imB
array([[255, 255, 255, ..., 255, 255, 255],
       [255,   0,   0, ...,   0, 255, 255],
       [255,   0,   0, ...,   0, 255, 255],
       ..., 
       [255,   0,   0, ..., 255, 255, 255],
       [255, 255, 255, ..., 255, 255, 255],
       [255, 255, 255, ..., 255, 255, 255]], dtype=uint8)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\prepross.py 
Traceback (most recent call last):
  File "C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\prepross.py", line 228, in <module>
    stat = ExtractBoxes(I,connexity = 8,thresh=(lx/18,ly/18,lx/3,ly/3))
NameError: name 'I' is not defined
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\prepross.py 
Traceback (most recent call last):
  File "C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\prepross.py", line 228, in <module>
    stat = ExtractBoxes(I,connexity = 8,thresh=(lx/18,ly/18,lx/3,ly/3))
  File "C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\prepross.py", line 129, in ExtractBoxes
    output = cv2.connectedComponentsWithStats(imBinarized,connexity)
cv2.error: C:\projects\opencv-python\opencv\modules\imgproc\src\connectedcomponents.cpp:349: error: (-215) iDepth == CV_8U || iDepth == CV_8S in function cv::connectedComponents_sub1

>>> I
array([[255, 255, 255, ..., 255, 255, 255],
       [255,   0,   0, ...,   0, 255, 255],
       [255,   0,   0, ...,   0, 255, 255],
       ..., 
       [255,   0,   0, ...,   0, 255, 255],
       [255, 255, 255, ..., 255, 255, 255],
       [255, 255, 255, ..., 255, 255, 255]])
>>> I.shape
(331, 331)
>>> imB
array([[255, 255, 255, ..., 255, 255, 255],
       [255,   0,   0, ...,   0, 255, 255],
       [255,   0,   0, ...,   0, 255, 255],
       ..., 
       [255,   0,   0, ..., 255, 255, 255],
       [255, 255, 255, ..., 255, 255, 255],
       [255, 255, 255, ..., 255, 255, 255]], dtype=uint8)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\prepross.py 
>>> I
array([[ True,  True,  True, ...,  True,  True,  True],
       [ True, False, False, ..., False,  True,  True],
       [ True, False, False, ..., False,  True,  True],
       ..., 
       [ True, False, False, ..., False,  True,  True],
       [ True,  True,  True, ...,  True,  True,  True],
       [ True,  True,  True, ...,  True,  True,  True]], dtype=bool)
>>> cv2.imshow('jn',imB*I)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Extracting /tmp/tensorflow\train-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\train-labels-idx1-ubyte.gz
Extracting /tmp/tensorflow\t10k-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\t10k-labels-idx1-ubyte.gz
>>> recogn
array([[0, 5, 0, 1, 0, 0, 0, 0, 6],
       [0, 1, 8, 0, 3, 0, 0, 9, 0],
       [0, 3, 0, 0, 2, 0, 0, 0, 0],
       [9, 2, 0, 0, 4, 0, 8, 0, 0],
       [0, 0, 0, 2, 0, 5, 0, 0, 0],
       [0, 0, 1, 0, 9, 0, 0, 2, 3],
       [0, 0, 0, 0, 7, 0, 0, 6, 0],
       [0, 9, 0, 0, 5, 0, 4, 8, 0],
       [1, 0, 0, 0, 0, 8, 0, 5, 0]], dtype=int64)
>>> recogn - recogn1
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> recogn - recogn2
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> recogn - recogn3
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Extracting /tmp/tensorflow\train-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\train-labels-idx1-ubyte.gz
Extracting /tmp/tensorflow\t10k-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\t10k-labels-idx1-ubyte.gz
>>> cv2.imshow('jn',imB*I)
>>> recogn
array([[0, 0, 4, 0, 0, 0, 7, 0, 0],
       [6, 7, 0, 0, 0, 0, 0, 9, 3],
       [3, 0, 0, 7, 0, 0, 0, 5, 0],
       [0, 0, 9, 4, 5, 0, 0, 3, 0],
       [4, 0, 0, 9, 0, 7, 0, 0, 6],
       [0, 1, 0, 0, 6, 3, 2, 0, 0],
       [0, 8, 0, 0, 0, 1, 0, 0, 4],
       [5, 4, 0, 0, 0, 0, 0, 6, 1],
       [0, 0, 2, 0, 0, 0, 8, 0, 0]], dtype=int64)
>>> recogn - recogn1
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> recogn - recogn2
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> recogn - recogn3
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Extracting /tmp/tensorflow\train-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\train-labels-idx1-ubyte.gz
Extracting /tmp/tensorflow\t10k-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\t10k-labels-idx1-ubyte.gz
>>> cv2.imshow('jn',imB*I)
>>> cv2.imshow('jn',imB)
>>> cv2.imshow('jn',imB*I)
>>> recogn
array([[0, 0, 0, 0, 5, 0, 0, 0, 0],
       [1, 0, 0, 0, 0, 0, 0, 0, 7],
       [0, 4, 0, 8, 0, 1, 0, 3, 0],
       [7, 0, 0, 0, 0, 0, 0, 0, 2],
       [0, 0, 1, 0, 0, 0, 8, 0, 0],
       [0, 9, 8, 3, 0, 7, 1, 4, 0],
       [0, 1, 0, 0, 3, 0, 0, 2, 0],
       [0, 0, 3, 9, 0, 5, 6, 0, 0],
       [0, 0, 4, 1, 0, 6, 7, 0, 0]], dtype=int64)
>>> recogn - recogn1
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> recogn - recogn2
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> recogn - recogn3
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Extracting /tmp/tensorflow\train-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\train-labels-idx1-ubyte.gz
Extracting /tmp/tensorflow\t10k-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\t10k-labels-idx1-ubyte.gz
>>> cv2.imshow('jn',imB*I)
>>> cv2.imshow('jnl',imB)
>>> recogn
array([[3, 0, 0, 0, 9, 0, 0, 0, 0],
       [0, 5, 1, 8, 3, 0, 7, 0, 0],
       [0, 0, 7, 0, 0, 0, 9, 0, 6],
       [0, 0, 5, 0, 0, 0, 0, 0, 7],
       [0, 0, 9, 0, 8, 0, 3, 5, 0],
       [0, 0, 0, 9, 2, 0, 0, 0, 1],
       [0, 0, 0, 0, 4, 2, 0, 0, 0],
       [0, 0, 2, 5, 0, 0, 0, 6, 3],
       [1, 4, 0, 0, 0, 0, 8, 0, 0]], dtype=int64)
>>> recogn - recogn1
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> recogn - recogn2
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> recogn - recogn3
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Extracting /tmp/tensorflow\train-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\train-labels-idx1-ubyte.gz
Extracting /tmp/tensorflow\t10k-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\t10k-labels-idx1-ubyte.gz
>>> cv2.imshow('jn',imB*I)
>>> recogn
array([[0, 9, 0, 0, 0, 0, 0, 3, 6],
       [1, 0, 0, 3, 2, 9, 6, 0, 0],
       [0, 0, 3, 0, 9, 0, 0, 0, 0],
       [3, 0, 2, 9, 3, 6, 0, 0, 1],
       [0, 6, 0, 2, 1, 9, 0, 6, 0],
       [0, 1, 0, 0, 0, 0, 0, 6, 0],
       [0, 2, 7, 1, 0, 6, 3, 9, 3],
       [0, 9, 1, 3, 9, 0, 7, 0, 6],
       [0, 0, 6, 9, 7, 0, 6, 0, 0]], dtype=int64)
>>> recogn1
array([[0, 9, 0, 0, 0, 0, 0, 3, 6],
       [1, 0, 0, 3, 2, 9, 9, 0, 0],
       [0, 0, 3, 0, 9, 0, 0, 0, 0],
       [3, 0, 2, 9, 3, 6, 0, 0, 1],
       [0, 6, 0, 2, 1, 9, 0, 9, 0],
       [0, 1, 0, 0, 0, 0, 0, 6, 0],
       [0, 2, 7, 1, 0, 9, 3, 9, 3],
       [0, 9, 1, 3, 9, 0, 7, 0, 9],
       [0, 0, 9, 9, 7, 0, 6, 0, 0]], dtype=int64)
>>> cv2.imshow('jn',imB)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Extracting /tmp/tensorflow\train-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\train-labels-idx1-ubyte.gz
Extracting /tmp/tensorflow\t10k-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\t10k-labels-idx1-ubyte.gz
>>> recogn
array([[2, 9, 9, 7, 9, 3, 1, 3, 8],
       [1, 7, 6, 3, 2, 9, 9, 3, 9],
       [9, 3, 3, 6, 9, 1, 2, 9, 7],
       [3, 9, 2, 9, 3, 8, 9, 7, 1],
       [7, 8, 3, 2, 1, 9, 9, 9, 3],
       [9, 1, 9, 9, 3, 7, 3, 8, 2],
       [9, 2, 7, 1, 6, 9, 3, 9, 3],
       [6, 9, 1, 3, 9, 3, 7, 2, 9],
       [3, 3, 9, 9, 7, 2, 8, 1, 9]], dtype=int64)
>>> recogn3
array([[2, 9, 9, 7, 9, 3, 1, 3, 8],
       [1, 7, 6, 3, 2, 9, 9, 3, 9],
       [9, 3, 3, 6, 9, 1, 2, 9, 7],
       [3, 9, 2, 9, 3, 8, 9, 7, 1],
       [7, 8, 3, 2, 1, 9, 9, 9, 3],
       [9, 1, 9, 9, 3, 7, 3, 8, 2],
       [9, 2, 7, 1, 6, 9, 3, 9, 3],
       [6, 9, 1, 3, 9, 3, 7, 2, 9],
       [3, 3, 9, 9, 7, 2, 8, 1, 9]], dtype=int64)
>>> cv2.imshow('jn',imB*I)
>>> recogn1
array([[2, 9, 9, 7, 9, 3, 1, 3, 8],
       [1, 7, 6, 3, 2, 9, 6, 3, 9],
       [9, 3, 3, 6, 9, 1, 2, 9, 7],
       [3, 9, 2, 9, 3, 8, 9, 7, 1],
       [7, 8, 3, 2, 1, 9, 9, 6, 3],
       [9, 1, 9, 9, 3, 7, 3, 8, 2],
       [9, 2, 7, 1, 6, 6, 3, 9, 3],
       [6, 9, 1, 3, 9, 3, 7, 2, 6],
       [3, 3, 6, 9, 7, 2, 8, 1, 9]], dtype=int64)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Extracting /tmp/tensorflow\train-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\train-labels-idx1-ubyte.gz
Extracting /tmp/tensorflow\t10k-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\t10k-labels-idx1-ubyte.gz
>>> cv2.imshow('jn',imB*I)
>>> recogn
array([[0, 0, 7, 9, 6, 2, 4, 0, 0],
       [9, 0, 0, 0, 1, 0, 0, 0, 2],
       [0, 1, 0, 8, 5, 3, 0, 6, 0],
       [5, 0, 0, 4, 7, 9, 0, 0, 1],
       [0, 0, 0, 0, 8, 0, 0, 0, 0],
       [4, 0, 0, 3, 2, 1, 0, 0, 7],
       [0, 9, 0, 2, 4, 8, 0, 5, 0],
       [6, 0, 0, 0, 3, 0, 0, 0, 8],
       [0, 0, 8, 6, 9, 5, 1, 0, 0]], dtype=int64)
>>> recogn - recogn1
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> recogn - recogn2
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> recogn - recogn3
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Extracting /tmp/tensorflow\train-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\train-labels-idx1-ubyte.gz
Extracting /tmp/tensorflow\t10k-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\t10k-labels-idx1-ubyte.gz
>>> cv2.imshow('jn',imB*I)
>>> recogn
array([[0, 0, 4, 5, 7, 9, 8, 0, 0],
       [2, 6, 0, 0, 0, 8, 0, 0, 0],
       [0, 0, 0, 0, 5, 0, 4, 0, 0],
       [9, 2, 0, 0, 0, 5, 1, 8, 4],
       [0, 4, 0, 2, 0, 1, 0, 9, 0],
       [1, 8, 6, 9, 0, 0, 0, 2, 5],
       [0, 0, 1, 0, 9, 0, 0, 0, 0],
       [0, 0, 0, 5, 0, 0, 0, 4, 8],
       [0, 0, 3, 7, 2, 4, 6, 0, 0]], dtype=int64)
>>> recogn1
array([[0, 0, 4, 5, 7, 9, 8, 0, 0],
       [2, 6, 0, 0, 0, 8, 0, 0, 0],
       [0, 0, 0, 0, 5, 0, 4, 0, 0],
       [9, 2, 0, 0, 0, 5, 1, 8, 4],
       [0, 4, 0, 2, 0, 1, 0, 9, 0],
       [1, 8, 6, 9, 0, 0, 0, 2, 5],
       [0, 0, 1, 0, 9, 0, 0, 0, 0],
       [0, 0, 0, 5, 0, 0, 0, 4, 8],
       [0, 0, 3, 7, 2, 4, 6, 0, 0]], dtype=int64)
>>> recogn - recogn1
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> recogn - recogn2
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> recogn - recogn3
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> cv2.imshow('jn',imB)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Extracting /tmp/tensorflow\train-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\train-labels-idx1-ubyte.gz
Extracting /tmp/tensorflow\t10k-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\t10k-labels-idx1-ubyte.gz
>>> recogn
array([[0, 0, 4, 5, 7, 9, 8, 0, 0],
       [2, 6, 0, 0, 0, 8, 0, 0, 0],
       [0, 0, 0, 0, 5, 0, 4, 0, 0],
       [9, 2, 0, 0, 0, 5, 1, 8, 4],
       [0, 4, 0, 2, 0, 1, 0, 9, 0],
       [1, 8, 6, 9, 0, 0, 0, 2, 5],
       [0, 0, 1, 0, 9, 0, 0, 0, 0],
       [0, 0, 0, 5, 0, 0, 0, 4, 8],
       [0, 0, 3, 7, 2, 4, 6, 0, 0]], dtype=int64)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Extracting /tmp/tensorflow\train-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\train-labels-idx1-ubyte.gz
Extracting /tmp/tensorflow\t10k-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\t10k-labels-idx1-ubyte.gz
>>> re
Traceback (most recent call last):
  File "<pyshell#215>", line 1, in <module>
    re
NameError: name 're' is not defined
>>> recogn
array([[0, 0, 4, 6, 7, 9, 8, 0, 0],
       [2, 6, 0, 0, 0, 8, 0, 0, 0],
       [0, 0, 0, 0, 5, 0, 4, 0, 0],
       [9, 2, 0, 0, 0, 5, 1, 8, 4],
       [0, 4, 0, 2, 0, 1, 0, 9, 0],
       [1, 8, 6, 9, 0, 0, 0, 2, 5],
       [0, 0, 1, 0, 9, 0, 0, 0, 0],
       [0, 0, 0, 5, 0, 0, 0, 4, 8],
       [0, 0, 3, 7, 2, 4, 6, 0, 0]], dtype=int64)
>>> recogn1
array([[0, 0, 4, 5, 7, 9, 8, 0, 0],
       [2, 6, 0, 0, 0, 8, 0, 0, 0],
       [0, 0, 0, 0, 5, 0, 4, 0, 0],
       [9, 2, 0, 0, 0, 5, 1, 8, 4],
       [0, 4, 0, 2, 0, 1, 0, 9, 0],
       [1, 8, 6, 9, 0, 0, 0, 2, 5],
       [0, 0, 1, 0, 9, 0, 0, 0, 0],
       [0, 0, 0, 5, 0, 0, 0, 4, 8],
       [0, 0, 3, 7, 2, 4, 6, 0, 0]], dtype=int64)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Extracting /tmp/tensorflow\train-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\train-labels-idx1-ubyte.gz
Extracting /tmp/tensorflow\t10k-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\t10k-labels-idx1-ubyte.gz
Traceback (most recent call last):
  File "C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py", line 283, in <module>
    recogn = session.run(y_pred_cls,feed_dict).reshape((9,9))
ValueError: total size of new array must be unchanged
>>> cv2.imshow('jn',imB)
>>> cv2.imshow('jn',imB*I)
>>> cv2.imshow('jn',img)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Extracting /tmp/tensorflow\train-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\train-labels-idx1-ubyte.gz
Extracting /tmp/tensorflow\t10k-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\t10k-labels-idx1-ubyte.gz
Traceback (most recent call last):
  File "C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py", line 283, in <module>
    recogn = session.run(y_pred_cls,feed_dict).reshape((9,9))
ValueError: total size of new array must be unchanged
>>> cv2.imshow('jn',imB*I)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\prepross.py 
>>> cv2.imshow('jn',imB*I)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\prepross.py 
>>> cv2.imshow('jn',imB*I)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\prepross.py 
>>> cv2.imshow('jn',imB*I)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\prepross.py 
>>> cv2.imshow('jn',imB*I)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\prepross.py 
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Extracting /tmp/tensorflow\train-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\train-labels-idx1-ubyte.gz
Extracting /tmp/tensorflow\t10k-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\t10k-labels-idx1-ubyte.gz
>>> recogn
array([[1, 2, 6, 5, 4, 7, 9, 3, 8],
       [9, 5, 8, 1, 6, 3, 2, 4, 7],
       [7, 3, 4, 8, 2, 9, 5, 6, 1],
       [8, 4, 7, 9, 1, 2, 6, 5, 3],
       [2, 1, 9, 3, 5, 6, 7, 8, 4],
       [5, 6, 3, 4, 7, 8, 1, 9, 2],
       [3, 7, 2, 6, 9, 4, 8, 1, 5],
       [6, 8, 5, 2, 3, 1, 4, 7, 9],
       [4, 9, 1, 7, 8, 5, 3, 2, 6]], dtype=int64)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\prepross.py 
>>> cv2.imshow('jn',imB*I)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\prepross.py 
>>> cv2.imshow('jn',imB*I)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Extracting /tmp/tensorflow\train-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\train-labels-idx1-ubyte.gz
Extracting /tmp/tensorflow\t10k-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\t10k-labels-idx1-ubyte.gz
>>> recogn -recogn1
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> recogn -recogn2
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> recogn -recogn3
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Extracting /tmp/tensorflow\train-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\train-labels-idx1-ubyte.gz
Extracting /tmp/tensorflow\t10k-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\t10k-labels-idx1-ubyte.gz
>>> img.shape
(1200, 1200)
>>> recogn
array([[0, 0, 3, 0, 9, 2, 0, 0, 0],
       [4, 0, 0, 0, 3, 0, 0, 1, 0],
       [2, 7, 0, 0, 0, 0, 0, 0, 0],
       [0, 1, 0, 3, 0, 0, 0, 0, 5],
       [0, 5, 0, 1, 6, 7, 0, 3, 0],
       [3, 0, 0, 0, 0, 8, 0, 6, 0],
       [0, 0, 0, 0, 0, 0, 0, 5, 3],
       [0, 3, 0, 0, 8, 0, 0, 0, 9],
       [0, 0, 0, 5, 2, 0, 1, 0, 0]], dtype=int64)
>>> recogn1
array([[0, 0, 3, 0, 9, 2, 0, 0, 0],
       [4, 0, 0, 0, 3, 0, 0, 1, 0],
       [2, 7, 0, 0, 0, 0, 0, 0, 0],
       [0, 1, 0, 3, 0, 0, 0, 0, 5],
       [0, 5, 0, 1, 6, 7, 0, 3, 0],
       [3, 0, 0, 0, 0, 8, 0, 6, 0],
       [0, 0, 0, 0, 0, 0, 0, 5, 3],
       [0, 3, 0, 0, 8, 0, 0, 0, 9],
       [0, 0, 0, 5, 2, 0, 1, 0, 0]], dtype=int64)
>>> recogn - recogn1
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> recogn - recogn2
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> recogn - recogn3
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Extracting /tmp/tensorflow\train-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\train-labels-idx1-ubyte.gz
Extracting /tmp/tensorflow\t10k-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\t10k-labels-idx1-ubyte.gz
>>> recogn
array([[0, 0, 3, 0, 9, 2, 0, 0, 0],
       [4, 0, 0, 0, 3, 0, 0, 1, 0],
       [2, 7, 0, 0, 0, 0, 0, 0, 0],
       [0, 1, 0, 3, 0, 0, 0, 0, 5],
       [0, 5, 0, 1, 6, 7, 0, 3, 0],
       [3, 0, 0, 0, 0, 8, 0, 6, 0],
       [0, 0, 0, 0, 0, 0, 0, 5, 3],
       [0, 3, 0, 0, 8, 0, 0, 0, 9],
       [0, 0, 0, 5, 2, 0, 1, 0, 0]], dtype=int64)
>>> recogn1
array([[0, 0, 3, 0, 9, 2, 0, 0, 0],
       [4, 0, 0, 0, 3, 0, 0, 1, 0],
       [2, 7, 0, 0, 0, 0, 0, 0, 0],
       [0, 1, 0, 3, 0, 0, 0, 0, 5],
       [0, 5, 0, 1, 6, 7, 0, 3, 0],
       [3, 0, 0, 0, 0, 8, 0, 6, 0],
       [0, 0, 0, 0, 0, 0, 0, 5, 3],
       [0, 3, 0, 0, 8, 0, 0, 0, 9],
       [0, 0, 0, 5, 2, 0, 1, 0, 0]], dtype=int64)
>>> recogn - recogn1
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> recogn - recogn2
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Extracting /tmp/tensorflow\train-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\train-labels-idx1-ubyte.gz
Extracting /tmp/tensorflow\t10k-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\t10k-labels-idx1-ubyte.gz
>>> recogn
array([[3, 4, 0, 8, 2, 6, 0, 7, 1],
       [0, 0, 8, 0, 0, 0, 9, 0, 0],
       [7, 6, 0, 0, 9, 0, 0, 4, 3],
       [0, 8, 0, 1, 0, 2, 0, 3, 0],
       [0, 3, 0, 0, 0, 0, 0, 9, 0],
       [0, 7, 0, 9, 0, 4, 0, 1, 0],
       [8, 2, 0, 0, 4, 0, 0, 5, 9],
       [0, 0, 7, 0, 0, 0, 3, 0, 0],
       [4, 1, 0, 3, 8, 9, 0, 6, 2]], dtype=int64)
>>> recogn - recogn1
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> recogn - recogn2
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> recogn - recogn3
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Extracting /tmp/tensorflow\train-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\train-labels-idx1-ubyte.gz
Extracting /tmp/tensorflow\t10k-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\t10k-labels-idx1-ubyte.gz
>>> recogn
array([[0, 0, 0, 0, 8, 0, 0, 0, 4],
       [0, 0, 7, 3, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 0, 8, 3, 9],
       [8, 7, 5, 0, 3, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 7, 4, 0, 0],
       [9, 0, 0, 0, 2, 0, 0, 0, 0],
       [1, 0, 0, 6, 0, 0, 0, 5, 0],
       [0, 3, 0, 0, 0, 0, 0, 6, 0],
       [0, 2, 0, 0, 0, 5, 0, 0, 1]], dtype=int64)
>>> recogn - recogn1
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> recogn - recogn2
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> recogn - recogn3
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> cv2.imshow('jn',imB*I)
>>> cv2.imshow('jn',imB)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Extracting /tmp/tensorflow\train-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\train-labels-idx1-ubyte.gz
Extracting /tmp/tensorflow\t10k-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\t10k-labels-idx1-ubyte.gz
>>> recogn
array([[0, 2, 0, 5, 0, 1, 0, 9, 0],
       [8, 0, 0, 2, 0, 3, 0, 0, 6],
       [0, 3, 0, 0, 6, 0, 0, 7, 0],
       [0, 0, 1, 0, 0, 0, 6, 0, 0],
       [5, 4, 0, 0, 0, 0, 0, 1, 9],
       [0, 0, 2, 0, 0, 0, 7, 0, 0],
       [0, 9, 0, 0, 3, 0, 0, 8, 0],
       [2, 0, 0, 8, 0, 4, 9, 0, 7],
       [0, 1, 0, 9, 0, 7, 0, 6, 0]], dtype=int64)
>>> recogn - recogn1
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> recogn - recogn2
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> recogn - recogn3
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Extracting /tmp/tensorflow\train-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\train-labels-idx1-ubyte.gz
Extracting /tmp/tensorflow\t10k-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\t10k-labels-idx1-ubyte.gz
>>> recogn
array([[1, 7, 8, 9, 0, 4, 5, 0, 9],
       [0, 9, 6, 8, 2, 0, 3, 1, 4],
       [3, 2, 0, 1, 5, 9, 8, 0, 6],
       [2, 4, 9, 3, 0, 9, 9, 8, 0],
       [9, 0, 7, 0, 4, 8, 6, 5, 3],
       [6, 0, 3, 7, 0, 5, 1, 4, 2],
       [8, 3, 0, 5, 7, 0, 4, 6, 1],
       [7, 5, 1, 0, 6, 9, 2, 9, 0],
       [0, 6, 2, 9, 8, 1, 0, 3, 5]], dtype=int64)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Extracting /tmp/tensorflow\train-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\train-labels-idx1-ubyte.gz
Extracting /tmp/tensorflow\t10k-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\t10k-labels-idx1-ubyte.gz
>>> recogn
array([[1, 7, 8, 6, 0, 4, 5, 0, 9],
       [0, 9, 6, 8, 2, 0, 3, 1, 4],
       [3, 2, 0, 1, 5, 9, 8, 0, 6],
       [2, 4, 5, 4, 0, 9, 9, 8, 0],
       [9, 0, 7, 0, 4, 8, 6, 5, 3],
       [6, 0, 3, 7, 0, 5, 1, 4, 2],
       [8, 3, 0, 5, 7, 0, 4, 6, 1],
       [7, 5, 1, 0, 6, 3, 2, 9, 0],
       [0, 6, 2, 9, 8, 1, 0, 3, 5]], dtype=int64)
>>> recogn1
array([[1, 7, 8, 6, 0, 4, 5, 0, 9],
       [0, 9, 6, 8, 2, 0, 3, 1, 4],
       [3, 2, 0, 1, 5, 9, 8, 0, 6],
       [2, 4, 9, 3, 0, 6, 9, 8, 0],
       [9, 0, 7, 0, 4, 8, 6, 5, 3],
       [6, 0, 3, 7, 0, 5, 1, 4, 2],
       [8, 3, 0, 5, 7, 0, 4, 6, 1],
       [7, 5, 1, 0, 6, 3, 2, 9, 0],
       [0, 6, 2, 9, 8, 1, 0, 3, 5]], dtype=int64)
>>> recogn2
array([[1, 7, 8, 6, 0, 4, 5, 0, 9],
       [0, 9, 6, 8, 2, 0, 3, 1, 4],
       [3, 2, 0, 1, 5, 9, 8, 0, 6],
       [2, 4, 8, 4, 0, 9, 9, 8, 0],
       [9, 0, 7, 0, 4, 8, 6, 5, 3],
       [6, 0, 3, 7, 0, 5, 1, 4, 2],
       [8, 3, 0, 5, 7, 0, 4, 6, 1],
       [7, 5, 1, 0, 6, 3, 2, 9, 0],
       [0, 6, 2, 9, 8, 1, 0, 3, 5]], dtype=int64)
>>> recogn3
array([[1, 7, 8, 6, 0, 4, 5, 0, 9],
       [0, 9, 6, 8, 2, 0, 3, 1, 4],
       [3, 2, 0, 1, 5, 9, 8, 0, 6],
       [2, 4, 5, 4, 0, 9, 9, 8, 0],
       [9, 0, 7, 0, 4, 8, 6, 5, 3],
       [6, 0, 3, 7, 0, 5, 1, 4, 2],
       [8, 3, 0, 5, 7, 0, 4, 6, 1],
       [7, 5, 1, 0, 6, 3, 2, 9, 0],
       [0, 6, 2, 9, 8, 1, 0, 3, 5]], dtype=int64)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Extracting /tmp/tensorflow\train-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\train-labels-idx1-ubyte.gz
Extracting /tmp/tensorflow\t10k-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\t10k-labels-idx1-ubyte.gz
>>> recogn
array([[8, 1, 0, 0, 6, 0, 0, 2, 7],
       [7, 2, 0, 8, 0, 5, 0, 1, 6],
       [0, 0, 0, 7, 0, 1, 0, 0, 0],
       [0, 0, 6, 0, 3, 0, 2, 0, 0],
       [4, 0, 1, 0, 0, 0, 5, 0, 8],
       [0, 0, 7, 0, 9, 0, 1, 0, 0],
       [0, 0, 0, 3, 0, 6, 0, 0, 0],
       [3, 7, 0, 4, 0, 9, 0, 8, 1],
       [6, 4, 0, 0, 1, 0, 0, 5, 9]], dtype=int64)
>>> recogn-recogn1
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> recogn-recogn2
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> recogn-recogn3
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Extracting /tmp/tensorflow\train-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\train-labels-idx1-ubyte.gz
Extracting /tmp/tensorflow\t10k-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\t10k-labels-idx1-ubyte.gz
>>> recogn
array([[5, 6, 7, 2, 0, 3, 4, 9, 0],
       [1, 8, 0, 9, 6, 4, 5, 7, 3],
       [4, 9, 3, 8, 7, 5, 1, 2, 6],
       [3, 1, 6, 4, 8, 9, 2, 5, 7],
       [0, 5, 9, 1, 2, 6, 3, 8, 4],
       [2, 4, 8, 3, 5, 0, 9, 0, 1],
       [9, 2, 4, 6, 3, 8, 7, 1, 5],
       [6, 0, 1, 5, 4, 2, 0, 3, 9],
       [8, 3, 5, 7, 0, 1, 6, 4, 2]], dtype=int64)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Optimization Iteration:      1, Training Accuracy:  28.6%
Optimization Iteration:    101, Training Accuracy:  16.7%
Optimization Iteration:    201, Training Accuracy:   4.8%
Traceback (most recent call last):
  File "C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py", line 277, in <module>
    optimize(4000)
  File "C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py", line 104, in optimize
    session.run(optimizer, feed_dict=feed_dict_train)
  File "C:\python35\lib\site-packages\tensorflow\python\client\session.py", line 766, in run
    run_metadata_ptr)
  File "C:\python35\lib\site-packages\tensorflow\python\client\session.py", line 964, in _run
    feed_dict_string, options, run_metadata)
  File "C:\python35\lib\site-packages\tensorflow\python\client\session.py", line 1014, in _do_run
    target_list, options, run_metadata)
  File "C:\python35\lib\site-packages\tensorflow\python\client\session.py", line 1021, in _do_call
    return fn(*args)
  File "C:\python35\lib\site-packages\tensorflow\python\client\session.py", line 1003, in _run_fn
    status, run_metadata)
KeyboardInterrupt
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Optimization Iteration:      1, Training Accuracy:  16.7%
Optimization Iteration:    101, Training Accuracy:  88.1%
Optimization Iteration:    201, Training Accuracy:  92.9%
Optimization Iteration:    301, Training Accuracy: 100.0%
Optimization Iteration:    401, Training Accuracy: 100.0%
Optimization Iteration:    501, Training Accuracy: 100.0%
Optimization Iteration:    601, Training Accuracy: 100.0%
Optimization Iteration:    701, Training Accuracy: 100.0%
Optimization Iteration:    801, Training Accuracy: 100.0%
Optimization Iteration:    901, Training Accuracy: 100.0%
Optimization Iteration:   1001, Training Accuracy: 100.0%
Optimization Iteration:   1101, Training Accuracy: 100.0%
Optimization Iteration:   1201, Training Accuracy: 100.0%
Optimization Iteration:   1301, Training Accuracy: 100.0%
Optimization Iteration:   1401, Training Accuracy: 100.0%
Optimization Iteration:   1501, Training Accuracy: 100.0%
Optimization Iteration:   1601, Training Accuracy: 100.0%
Optimization Iteration:   1701, Training Accuracy: 100.0%
Optimization Iteration:   1801, Training Accuracy: 100.0%
Optimization Iteration:   1901, Training Accuracy: 100.0%
Optimization Iteration:   2001, Training Accuracy: 100.0%
Optimization Iteration:   2101, Training Accuracy: 100.0%
Optimization Iteration:   2201, Training Accuracy: 100.0%
Optimization Iteration:   2301, Training Accuracy: 100.0%
Optimization Iteration:   2401, Training Accuracy: 100.0%
Optimization Iteration:   2501, Training Accuracy: 100.0%
Optimization Iteration:   2601, Training Accuracy: 100.0%
Optimization Iteration:   2701, Training Accuracy: 100.0%
Optimization Iteration:   2801, Training Accuracy: 100.0%
Optimization Iteration:   2901, Training Accuracy: 100.0%
Optimization Iteration:   3001, Training Accuracy: 100.0%
Optimization Iteration:   3101, Training Accuracy: 100.0%
Optimization Iteration:   3201, Training Accuracy: 100.0%
Optimization Iteration:   3301, Training Accuracy: 100.0%
Optimization Iteration:   3401, Training Accuracy: 100.0%
Optimization Iteration:   3501, Training Accuracy: 100.0%
Optimization Iteration:   3601, Training Accuracy: 100.0%
Optimization Iteration:   3701, Training Accuracy: 100.0%
Optimization Iteration:   3801, Training Accuracy: 100.0%
Optimization Iteration:   3901, Training Accuracy: 100.0%
Time usage: 0:05:04
>>> recogn
array([[5, 6, 7, 2, 0, 3, 4, 9, 0],
       [1, 8, 0, 9, 6, 4, 5, 7, 3],
       [4, 9, 3, 8, 7, 5, 1, 2, 6],
       [3, 1, 6, 4, 8, 9, 2, 5, 7],
       [0, 5, 9, 1, 2, 6, 3, 8, 4],
       [2, 4, 8, 3, 5, 0, 9, 0, 1],
       [9, 2, 4, 6, 3, 8, 7, 1, 5],
       [6, 0, 1, 5, 4, 2, 0, 3, 9],
       [8, 3, 5, 7, 0, 1, 6, 4, 2]], dtype=int64)
>>> recogn - recogn1
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> recogn - recogn2
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> recogn - recogn3
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Optimization Iteration:      1, Training Accuracy:  16.7%
Traceback (most recent call last):
  File "C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py", line 277, in <module>
    optimize(4000)
  File "C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py", line 104, in optimize
    session.run(optimizer, feed_dict=feed_dict_train)
  File "C:\python35\lib\site-packages\tensorflow\python\client\session.py", line 766, in run
    run_metadata_ptr)
  File "C:\python35\lib\site-packages\tensorflow\python\client\session.py", line 964, in _run
    feed_dict_string, options, run_metadata)
  File "C:\python35\lib\site-packages\tensorflow\python\client\session.py", line 1014, in _do_run
    target_list, options, run_metadata)
  File "C:\python35\lib\site-packages\tensorflow\python\client\session.py", line 1021, in _do_call
    return fn(*args)
  File "C:\python35\lib\site-packages\tensorflow\python\client\session.py", line 1003, in _run_fn
    status, run_metadata)
KeyboardInterrupt
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Traceback (most recent call last):
  File "C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py", line 204, in <module>
    data.test.cls = np.array([label.argmax() for label in data.test.labels])
NameError: name 'data' is not defined
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Extracting /tmp/tensorflow\train-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\train-labels-idx1-ubyte.gz
Extracting /tmp/tensorflow\t10k-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\t10k-labels-idx1-ubyte.gz
>>> recogn
array([[4, 0, 0, 0, 1, 0, 0, 0, 5],
       [0, 0, 0, 9, 0, 2, 0, 0, 0],
       [0, 0, 6, 0, 7, 0, 3, 0, 0],
       [0, 5, 0, 3, 0, 4, 0, 1, 0],
       [1, 0, 8, 0, 0, 0, 6, 0, 4],
       [0, 9, 0, 7, 0, 1, 0, 8, 0],
       [0, 0, 5, 0, 4, 0, 1, 0, 0],
       [0, 0, 0, 1, 0, 9, 0, 0, 0],
       [2, 0, 0, 0, 3, 0, 0, 0, 8]], dtype=int64)
>>> recogn - recogn
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> recogn - recogn1
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> recogn - recogn2
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> recogn - recogn3
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Extracting /tmp/tensorflow\train-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\train-labels-idx1-ubyte.gz
Extracting /tmp/tensorflow\t10k-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\t10k-labels-idx1-ubyte.gz
>>> recogn
array([[1, 7, 8, 6, 0, 4, 5, 0, 9],
       [0, 9, 6, 8, 2, 0, 3, 1, 4],
       [3, 2, 0, 1, 5, 9, 8, 0, 6],
       [2, 4, 5, 3, 0, 6, 9, 5, 0],
       [9, 0, 7, 0, 4, 8, 6, 5, 3],
       [6, 0, 3, 7, 0, 5, 1, 4, 2],
       [8, 3, 0, 5, 7, 5, 4, 6, 1],
       [7, 5, 1, 0, 6, 3, 4, 9, 0],
       [0, 6, 2, 9, 8, 1, 0, 3, 5]], dtype=int64)
>>> recogn1
array([[1, 7, 8, 6, 0, 4, 5, 0, 9],
       [0, 9, 6, 8, 2, 0, 3, 1, 4],
       [3, 2, 0, 1, 5, 9, 8, 0, 6],
       [2, 4, 5, 3, 0, 6, 9, 8, 0],
       [2, 0, 7, 0, 4, 8, 6, 5, 3],
       [6, 0, 3, 7, 0, 5, 1, 4, 2],
       [8, 3, 0, 5, 7, 5, 4, 6, 1],
       [7, 5, 1, 0, 6, 3, 2, 9, 0],
       [0, 6, 2, 7, 8, 1, 0, 3, 5]], dtype=int64)
>>> recogn - recogn1
array([[ 0,  0,  0,  0,  0,  0,  0,  0,  0],
       [ 0,  0,  0,  0,  0,  0,  0,  0,  0],
       [ 0,  0,  0,  0,  0,  0,  0,  0,  0],
       [ 0,  0,  0,  0,  0,  0,  0, -3,  0],
       [ 7,  0,  0,  0,  0,  0,  0,  0,  0],
       [ 0,  0,  0,  0,  0,  0,  0,  0,  0],
       [ 0,  0,  0,  0,  0,  0,  0,  0,  0],
       [ 0,  0,  0,  0,  0,  0,  2,  0,  0],
       [ 0,  0,  0,  2,  0,  0,  0,  0,  0]], dtype=int64)
>>> recogn - recogn2
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 2, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 2, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> recogn2
array([[1, 7, 8, 6, 0, 4, 5, 0, 9],
       [0, 9, 6, 8, 2, 0, 3, 1, 4],
       [3, 2, 0, 1, 5, 9, 8, 0, 6],
       [2, 4, 3, 3, 0, 6, 9, 5, 0],
       [9, 0, 7, 0, 4, 8, 6, 5, 3],
       [6, 0, 3, 7, 0, 5, 1, 4, 2],
       [8, 3, 0, 5, 7, 5, 4, 6, 1],
       [7, 5, 1, 0, 6, 3, 2, 9, 0],
       [0, 6, 2, 9, 8, 1, 0, 3, 5]], dtype=int64)
>>> recogn3
array([[1, 7, 8, 6, 0, 4, 5, 0, 9],
       [0, 9, 6, 8, 2, 0, 3, 1, 4],
       [3, 2, 0, 1, 5, 9, 8, 0, 6],
       [2, 4, 5, 3, 0, 6, 9, 5, 0],
       [9, 0, 7, 0, 4, 8, 6, 5, 3],
       [6, 0, 3, 7, 0, 5, 1, 4, 2],
       [8, 3, 0, 5, 7, 5, 4, 6, 1],
       [7, 5, 1, 0, 6, 3, 2, 9, 0],
       [0, 6, 2, 9, 8, 1, 0, 3, 5]], dtype=int64)
>>> recogn3 - recogn
array([[ 0,  0,  0,  0,  0,  0,  0,  0,  0],
       [ 0,  0,  0,  0,  0,  0,  0,  0,  0],
       [ 0,  0,  0,  0,  0,  0,  0,  0,  0],
       [ 0,  0,  0,  0,  0,  0,  0,  0,  0],
       [ 0,  0,  0,  0,  0,  0,  0,  0,  0],
       [ 0,  0,  0,  0,  0,  0,  0,  0,  0],
       [ 0,  0,  0,  0,  0,  0,  0,  0,  0],
       [ 0,  0,  0,  0,  0,  0, -2,  0,  0],
       [ 0,  0,  0,  0,  0,  0,  0,  0,  0]], dtype=int64)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Extracting /tmp/tensorflow\train-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\train-labels-idx1-ubyte.gz
Extracting /tmp/tensorflow\t10k-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\t10k-labels-idx1-ubyte.gz
>>> recogn
array([[1, 7, 8, 9, 0, 4, 5, 0, 9],
       [0, 9, 6, 8, 2, 0, 3, 1, 4],
       [3, 2, 0, 1, 5, 9, 8, 0, 6],
       [2, 4, 5, 3, 0, 9, 9, 8, 0],
       [9, 0, 7, 0, 4, 8, 6, 5, 3],
       [6, 0, 3, 7, 0, 5, 1, 4, 2],
       [8, 3, 0, 5, 7, 0, 4, 6, 1],
       [7, 5, 1, 0, 6, 3, 2, 9, 0],
       [0, 6, 2, 9, 8, 1, 0, 3, 5]], dtype=int64)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\database.py 
>>> tab
array([ 94.,  81.,  80.,  79.,  76.,  82.,  77.,  77.,  80.,  84.])
>>> tab[8]
80.0
>>> tab[6]
77.0
>>> sum(tab)
810.0
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Extracting /tmp/tensorflow\train-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\train-labels-idx1-ubyte.gz
Extracting /tmp/tensorflow\t10k-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\t10k-labels-idx1-ubyte.gz
>>> recogn
array([[0, 2, 0, 5, 0, 1, 0, 9, 0],
       [8, 0, 0, 2, 0, 3, 0, 0, 6],
       [0, 3, 0, 0, 6, 0, 0, 7, 0],
       [0, 0, 1, 0, 0, 0, 6, 0, 0],
       [5, 4, 0, 0, 0, 0, 0, 1, 9],
       [0, 0, 2, 0, 0, 0, 7, 0, 0],
       [0, 9, 0, 0, 3, 0, 0, 8, 0],
       [2, 0, 0, 8, 0, 4, 0, 0, 7],
       [0, 1, 0, 9, 0, 7, 0, 6, 0]], dtype=int64)
>>> recogn - recogn1
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> recogn - recogn2
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> recogn - recogn3
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int64)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Extracting /tmp/tensorflow\train-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\train-labels-idx1-ubyte.gz
Extracting /tmp/tensorflow\t10k-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\t10k-labels-idx1-ubyte.gz
>>> recogn
array([[0, 2, 0, 5, 0, 1, 0, 9, 0],
       [8, 0, 0, 2, 0, 3, 0, 0, 6],
       [0, 3, 0, 0, 6, 0, 0, 7, 0],
       [0, 0, 1, 0, 0, 0, 6, 0, 0],
       [5, 4, 0, 0, 0, 0, 0, 1, 9],
       [0, 0, 2, 0, 0, 0, 7, 0, 0],
       [0, 9, 0, 0, 3, 0, 0, 8, 0],
       [2, 0, 0, 8, 0, 4, 0, 0, 7],
       [0, 1, 0, 9, 0, 7, 0, 6, 0]], dtype=int64)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Extracting /tmp/tensorflow\train-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\train-labels-idx1-ubyte.gz
Extracting /tmp/tensorflow\t10k-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\t10k-labels-idx1-ubyte.gz
>>> recogn
array([[0, 2, 3, 5, 3, 1, 0, 9, 0],
       [8, 0, 0, 2, 3, 3, 0, 0, 6],
       [0, 3, 0, 0, 6, 0, 0, 7, 0],
       [0, 0, 1, 0, 0, 0, 6, 0, 0],
       [5, 4, 0, 0, 0, 0, 0, 1, 9],
       [0, 0, 2, 0, 0, 0, 7, 0, 0],
       [0, 9, 3, 0, 3, 0, 0, 8, 0],
       [2, 0, 7, 8, 0, 4, 9, 0, 7],
       [0, 1, 9, 9, 0, 7, 0, 6, 0]], dtype=int64)
>>> recogn1
array([[0, 2, 3, 5, 3, 1, 0, 9, 0],
       [8, 0, 0, 2, 3, 3, 0, 0, 6],
       [0, 3, 0, 0, 6, 0, 0, 7, 0],
       [0, 0, 1, 0, 0, 0, 6, 0, 0],
       [5, 4, 0, 0, 0, 0, 0, 1, 9],
       [0, 0, 2, 0, 0, 0, 7, 0, 0],
       [0, 9, 3, 0, 3, 0, 0, 8, 0],
       [2, 0, 7, 8, 0, 4, 9, 0, 7],
       [0, 1, 9, 9, 0, 7, 0, 6, 0]], dtype=int64)
>>> recogn3
array([[0, 2, 3, 5, 3, 1, 0, 9, 0],
       [8, 0, 0, 2, 3, 3, 0, 0, 6],
       [0, 3, 0, 0, 6, 0, 0, 7, 0],
       [0, 0, 1, 0, 0, 0, 6, 0, 0],
       [5, 4, 0, 0, 0, 0, 0, 1, 9],
       [0, 0, 2, 0, 0, 0, 7, 0, 0],
       [0, 9, 3, 0, 3, 0, 0, 8, 0],
       [2, 0, 7, 8, 0, 4, 9, 0, 7],
       [0, 1, 9, 9, 0, 7, 0, 6, 0]], dtype=int64)
>>> recogn2
array([[0, 2, 3, 5, 3, 1, 0, 9, 0],
       [8, 0, 0, 2, 3, 3, 0, 0, 6],
       [0, 3, 0, 0, 6, 0, 0, 7, 0],
       [0, 0, 1, 0, 0, 0, 6, 0, 0],
       [5, 4, 0, 0, 0, 0, 0, 1, 9],
       [0, 0, 2, 0, 0, 0, 7, 0, 0],
       [0, 9, 3, 0, 3, 0, 0, 8, 0],
       [2, 0, 7, 8, 0, 4, 9, 0, 7],
       [0, 1, 9, 9, 0, 7, 0, 6, 0]], dtype=int64)
>>> cv2.imshow('jn',imB)
>>> 
 RESTART: C:\Users\Mohamed\Documents\2ASicom\Sudoku-robot\Firmware\mnist_model_convolutionnel.py 
Extracting /tmp/tensorflow\train-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\train-labels-idx1-ubyte.gz
Extracting /tmp/tensorflow\t10k-images-idx3-ubyte.gz
Extracting /tmp/tensorflow\t10k-labels-idx1-ubyte.gz
>>> recogn
array([[0, 2, 5, 5, 3, 1, 0, 9, 0],
       [8, 0, 0, 2, 3, 3, 0, 0, 6],
       [0, 3, 0, 0, 5, 0, 0, 7, 0],
       [0, 0, 1, 0, 0, 0, 6, 0, 0],
       [5, 4, 0, 0, 0, 0, 0, 1, 9],
       [0, 0, 2, 0, 0, 0, 7, 0, 0],
       [0, 9, 3, 0, 3, 0, 0, 8, 0],
       [2, 0, 7, 8, 0, 4, 9, 0, 7],
       [0, 1, 9, 9, 0, 7, 0, 6, 0]], dtype=int64)
>>> recogn
array([[0, 2, 5, 5, 3, 1, 0, 9, 0],
       [8, 0, 0, 2, 3, 3, 0, 0, 6],
       [0, 3, 0, 0, 5, 0, 0, 7, 0],
       [0, 0, 1, 0, 0, 0, 6, 0, 0],
       [5, 4, 0, 0, 0, 0, 0, 1, 9],
       [0, 0, 2, 0, 0, 0, 7, 0, 0],
       [0, 9, 3, 0, 3, 0, 0, 8, 0],
       [2, 0, 7, 8, 0, 4, 9, 0, 7],
       [0, 1, 9, 9, 0, 7, 0, 6, 0]], dtype=int64)
>>> recogn2
array([[0, 2, 5, 5, 3, 1, 0, 9, 0],
       [8, 0, 0, 2, 3, 3, 0, 0, 6],
       [0, 3, 0, 0, 6, 0, 0, 7, 0],
       [0, 0, 1, 0, 0, 0, 6, 0, 0],
       [5, 4, 0, 0, 0, 0, 0, 1, 9],
       [0, 0, 2, 0, 0, 0, 7, 0, 0],
       [0, 9, 3, 0, 3, 0, 0, 8, 0],
       [2, 0, 7, 8, 0, 4, 9, 0, 7],
       [0, 1, 9, 9, 0, 7, 0, 6, 0]], dtype=int64)
>>> 
