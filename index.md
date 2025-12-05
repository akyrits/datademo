<link rel="stylesheet" href="style.css">

<nav>
  <a href="#problem">Problem</a>
  <a href="#approach">Approach</a>
  <a href="#visualizations">Visualizations</a>
  <a href="#results">Results</a>
  <a href="#takeaways">Takeaways</a>
  <a href="results.html">Full Results Page</a>
</nav>

<section id="title">
<h1>PawSense AI: Real-Time Dog Emotion Detection</h1>
<p><strong>Author:</strong> Alexander Kyritsopoulos<br>
<strong>Course:</strong> Data Science / Deep Learning Project</p>

<p>Exploring whether transfer learning with AlexNet can reliably detect dog emotional states
(happy vs. stressed) from images, as a first step toward real-time well-being monitoring.</p>
</section>

<section id="problem">
<h2>Problem & Motivation</h2>

<p>Modern pet parents care deeply about their dog’s emotional health, but stress and anxiety
are often missed until they show up as problem behaviors (barking, growling, biting) or
health issues.</p>

<h3>Challenges</h3>
<ul>
  <li>Humans are not great at spotting subtle stress signals like whale eye, ear position, or tension around the muzzle.</li>
  <li>Owners may miss early signs, especially when away from home.</li>
  <li>Existing smart cameras track <em>activity</em>, not <em>emotion</em>.</li>
</ul>

<h3>Goal of PawSense AI</h3>
<ul>
  <li>Detect whether a dog looks <strong>relaxed/happy</strong> vs. <strong>stressed/anxious</strong>.</li>
  <li>Show that deep learning can capture subtle emotional cues.</li>
  <li>Serve as a foundation for real-time emotion alerts and behavioral insights.</li>
</ul>
</section>

<section id="approach">
<h2>Technical Approach: AlexNet-Based Classification</h2>

<h3>Dataset</h3>
<ul>
  <li>Two classes: <strong>Happy/Relaxed</strong> vs <strong>Stressed/Anxious</strong>.</li>
  <li>Images curated for clear facial/body cues.</li>
  <li>Preprocessing: resize to 224×224, normalize using ImageNet statistics, split into train/val/test.</li>
</ul>

<h3>Model Architecture</h3>
<ul>
  <li>Base model: <strong>AlexNet pretrained on ImageNet</strong>.</li>
  <li>Final FC layer modified for 2-class output.</li>
  <li>ReLU activations, dropout, and softmax classifier.</li>
</ul>

<h3>Default Training Hyperparameters</h3>
<ul>
  <li><strong>Optimizer:</strong> Adam</li>
  <li><strong>Pretrained:</strong> True</li>
  <li><strong>Learning Rate:</strong> 1e-4</li>
  <li><strong>Batch Size:</strong> 32</li>
  <li><strong>Device:</strong> GPU (CUDA)</li>
  <li><strong>Loss:</strong> Cross-entropy</li>
  <li><strong>Epochs:</strong> ~10–14 with early stopping</li>
</ul>

<h3>Experimental Design</h3>
<p>Each experiment changed <strong>one parameter at a time</strong>, keeping all other defaults constant.  
This allows clean, interpretable comparisons.</p>

<p>Examples:</p>
<ul>
  <li>Device: GPU vs CPU</li>
  <li>Color mode: RGB vs grayscale</li>
  <li>Optimizer: Adam vs SGD</li>
  <li>Learning rate: 1e-4 vs 1e-3</li>
  <li>Batch size: 16 vs 32</li>
</ul>

<p>All training curves and metrics were logged using <strong>Weights & Biases (W&B)</strong>.</p>
</section>

<section id="visualizations">
<h2>Visualizations</h2>

<h3>Training Accuracy (Top Runs)</h3>
<img src="assets/train_acc.png" alt="Training Accuracy">

<ul>
  <li>All runs reach high accuracy quickly.</li>
  <li>The default configuration (GPU + RGB + Adam + LR=1e-4) converges the fastest.</li>
  <li>Grayscale and SGD learn slower and plateau lower.</li>
</ul>

<h3>Validation Accuracy</h3>
<img src="assets/val_acc.png" alt="Validation Accuracy">

<ul>
  <li>Most models reach 90–96% validation accuracy.</li>
  <li>GPU + RGB + Adam (default) is the most stable.</li>
  <li>SGD and grayscale introduce greater variance.</li>
</ul>

<h3>Validation Loss</h3>
<img src="assets/val_loss.png" alt="Validation Loss">

<ul>
  <li>The default configuration shows the lowest and smoothest loss curve.</li>
  <li>SGD and grayscale cause fluctuations and slower reduction.</li>
  <li>Lower learning rate (1e-4) performs more consistently.</li>
</ul>

<h3>Best Validation Accuracy by Hyperparameter</h3>
<img src="assets/best_val_acc.png" alt="Best Val Acc">

<ul>
  <li><strong>GPU > CPU</strong></li>
  <li><strong>RGB > Grayscale</strong></li>
  <li><strong>Adam > SGD</strong></li>
  <li><strong>LR 1e-4 > LR 1e-3</strong></li>
</ul>
</section>

<section id="results">
<h2>Results</h2>

<p>The AlexNet-based classifier performed strongly across all metrics.  
Using the default configuration, the model achieved:</p>

<ul>
  <li><strong>94–96% validation accuracy</strong></li>
  <li><strong>Low, stable validation loss</strong></li>
  <li><strong>Fast convergence and minimal overfitting</strong></li>
</ul>

<h3>Confusion Matrix</h3>
<img src="assets/confusion_matrix.png" alt="Confusion Matrix">

<ul>
  <li>Class 0: 37 correct, 3 incorrect</li>
  <li>Class 1: 38 correct, 2 incorrect</li>
  <li>Only <strong>5 misclassifications</strong> across 80 samples</li>
  <li>No major class imbalance or bias</li>
</ul>

<p>These results show that transfer learning with AlexNet is an effective baseline for dog emotion recognition.</p>
</section>

<section id="takeaways">
<h2>Takeaways & Future Work</h2>

<h3>Key Takeaways</h3>
<ul>
  <li>AlexNet with transfer learning is highly effective for this task.</li>
  <li>Color mode, optimizer choice, and device speed meaningfully affect generalization.</li>
  <li>The model captures subtle emotional cues such as eye tension and ear position.</li>
</ul>

<h3>Future Improvements</h3>
<ul>
  <li>Expand beyond binary emotion classification to <strong>multi-label cues</strong> (ears back, whale eye, lip licking).</li>
  <li>Train on more diverse dogs, lighting, and real-world scenarios.</li>
  <li>Integrate real-time webcam/video inference.</li>
  <li>Explore lightweight architectures (MobileNet, EfficientNet) for deployment.</li>
</ul>
</section>

<footer>
<p>© 2025 PawSense AI — Built for FAU Data Science</p>
</footer>
