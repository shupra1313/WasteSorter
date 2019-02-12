from flask import Flask, render_template, request, redirect
import os
import glob
from keras.models import Model
import pandas as pd
from keras import backend as K
import keras
import keras.applications.inception_v3 as incept
from keras.preprocessing import image
from keras.models import load_model
from keras import backend as K
import numpy as np
from keras.preprocessing.image import img_to_array,load_img
import h5py
import numpy

def create_model():
    K.clear_session()
    filename = 'model.05-0.94.hdf5'
    model = load_model(filename)
    return model

# prediction
def call_predict(images, imageupload):
    model = create_model()
    for image_name in images:
        image_path = imageupload + "/" + image_name
        print(f"imagepath: {image_path}")
        img = load_img(image_path,target_size = (299,299)) #Load the image and set the target size to the size of input of our model
        x = img_to_array(img) #Convert the image to array
        x = np.expand_dims(x,axis=0) #Convert the array to the form (1,x,y,z)
        x = incept.preprocess_input(x) # Use the preprocess input function o subtract the mean of all the images
        predictions = model.predict(x) # Store the argmax of the predictions
        prediction = predictions[0][0]
        if prediction < 0.5:
            print("recyclable")
            prediction_category = 'recyclable'
        elif prediction >= 0.5:
            print("compostable")
            prediction_category = 'compostable'

    return prediction_category

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

####################### Define routes ###########################
@app.route("/",  methods=['GET', 'POST'])
def index():
    print("upload click")
    print(request.method)
    if request.method == 'POST':
        if request.files['file']:
            print('got file')
            images = request.files.getlist("file") # convert multidict to dict
            print(f"Images: {images}")
            # Remove all the files
            files = glob.glob(app.config['UPLOAD_FOLDER']+'/*')
            # print(files)
            for f in files:
                os.remove(f)

            filenames = []
            #save the image
            for image in images:     #image will be the key
                # create a path to the uploads folder
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
                image.save(filepath)
                filenames.append(image.filename)
                print(filenames)

            category = call_predict(filenames, app.config['UPLOAD_FOLDER'])

            return render_template('index.html', prediction=category, image=filepath)
        else:
            return('upload failed')
    else:
        # Print an error message
        print("Error: Image not recognized")

        return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)