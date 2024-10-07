# SRGAN - Super-Resolution using Generative Adversarial Networks

This project implements **SRGAN (Super-Resolution GAN)** using PyTorch, a deep learning model that takes **low-resolution (LR)** images and generates corresponding **high-resolution (HR)** images. The SRGAN is based on the paper "Photo-Realistic Single Image Super-Resolution Using a Generative Adversarial Network" by Christian Ledig et al (https://arxiv.org/abs/1609.04802).

I have tried to recreate the network architecture as mentioned in the paper but with minor changes:
![image](https://github.com/user-attachments/assets/333c8747-4bda-4f85-a027-e5b631adb9c7)




## Introduction

Super-Resolution GAN (SRGAN) is a state-of-the-art model for generating **high-resolution images** from **low-resolution inputs**. The GAN framework consists of two networks: the **generator** and the **discriminator**. The generator attempts to generate realistic HR images, while the discriminator tries to differentiate between real HR images and generated HR images.

This project is implemented using **PyTorch** and includes the following key components:

- **Generator Network**: Upsamples LR images to HR images.
- **Discriminator Network**: Classifies real and generated HR images.
- **Loss Functions**: Adversarial loss (GAN), pixel-wise loss (MSE), and perceptual loss (VGG loss).

## Model Architecture

### Generator

The generator uses **residual blocks** with skip connections to preserve image features and upsample LR images. It uses **PixelShuffle** for upscaling to achieve a 4x resolution enhancement (e.g., `64x64` LR to `256x256` HR).

### Discriminator

The discriminator is a binary classifier that distinguishes between real and generated HR images. It consists of convolutional layers with increasing depth, followed by fully connected layers, and outputs a probability (real/fake).

## Installation

To run this project, you need to have the following libraries installed:

- **Python 3.7+**
- **PyTorch**
- **Torchvision**
- **Pillow**
- **Matplotlib**
- **numpy**

You can install the required dependencies using `pip`:

```bash
pip install torch torchvision pillow matplotlib numpy

```

## Dataset
The Dataset has been downloaded from Div2K High Resolution Images (https://www.kaggle.com/datasets/soumikrakshit/div2k-high-resolution-images/data)
This project uses a dataset of high-resolution images. You need two sets of images:

 - **High-Resolution (HR) Images**: Original high-resolution images obtained from the dataset.
 - **Low-Resolution (LR) Images**: Downscaled versions of HR images. 
The dataset only has High-Resolution images and to obtain the Low-Resolution images run the down_scale.py file. This will downscale the image by a given factor (4 in my case).

You can use any image dataset of your choice. In this project, LR images are resized to 64x64 and HR images to 256x256 to save time and compute.

Place the training images in the following directories:
 - train_LR/: Low-resolution images (e.g., 64x64)
 - train_HR/: High-resolution images (e.g., 256x256)

Place the validation images in the following directories:
 - val_LR/: Low-resolution validation images
 - val_HR/: High-resolution validation images

## Training Process
 - The generator is trained to minimize pixel-wise loss (MSE) and fool the discriminator.
 - The discriminator is trained to distinguish between real and fake HR images.
 - The VGG loss (perceptual loss) ensures that the generated images look realistic by matching high-level features between real and generated images.

## Evaluation
This will generate super-resolution (SR) images from the validation LR images and display/save them alongside the original HR images.

The script outputs the following images for comparison:

 - Low-Resolution (LR) Image
 - Generated Super-Resolution (SR) Image
 - Original High-Resolution (HR) Image

I have saved my result in the Eval folder.


