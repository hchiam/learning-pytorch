# Learning [PyTorch](https://pytorch.org/)

Just one of the things I'm learning. https://github.com/hchiam/learning

"PyTorch in 100 seconds": https://www.youtube.com/watch?v=ORMx45xqWkA

https://pytorch.org

https://pytorch.org/get-started/locally --> this website automatically suggests how to install locally

https://github.com/pytorch/examples --> example PyTorch code for quick starts, e.g. [Image classification (MNIST) using Convnets](https://github.com/pytorch/examples/tree/main/mnist), [Training Imagenet Classifiers with Popular Networks](https://github.com/pytorch/examples/tree/main/imagenet), [DCGAN](https://github.com/pytorch/examples/blob/main/dcgan/README.md), [VAE](https://github.com/pytorch/examples/tree/main/vae), [RL](https://github.com/pytorch/examples/tree/main/reinforcement_learning), [time sequence prediction](https://github.com/pytorch/examples/tree/main/time_sequence_prediction), [translation](https://github.com/pytorch/examples/tree/main/language_translation), and much more

e.g.:

```sh
conda install pytorch torchvision -c pytorch
```

or I think I prefer this:

```sh
pip3 install torch torchvision
```

or minimally just:

```sh
pip3 install torch
```

There's much more in the docs, but here's a sample of some interesting pages:

- recipes: https://pytorch.org/tutorials/recipes/recipes_index.html
  - neural network: https://pytorch.org/tutorials/recipes/recipes/defining_a_neural_network.html
  - saving/loading/using models: https://pytorch.org/tutorials/recipes/recipes/saving_and_loading_models_for_inference.html
- tutorials: https://pytorch.org/tutorials
  - quickstart tutorial: https://pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html (python code to download open datasets, create models, set model params, save model, and load model for use)
- mobile deployment: https://pytorch.org/get-started/mobile

## Demo

```sh
# creates model.pth:
python3 demo_run_save_model.py

# and now model.pth can be used by:
python3 demo_use_model.py
```

## Running PyTorch from C# or .Net

- As a subprocess (_I think this is easier_): https://stackoverflow.com/a/11779234

- Directly coding in C# as a library: https://github.com/dotnet/TorchSharp

  - Here are some examples of using TorchSharp: https://github.com/dotnet/TorchSharpExamples/tree/main/src/CSharp/CSharpExamples

## Stable Diffusion Colab

https://colab.research.google.com/drive/1roZqqhsdpCXZr8kgV_Bx_ABVBPgea3lX

## PyTorch Cheat Sheets

https://www.datacamp.com/cheat-sheet/deep-learning-with-py-torch

https://pytorch.org/tutorials/beginner/ptcheat.html

## Suggestions on how to learn PyTorch

https://www.datacamp.com/blog/how-to-learn-pytorch
