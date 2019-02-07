from flask import Flask, render_template, request, redirect
import os
import glob
from keras.models import Model
import pandas as pd
from keras import backend as K
import keras
# from keras.applications.inception_V3 import preprocess_input
from keras.preprocessing import image
from keras import backend as K
import numpy as np
from keras.preprocessing.image import img_to_array,load_img
import h5py

class Wastesort:

   #Load the model


   def create_model(self):
       self.img_width = 299
       self.img_height = 299
       K.clear_session()
       self.create_model()
       filename = 'InceptionV3_model2_waste_sorting_made_simple.h5'
       f = h5py.File(filename, 'r')

       self.f.load_weights(filename)

   # prediction
   def call_predict(self, images, img_path):
       for image_name in images:
           img_path = imageupload + "/" + image_name
           print(f"imagepath: {img_path}")
           img = load_img(img_path,target_size = (299,299)) #Load the image and set the target size to the size of input of our model
           x = img_to_array(img) #Convert the image to array
           x = np.expand_dims(x,axis=0) #Convert the array to the form (1,x,y,z) 
           x = preprocess_input(x) # Use the preprocess input function o subtract the mean of all the images
           predictions = self.model.predict(x) # Store the argmax of the predictions
           print(predictions)
           if predictions < 0.1:
               print("compostable")
           elif predictions >= 0.1:
               print("recyclable")

       return predictions

app = Flask(__name__, static_folder="images")
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    print(target)   # print for debugging purposes

    if not os.path.isdir(target):
        os.mkdir(target)

    for upload in request.files.getlist("file"):
        print(upload)
        filename = upload.filename
        destination = "/".join([target, filename])
        print("Accept incoming file:", filename)
        print("Save it to:", destination)
        upload.save(destination)

    return render_template("complete.html", image_name = filename)

@app.route('/<filename>', methods=['GET'])
def send_image(filename):
    return send_from_directory("images", filename)
if __name__ == '__main__':
   app.run(debug=True)