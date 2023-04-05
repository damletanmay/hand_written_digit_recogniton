import tensorflow as tf
import cv2
import numpy as np
import os

hindi_model_path = os.path.join(os.path.join(os.path.join(os.getcwd(),'digit'),'models'),'hindi_digit_recognition.h5')
english_model_path = os.path.join(os.path.join(os.path.join(os.getcwd(),'digit'),'models'),'english_digit_recognition.h5')

def predict_hindi_digit(image_path):

    # Use the model for prediction
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, (32, 32))
    image = image / 255.0
    image = np.expand_dims(image, axis=0).reshape(-1, 32, 32, 1)
    model = tf.keras.models.load_model(hindi_model_path)
    print(model)
    prediction = model.predict(image)
    return int(np.argmax(prediction))

def predict_english_digit(image_path):
    img = cv2.imread(image_path)[:,:,0]
    img = cv2.resize(img, (28, 28))
    img = np.invert(np.array([img]))
    model = tf.keras.models.load_model(english_model_path)
    print(model)
    prediction = model.predict(img)
    return int(np.argmax(prediction))
