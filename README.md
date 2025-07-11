Handwritten Character Recognition (A–Z) using CNN

This project uses Convolutional Neural Networks (CNN) to recognize handwritten English alphabets (A–Z) from grayscale images. It processes a large dataset of handwritten characters and provides a simple GUI for real-time letter prediction.

##  Project Overview

- Recognizes handwritten characters (A–Z) using deep learning.
- Uses CNN model built with Keras and TensorFlow.
- Includes data preprocessing, model training, evaluation, and a GUI.
- Dataset: [A_Z Handwritten Data.csv](https://www.kaggle.com/datasets/sachinpatel21/az-handwritten-alphabets-in-csv-format)

## Technologies Used
- Python 3.x  
- TensorFlow / Keras  
- NumPy, Pandas, Matplotlib  
- Scikit-learn  
- Tkinter (GUI)

##  Dataset Details
- 26 classes (A to Z)
- 372,450 labeled grayscale images
- Each image: 28x28 pixels, flattened into 784 columns

##  How It Works

### 1. Load and Preprocess Data
- Normalize image pixel values to range [0, 1]
- Reshape to (28, 28, 1) for CNN input
- One-hot encode labels
- Handle class imbalance using `class_weight`

### 2. Model Architecture
- CNN with Conv2D, MaxPooling, Dropout
- Flatten + Dense layers for final classification
- Output layer with softmax (26 classes)

### 3. Training
- Optimizer: Adam
- Loss: Categorical Crossentropy
- Callbacks: EarlyStopping, ReduceLROnPlateau

### 4. Evaluation
- Accuracy and loss plots
- Predict and visualize results for test samples


##  GUI (Optional)

A basic Tkinter GUI allows users to draw a letter on the screen and get the model's prediction in real time.


##  Model Performance (1 Epoch Sample)

- Training Accuracy: ~26%
- Validation Accuracy: ~6%
> ⚠️ Note: The current model suffers from `NaN` loss due to architecture or learning rate issues. Further tuning is required.


## Improvements (To-Do)

- Fix NaN loss issue by adjusting architecture or learning rate
- Increase training epochs
- Add BatchNormalization and better regularization
- Improve GUI for smoother drawing

