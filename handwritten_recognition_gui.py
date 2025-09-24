import tkinter as tk
from tkinter import *
from PIL import Image, ImageDraw, ImageOps
import numpy as np
from keras.models import load_model

# Load trained model
model = load_model(r"C:\Kar_Materials\model_hand.h5")
# Character dictionary
word_dict = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',
             10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',
             18:'S',19:'T',20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z'}

# Create main window
root = tk.Tk()
root.title("Handwritten Character Recognition")

canvas_width = 280
canvas_height = 280

# Canvas widget for drawing
canvas = Canvas(root, width=canvas_width, height=canvas_height, bg='white')
canvas.grid(row=0, column=0, pady=2, sticky=W, columnspan=2)

# PIL image to draw on
image1 = Image.new("L", (canvas_width, canvas_height), 'white')
draw = ImageDraw.Draw(image1)

# Drawing function for mouse drag
def paint(event):
    x1, y1 = (event.x - 8), (event.y - 8)
    x2, y2 = (event.x + 8), (event.y + 8)
    canvas.create_oval(x1, y1, x2, y2, fill='black', width=15)
    draw.ellipse([x1, y1, x2, y2], fill='black')

canvas.bind("<B1-Motion>", paint)

# Clear canvas
def clear_canvas():
    canvas.delete("all")
    draw.rectangle([0, 0, canvas_width, canvas_height], fill='white')
    result_label.config(text="Draw a letter and click Predict")

# Prediction function
def predict():
    # Process canvas image for model input
    img = image1.resize((28, 28))
    img = ImageOps.invert(img)
    img = np.array(img)
    img = img / 255.0
    img = img.reshape(1, 28, 28, 1)

    pred = model.predict(img)
    class_idx = np.argmax(pred)
    result_label.config(text="Prediction: " + word_dict[class_idx])

# Buttons for Predict and Clear
predict_button = Button(root, text="Predict", command=predict)
predict_button.grid(row=1, column=0, pady=2)

clear_button = Button(root, text="Clear", command=clear_canvas)
clear_button.grid(row=1, column=1, pady=2)

# Label to show prediction result
result_label = Label(root, text="Draw a letter and click Predict", font=("Helvetica", 16))
result_label.grid(row=2, column=0, columnspan=2, pady=2)

root.mainloop()
