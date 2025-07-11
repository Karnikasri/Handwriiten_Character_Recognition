# ✍️ Handwritten Character Recognition with Python
Handwritten Character Recognition allows computers to read human handwriting and convert it into a machine-readable format.
This project focuses on recognizing English alphabets (A-Z) from handwritten images using Convolutional Neural Networks (CNNs), a powerful technique in Deep Learning.

## Project Overview
This project leverages a CNN trained on a dataset of handwritten English letters (A-Z) to classify each character image. 
It includes preprocessing, model training, evaluation, and a simple GUI to make predictions from hand-drawn characters.

## Technologies Used
- Python 3.x
- TensorFlow / Keras
- NumPy, Pandas, Matplotlib
- Scikit-learn
- Tkinter (for GUI)

## Dataset
We use the `A_Z Handwritten Data.csv` dataset, which contains:
- 26 classes (A-Z)
- 372,450 total samples
- Each sample is a 28x28 grayscale image flattened into a row with a label


## Steps to Implement the Project
 1. Import Libraries & Load Dataset
Import required Python libraries like Keras, NumPy, Pandas, etc., and load the handwritten character dataset.

 2. Preprocess the Data
- Reshape the image data to 28x28 format.
- Normalize the pixel values to [0, 1].
- One-hot encode the labels.
- Split the dataset into training and testing sets.
- Handle class imbalance with `class_weight`.

3. Create & Train the CNN Model
Build a Convolutional Neural Network using Keras. Include dropout layers to prevent overfitting. Train the model on the preprocessed dataset.

5. Evaluate the Model
Plot training vs validation accuracy and loss. Display predictions on sample test images.

6. Save the Model
Save the trained model in `.keras` format for deployment or further use.

7. (Optional) GUI for Prediction
You can build a simple GUI using `Tkinter` to draw characters and use the trained model to predict the letter.

