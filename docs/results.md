# Visualizations & Results

This section reviews the model’s performance using the default hyperparameters:

- **Optimizer:** Adam  
- **Pretrained:** True  
- **Learning Rate:** 1e-4  
- **Batch Size:** 32  
- **Device:** GPU (CUDA)  

All experiments shown below modify **only one parameter at a time**, allowing clear comparison of how each hyperparameter affects model performance.

---

## 🟦 Training Accuracy

![Training Accuracy](assets/train_acc.png)

Training accuracy climbs rapidly for all runs and reaches **~98–100%** within a few epochs.

### Key Points
- The **default configuration (Adam + GPU + RGB + LR=1e-4)** learns extremely quickly.  
- Switching to **CPU** or **SGD** slows convergence and slightly lowers final accuracy.  
- **Grayscale** models consistently learn slower and plateau lower.  
- **CUDA** provides the smoothest and fastest optimization trajectory.

### Interpretation  
AlexNet is highly effective at learning emotional cues in dog images. The default configuration is near optimal for training efficiency and stability.

---

## 🟥 Validation Accuracy

![Validation Accuracy](assets/val_acc.png)

Validation accuracy remains high across all experimental variations, typically **90–96%**.

### Key Points
- **GPU + RGB + Adam (default)** produces the highest and most stable validation accuracy.  
- **CPU** runs maintain competitive accuracy but show more noise.  
- **SGD** and **grayscale** negatively impact consistency and peak values.  
- Lower learning rate (1e-4, default) is noticeably more stable than higher LR settings.

### Interpretation  
The model generalizes very well. The differences between runs reveal that optimizer choice, color mode, and device speed materially influence generalization quality.

---

## 🟩 Validation Loss

![Validation Loss](assets/val_loss.png)

Validation loss trends downward for the highest-performing runs.

### Key Points
- The **default configuration** shows the lowest and smoothest validation loss.  
- **SGD** introduces instability and larger loss spikes.  
- **Grayscale** inputs cause higher variance and slower reduction in validation loss.  
- Higher LR results in increased fluctuation and slightly worse generalization.

### Interpretation  
Good generalization with minimal overfitting. The experiments confirm that stable optimization (Adam) and rich input information (RGB) significantly improve emotional classification.

---

## 🟪 Hyperparameter Comparison (Best Validation Accuracy)

![Best Validation Accuracy](assets/best_val_acc.png)

This comparison plot highlights how modifying a single parameter impacts peak validation accuracy.

### Key Findings
- **Device:** GPU > CPU  
- **Color Mode:** RGB > Grayscale  
- **Optimizer:** Adam > SGD  
- **Learning Rate:** 1e-4 (default) > 1e-3  
- **Batch Size:** Smaller batch sizes slightly improve accuracy, but differences are minor.

### Interpretation  
The default configuration is nearly optimal. Results confirm that **compute speed, image richness, and optimizer choice** meaningfully affect model performance.

---

## 🟦 Confusion Matrix

![Confusion Matrix](assets/confusion_matrix.png)

### Breakdown
- Class 0: **37 correct**, **3 incorrect**  
- Class 1: **38 correct**, **2 incorrect**  

### Interpretation
- Balanced, high performance across both classes.  
- Only **5 misclassifications** out of 80 predictions.  
- No class bias or imbalance issues.  
- Errors likely stem from ambiguous or borderline emotional expressions.

---

# ⭐ Overall Results Summary

The AlexNet-based classifier performs exceptionally well on dog emotion recognition. Using the default configuration (Adam, LR=1e-4, pretrained weights, batch size 32, GPU), the model achieves:

- **Near-perfect training accuracy**  
- **94–96% validation accuracy**  
- **Consistently low validation loss**  
- **Very strong classification balance (confusion matrix)**  

Experimentation confirms:

- **Adam > SGD**  
- **RGB > Grayscale**  
- **GPU > CPU**  
- **Low LR > High LR in stability and generalization**  

These results demonstrate that AlexNet effectively captures emotional cues in dog images and provides a strong foundation for future real-time or multi-label emotion detection systems.

---
