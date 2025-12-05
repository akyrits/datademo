---
title: Technical Approach – AlexNet
---

# Technical Approach: AlexNet

## Model Choice

I use **AlexNet**, a convolutional neural network with:

- Multiple **convolutional layers** + ReLU activations
- **Max pooling** layers for downsampling
- **Fully connected** layers at the end
- A final **softmax** layer for class probabilities

Instead of training from scratch, I **fine-tuned a pretrained AlexNet** (originally trained on ImageNet) to recognize emotional states from dog images.

## Dataset & Labels

The repository includes my dataset folders such as:

- `stage1_happy_vs_sad/` – images of dogs labeled as **happy** or **sad/neutral**.
- `dataset/` – supporting images and structure.

Images are labeled based on visible cues like:

- Mouth position and facial tension
- Ear position
- General posture and expression

## Preprocessing & Input Size

Typical preprocessing steps:

- Resize images to **224 × 224** pixels.
- Convert to tensors and **normalize** using ImageNet mean and standard deviation.
- Apply **data augmentation** (e.g., random horizontal flips, small rotations) to help generalization.

These match AlexNet’s expected input format.

## Training Configuration

Key training details (fill in with your actual values):

- **Loss function:** Cross-entropy
- **Optimizer:** (e.g.) Adam or SGD with momentum
- **Learning rate:** (e.g.) 1e-4
- **Batch size:** (e.g.) 32
- **Epochs:** (e.g.) 10–30, with early stopping based on validation loss
- **Metrics:** Training & validation accuracy, confusion matrix

## AlexNet Architecture Summary

Layer-by-layer overview:

1. **Convolution + ReLU + MaxPool** – capture low-level features (edges, textures).
2. **Deeper Conv layers + ReLU + Pooling** – capture more complex shapes (eyes, ears, muzzle shapes).
3. **Flatten → Fully Connected layers** – combine all features into global patterns.
4. **Output layer** – predicts the probability of each emotional class (e.g. Happy vs Sad).

## Why AlexNet Works for This Problem

- Pretraining on ImageNet gives strong **general visual features**.
- Fine-tuning allows the model to specialize on **canine emotion cues**.
- The architecture is relatively **lightweight** and straightforward to train in Colab.

See the [Visualizations, Results, & Takeaways](results.md) page for training curves and example results.
