# A robot that solves and fills alone a sudoku's puzzles !
<p align="center">
<img src="https://github.com/Sanahm/Sudoku-robot/blob/master/Ressources/Rapport%20final/pp.jpg" width="400" height="400"/>
</p>

Sudoku are digital puzzles that computers can solve automatically because they obey some simple mathematical rules.
<p align="center">
<img src="https://upload.wikimedia.org/wikipedia/commons/f/ff/Sudoku-by-L2G-20050714.svg" width="250" height="250"/>
<img src="https://upload.wikimedia.org/wikipedia/commons/3/31/Sudoku-by-L2G-20050714_solution.svg" width="250" height="250"/>
</p>
The main objective of this project was to build a rudimentary and autonomous robot,like plotting table, which will be able to:

1. analyze the grid of sudoku to be filled
2. solve the Sudoku problem
3. fill the grid

That means the robot must be able to process the grid to be solved in order to detect the boxes already filled,their values and then proceed to filling.

# How it works?

The hardware of the robot consist at using  a Raspberry pi 3 with a camera. A photo of the grid is taken at the beginning of the process.
<p align="center">
<img src="https://github.com/Sanahm/Sudoku-robot/blob/master/Ressources/Rapport%20final/b2.PNG" width="250" height="250"/>
<img src="https://github.com/Sanahm/Sudoku-robot/blob/master/Ressources/Rapport%20final/b4.PNG" width="250" height="250"/>
<img src="https://github.com/Sanahm/Sudoku-robot/blob/master/Ressources/Rapport%20final/b8.PNG" width="250" height="250"/>
</p>

The photo is then pre-processed using image processing methods to suppress artefacts, detect rotation and angle therefore (the puzzle can be solved whatever his position on the table). After that the image is redressed to obtain a picture focused only on the grid.

Once the sudoku grid obtained, we segment the picture to extract each box and proceed to image recognition using [a neural network](https://en.wikipedia.org/wiki/Artificial_neural_network). For that we used Tensorflow framework developed by Google for machine learning. At the end of this process we have a numerical representation of our grid which can then be solved.

Once solved, the raspberry pi is again used to control the motors of the robot in order to fill the grid. 

To sum up,
<p align="center">
<img src="https://github.com/Sanahm/Sudoku-robot/blob/master/Ressources/Rapport%20final/reco.PNG" />
</p>

**The result**
<p align="center">
<img src="https://media.giphy.com/media/xUOrw6IZKuRlDwsteE/200.gif" width="300" height="300"/>
</p>

link to youtube video (https://www.youtube.com/watch?v=cQKQf74-gNk)

**Required skills**

- computer vision
- Images processing
- Programming skills
- Electronic
- Mechanical

**useful tools and API**

- python
- [tensorflow](tensorflow.org) for neural network
- [opencv](http://opencv.org/) for image processing

# References

https://en.wikipedia.org/wiki/Sudoku
A detailled report of this project can be found in ressources directory.

for more information about the project don't hesitate to contact us
