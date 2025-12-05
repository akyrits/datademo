[Problem](#problem--motivation) • 
[Approach](#technical-approach-alexnet-based-classification) • 
[Visualizations](#visualizations) • 
[Results](#results) • 
[Takeaways](#takeaways--future-work) • 
[Links](#links)

---

# PawSense AI: Real-Time Dog Emotion Detection

**Author:** Alexander Kyritsopoulos  
**Course:** Data Science / Deep Learning Project  

Exploring whether transfer learning with AlexNet can reliably detect dog emotional states
(happy vs. stressed) from images, as a first step toward real-time well-being monitoring.

---

## Problem & Motivation

Modern pet parents care deeply about their dog’s emotional health, but stress and anxiety
are often missed until they show up as problem behaviors (barking, growling, biting) or
health issues.

**Challenges with the current situation**

- Humans are not great at spotting subtle stress signals like whale eye, ear position,
  or tension around the muzzle.
- Many owners are busy or away from home, so they miss early warning signs.
- Existing smart cameras focus on **activity** (motion, barking) rather than **emotion**.

**Goal of PawSense AI**

Build a computer-vision system that can:

- Detect whether a dog looks **relaxed/happy vs. stressed/anxious** from images.
- Show that deep learning can capture subtle visual cues in ears, eyes, and posture.
- Lay the groundwork for real-time alerts and insights (e.g., “your dog looks stressed”).

---

## Technical Approach: AlexNet-Based Classification

### Dataset

- Two main classes for this stage: **Happy/Relaxed** vs **Stressed/Anxious**.
- Images collected from curated online sources and filtered for clear facial/body cues.
- Preprocessing:
  - Resize to **224×224** pixels.
  - Normalize using **ImageNet statistics**.
  - Split into **training**, **validation**, and **test** sets.

### Model Architecture

- Base model: **AlexNet**, pretrained on ImageNet.
- Final fully connected layer modified for **2-class output** (happy vs. stressed).
- ReLU activations, dropout, and softmax output layer for class probabilities.

### Default Training Setup

These are the default hyperparameters used unless explicitly changed in an experiment:

- **Optimizer:** Adam  
- **Pretrained:** True  
- **Learning Rate:** 1e-4  
- **Batch Size:** 32  
- **Device:** GPU (CUDA)  
- **Loss:** Cross-entropy  
- **Epochs:** ~10–14 (early stopping based on validation performance)

### Experiments

Each experiment in the run list changes **only one parameter at a time**, keeping all others
at their default values above. Examples:

- Device: GPU vs. CPU
- Color mode: RGB vs. grayscale
- Optimizer: Adam vs. SGD
- Learning rate: 1e-4 vs. 1e-3
- Batch size: 16 vs. 32

Metrics and plots were logged with **Weights & Biases (W&B)**.

---

## Visualizations

### Training Accuracy (Top Runs)

![Training Accuracy](assets/train_acc.png)

- All runs reach high training accuracy.
- The **default configuration (GPU + RGB + Adam + LR=1e-4)** converges the fastest and most smoothly.
- Grayscale and SGD tend to learn more slowly and plateau slightly lower.

### Validation Accuracy

![Validation Accuracy](assets/val_acc.png)

- Validation accuracy stays in the **90–96%** range for the best runs.
- GPU + RGB + Adam (default) gives the most stable performance.
- CPU, grayscale, and SGD introduce more noise and slightly lower peak accuracy.

### Validation Loss

![Validation Loss](assets/val_loss.png)

- The default configuration shows the lowest and smoothest validation loss.
- SGD and grayscale introduce higher variance and occasional spikes.
- Lower learning rate (1e-4) is more stable than higher LR settings.

### Hyperparameter Comparison (Best Validation Accuracy)

![Best Validation Accuracy](assets/best_val_acc.png)

- **Device:** GPU > CPU  
- **Color Mode:** RGB > Grayscale  
- **Optimizer:** Adam > SGD  
- **Learning Rate:** 1e-4 (default) > 1e-3  

---

## Results

Overall, the AlexNet-based classifier performs strongly on this dataset:

- Best models achieve **~94–96% validation accuracy**.
- Validation loss remains low and closely follows training loss, indicating good generalization.
- Transfer learning (pretrained AlexNet) is crucial; it provides strong features out of the box.

From the confusion matrix:

![Confusion Matrix](assets/confusion_matrix.png)

- Class 0: **37 correct**, **3 incorrect**  
- Class 1: **38 correct**, **2 incorrect**  
- Only **5 misclassifications** out of 80 predictions, with no major class bias.

---

## Takeaways & Future Work

### Key Takeaways

- AlexNet with transfer learning is **effective** for dog emotion classification on this dataset.
- The model can learn meaningful features from ears, eyes, and facial tension to distinguish
  happy vs. stressed states.
- Small experimental changes (optimizer, color mode, LR) can noticeably impact stability and
  performance.

### Future Directions

- Move from simple “happy vs. stressed” to **multi-label cues** (ears back, whale eye, lip licking).
- Expand the dataset to include more breeds, lighting conditions, and real-world home environments.
- Integrate with **live video or smart cameras** for real-time monitoring and alerts.
- Explore lighter architectures (e.g., MobileNet, EfficientNet) for deployment on edge devices.

---

## Links

- **GitHub Repository:**  
  <https://github.com/akyrits/datademo>

- **GitHub Pages Site:**  
  <https://akyrits.github.io/datademo/>

- **Detailed Visualizations & Commentary:**  
  [Full Results Page](results.html)

- **Colab Notebook (training AlexNet):**  
  <https://colab.research.google.com/drive/1k5iSNhCEPMepvmNki9NIEJMuPeM5QtcU?usp=sharing>

