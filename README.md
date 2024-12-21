# NeuralNetwork
this project displays some of the intuition I got on Neural Networks after a machine learning course. 

This one is about numbers detection on a 20x20 grid.
Running the sketch on Processing should display the canvas. 
I was unable to use libraries like numpy to take advantage of matrix operations, so basic and slow 
operations are taking place for matrix multiplications and other operations.

How to use:
- Right clic to draw on the canvas.
- Left clic to erase your drawing. 
- Middle clic runs forward propagation.
- Typing the numbers 0-9 train the N-N on the number drawn on the canvas.

The neural network is initially working based on a stochastic aproach, you need to train the neural network
one number (one training example) at a time. 

The information stored in theta1 and theta2 will be erased after stopping the program. 
there is currently no way to store these values. 

## Neural network details:
  This NN takes a 20x20 grid as input: 400 inputs.

  it has only one 25-neurons hidden layer.  
  
  and also a 10 neurons output layer.  

it uses a sigmoid activation function. 
its cost function includes a regularization term. (theta^2)
