# Training a Convolutional Neural Network and Explaining its Predictions via Vanilla Gradient and LRP Methods (advanced)

The Network is trained on the CIFAR-10 dataset and explained its predictions in terms of input variables using Gradient X Input and LRP.

## Part 1: Training the Convolutional Network

To understand this code you need to understand the CIFAR-10 tutorial which is available at

https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html

## Part 2: Explaining the Model's Predictions

Once the model has been learned, we would like to explore in more detail which input features the model uses to support the evidence it has found for the correct class. To test the different explanation methods, we will consider a small subset of 15 data points from the test set.
