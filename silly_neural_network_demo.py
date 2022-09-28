#  https://pytorch.org/tutorials/recipes/recipes/defining_a_neural_network.html

import torch
import torch.nn as nn
import torch.nn.functional as F


class Net(nn.Module):
    """
    https://pytorch.org/tutorials/recipes/recipes/defining_a_neural_network.html
    """

    def __init__(self):
        super(Net, self).__init__()

        # First 2D convolutional layer, taking in 1 input channel (image),
        # outputting 32 convolutional features, with a square kernel size of 3
        self.conv1 = nn.Conv2d(1, 32, 3, 1)

        # Second 2D convolutional layer, taking in the 32 input layers,
        # outputting 64 convolutional features, with a square kernel size of 3
        self.conv2 = nn.Conv2d(32, 64, 3, 1)

        # Designed to ensure that adjacent pixels are either all 0s or all active
        # with an input probability of 0.25 or 0.5
        self.dropout1 = nn.Dropout2d(0.25)
        self.dropout2 = nn.Dropout2d(0.5)

        # First fully connected layer
        self.fc1 = nn.Linear(9216, 128)

        # Second fully connected layer that outputs our 10 labels
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        """
        x represents our data
        """

        # Pass data through conv1
        x = self.conv1(x)

        # Use the rectified-linear activation function over x
        x = F.relu(x)

        # (repeat)
        x = self.conv2(x)
        x = F.relu(x)

        # Run max pooling over x
        x = F.max_pool2d(x, 2)

        # Pass data through dropout1
        x = self.dropout1(x)

        # Flatten x with start_dim=1
        x = torch.flatten(x, 1)

        # Pass data through fc1
        x = self.fc1(x)

        # (repeat more stuff)
        x = F.relu(x)
        x = self.dropout2(x)
        x = self.fc2(x)

        # Apply softmax to x
        output = F.log_softmax(x, dim=1)

        return output


my_nn = Net()
# print(my_nn) # specs

random_28x28_image = torch.rand((1, 1, 28, 28))

tensor = my_nn(random_28x28_image)
print(tensor)
