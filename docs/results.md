---
title: Visualizations & Results
---

# Visualizations, Results, & Takeaways

## Training & Validation Curves

![Training vs Validation Accuracy](assets/accuracy_curve.png)

- Training accuracy trend: (Describe your curve – e.g., steadily increases then plateaus.)
- Validation accuracy trend: (Describe if it follows training accuracy or diverges.)
- Signs of overfitting: (Note if training keeps improving while validation flattens or drops.)

![Training vs Validation Loss](assets/loss_curve.png)

- Loss decreases over epochs, showing that the model is learning.
- Mention any instability (spikes) or early plateau.

## Confusion Matrix

![Confusion Matrix](assets/confusion_matrix.png)

Interpretation ideas:

- Where does the model perform well?
- Are **happy** dogs mostly predicted correctly?
- Are **sad/stressed** dogs sometimes misclassified as happy or neutral?

## Sample Predictions

![Sample Predictions](assets/sample_predictions.png)

You can highlight:

- Correct predictions on clear, well-lit images.
- Interesting failure cases:
  - Backlit dogs
  - Unusual poses
  - Occlusions or poor image quality

## Key Takeaways

- **Feasibility:** AlexNet can learn meaningful features related to dog emotional state from images.
- **Performance:** (Briefly summarize your best accuracy / metrics here.)
- **Limitations:**
  - Dataset size and potential label noise.
  - Limited diversity in breeds, lighting conditions, and camera angles.
- **Future directions:**
  - Collect more and better-labeled data.
  - Support **multi-label** outputs (e.g., ear position, mouth tension, tail position separately).
  - Extend to **video** and real-time inference.

## Practical Impact

Even at this early stage, this project shows that:

- Deep learning can assist humans in reading dog body language.
- A future app could help owners **notice stress earlier**, improving welfare.
- There is potential for integration with **shelter monitoring**, **veterinary care**, and **smart home devices** for dogs.

