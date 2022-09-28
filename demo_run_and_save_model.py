from demo_model import *

import torch

train_and_test_model()

torch.save(model.state_dict(), "model.pth")
print("Saved PyTorch Model State to model.pth")
