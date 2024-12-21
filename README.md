# NeuralNetwork
numbers detection on a 20x20 grid.
running the sketch on Processing should display the canvas. 
I was unable to use libraries like numpy to take advantage of matrix operations, so basic and slow 
operations are taking place for matrix multiplication.

- right clic to draw on the canvas.
- left clic to erase your drawing. 
- middle clic runs forward propagation.
- typing the numbers 0-9 train the N-N on the number written.

the neural network is initially working based on a stochastic aproach, you need to train the neural network
one number (one training example) at a time. 

The information stored in theta1 and theta2 will be erased after stopping the program. 
