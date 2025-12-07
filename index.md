PawSense AI

[Problem](#problem--motivation) · [Technical Approach](#technical-approach-alexnet-based-classification) · [Visualizations](#visualizations) · [Results](#results) · [Takeaways](#takeaways--future-work) · [Poster & Slides](#scientific-poster--slides)

# PawSense AI: Real-Time Dog Emotion Detection

Author: Alexander Kyritsopoulos  

Florida Atlantic University  

Exploring deep learning for automated **happy vs. stressed dog** classification using AlexNet and transfer learning.

## Problem & Motivation

Traditional pet care relies on humans noticing subtle behavioral changes: pacing, lip licking, pinned ears, or avoidance. 
These signs of stress and anxiety are easy to miss until they escalate into barking, destruction, or withdrawal.

Meanwhile, consumer pet tech (cameras, smart collars, home monitors) is more common than ever, but most devices focus on:

- *Where* the dog is (location, movement),
- Not *how* the dog feels (emotional state).

PawSense AI explores whether a computer vision model can reliably distinguish **happy vs. stressed/anxious** dogs from images, 
as a first step toward real-time well-being monitoring that can plug into existing pet cameras and apps.

### Project Focus

- Computer Vision  
- Deep Learning  
- Animal Welfare & Behavior  
- AlexNet Transfer Learning  

### Core Question

Can transfer learning with AlexNet achieve good accuracy on a modest custom dataset of dog images labeled as **happy** vs. **stressed**, 
while generalizing well enough to be useful in real-world pet monitoring?

---

## Technical Approach: AlexNet-Based Classification

### Dataset

- **Classes:**  
  - Happy  
  - Stressed / anxious  
- **Source:** Custom curated dog images (personal photos + open-source images where allowed).
- **Preprocessing:**
  - Resize to 256×256, then center-crop to 224×224 pixels.
  - Normalize using ImageNet mean and standard deviation.
- **Train/Validation Split:**
  - (Example) 80% training / 20% validation, stratified by class.

### Model Architecture

- **Base model:** AlexNet pretrained on ImageNet.
- **Feature extractor:** 5 convolutional layers with ReLU activations and max pooling:
  - Conv1 → ReLU → MaxPool  
  - Conv2 → ReLU → MaxPool  
  - Conv3 → ReLU  
  - Conv4 → ReLU  
  - Conv5 → ReLU → MaxPool  
- **Classifier (modified for 2 classes):**
  - Flatten
  - Fully-connected → ReLU → Dropout
  - Fully-connected → ReLU → Dropout
  - Output layer with 2 units (happy, stressed) + softmax probabilities

Early convolutional layers can be mostly **frozen** (or trained with a smaller learning rate), 
while the classifier layers are fine-tuned on the dog emotion dataset.

### Training Setup

- **Loss function:** Cross-entropy loss
- **Optimizer:** (e.g.) Adam or SGD with momentum
- **Learning rate:** (e.g.) 1e-4 to 1e-3 for fine-tuning
- **Batch size:** (e.g.) 32
- **Epochs:** Trained for *N* epochs with early stopping based on validation loss
- **Regularization:**
  - Dropout in the classifier
  - Data augmentation (random flips, small rotations)

Experiments are run in **Google Colab** with GPU acceleration, and metrics/plots are logged from within the notebook.

---

## Visualizations

Below are example plots and artifacts from the Colab experiments.

> ⚠️ After you upload images into `docs/images/`, update the filenames below to match.

![Training Accuracy Curve](images/train_val_acc.png)  
*Figure 1. Training accuracy over epochs.*

![Validation Accuracy Curve](images/val_acc.png)  
*Figure 2. Validation accuracy over epochs, showing how well the model generalizes.*

![Confusion Matrix](images/confusion_matrix.png)  
*Figure 3. Confusion matrix on the validation set for "happy" vs. "stressed" classes.*

![Sample Predictions](images/sample_predictions.png)  
*Figure 4. Example model predictions on held-out images.*

---

## Results

Key findings from the experiments include:

- Fine-tuned pretrained AlexNet reaches about **[fill in]%** validation accuracy.  
- A version with more frozen layers performs slightly worse, around **[fill in]%**, showing the benefit of fine-tuning.  
- Training AlexNet from scratch performs noticeably worse (around **[fill in]%**), highlighting the importance of transfer learning on a small dataset.  
- Confusion matrices show that most predictions fall along the diagonal (correct class), with misclassifications usually occurring on blurry or ambiguous images.

You can replace the placeholder percentages above with your actual results from Colab or Weights & Biases.

---

## Takeaways & Future Work

- **Transfer learning is essential:** Using a pretrained AlexNet drastically improves performance compared to training from scratch.
- **Data quality & balance matter:** Misclassifications often happen when:
  - Images are low quality (motion blur, poor lighting), or  
  - Labels are ambiguous (mild stress vs. neutral).
- **Good starting point for real-time systems:** A lightweight CNN like AlexNet can run efficiently enough to be integrated into pet camera pipelines.
- **Future directions:**
  - Expand from binary "happy vs. stressed" to more nuanced emotional states (relaxed, playful, fearful, etc.).
  - Move from static images to short video clips to capture temporal cues (tail wagging, pacing).
  - Test deployment on edge devices (Raspberry Pi + camera) for real-time monitoring.

---

## Scientific Poster & Slides

This website is part of a larger project deliverable that also includes a research-style poster and a narrated slide presentation.

- Scientific Poster: [View poster](https://example.com)  <!-- Replace with real link -->
- Slide Deck: [View presentation slides](https://example.com)  <!-- Replace with real link -->

PawSense AI · GitHub Pages Project · 2025 · Alexander Kyritsopoulos
