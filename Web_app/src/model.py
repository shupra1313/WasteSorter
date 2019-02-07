import keras
from keras.models import Model
from keras import applications, optimizers
from keras.applications.inception_V3 import preprocess_input
from keras.preprocessing import image
from keras.layers import Dense, Flatten, Dropout
from keras.callbacks import ModelCheckpoint
from keras import backend as K
import numpy as np
import pandas as pd
from keras.preprocessing.image import img_to_array,load_img

class Wastesort:

    #Load the model
    
    def __init__(self):
        self.img_width = 299
        self.img_height = 299
        K.clear_session()
        self.create_model()
    
    def create_model(self):

        self.model.load_weights("InceptionV3_model2_waste_sorting_made_simple.h5")

    # prediction
    def call_predict(self, images, imageupload):
        for image_name in images:
            image_path = imageupload + "/" + image_name
            print(f"imagepath: {image_path}")   
            img = load_img(image_path,target_size = (299,299)) #Load the image and set the target size to the size of input of our model
            x = img_to_array(img) #Convert the image to array
            x = np.expand_dims(x,axis=0) #Convert the array to the form (1,x,y,z) 
            x = preprocess_input(x) # Use the preprocess input function o subtract the mean of all the images
            predictions = self.model.predict(x) # Store the argmax of the predictions
            # print(predictions)
            if predictions < 0.1:
                print("compostable")
            elif predictions >= 0.1:
                print("recyclable")

        return predictions
    

