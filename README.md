# NeuralNetwork
This project displays some of the intuition I got on Neural Networks after a machine learning course. 

This one is about numbers detection on a grid.
I was unable to use libraries like numpy to take advantage of matrix operations, so basic and slow 
operations are taking place for matrix multiplications and other operations.
This sketch is meant to be run on Processing(https://processing.org/). 

How to use:
- Right clic to draw on the canvas.
- Left clic to erase your drawing. 
- Middle clic runs forward propagation.
- Typing the numbers 0-9 will train the NN on the number drawn on the canvas.

The neural network is initially working following a stochastic aproach, you need to train the neural network
one number (one training example) at a time. 

The information stored in theta1 and theta2 will be erased after stopping the program. 
There is currently no way to store these values. 

## Neural network details:
  This NN takes a 20x20 grid as input: 400 inputs. (It can be changed with the pixels variable)

  it has only one hidden layer with 25-neurons.  (It can be changed with the capaOculta variable)
  
  and also a 10 neurons output layer.  

it uses a sigmoid activation function. 
its cost function includes a regularization term. (theta^2)
