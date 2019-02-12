# from flask import Flask, render_template, request
# import keras
# from keras.models import Model
# from keras import applications, optimizers
# from keras.applications.inception_v3 import preprocess_input
# from keras.preprocessing import image
# from keras.layers import Dense, Flatten, Dropout
# from keras.callbacks import ModelCheckpoint
# import numpy as np
# import pandas as pd
# from keras import backend as K


# class PredictWaste:
#     def __init__(self):
#         #Load the model
#         self.img_width = 299
#         self.img_height = 299

#         #get the labels
#         df_labels = pd.read_csv("labels.csv")
#         df_labels = df_labels.sort_values(by=['Index'])
#         self.labels= list(df_labels['Label'])
#         self.num_labels = len(self.labels)
#         K.clear_session()
#         self.create_model()

#         # self.Model._make_predict_function()

#     def create_model(self):
#         self.model = self.model.load_weights("model.05-0.94.hdf5")

#     def call_predict(self, images, folder):
#         predictions = []
#         #predict
#         for image_name in images:
#             image_path = folder+ "/" + image_name
#             print(f"imagepath: {image_path}")
#             test_image = keras.preprocessing.image.load_img(image_path, target_size=(299,299), grayscale=False)
#             test_image = image.img_to_array(test_image)
#             test_image = np.expand_dims(test_image, axis=0)
#             test_image = preprocess_input(test_image)
#             # print(test_image)
#             predict = self.model.predict(test_image)
#             # print(predict)
#             zip_pred= zip(predict[0], self.labels)
#             # if the prediction is high then only senf the value
#             match_found = False
#             for pred_value, pred in zip_pred:
#                 if (pred_value > 0.8):
#                     match_found = True
#                     predictions.append((image_name, pred))

#             if(not(match_found)):
#                 predictions.append((image_name, ""))

#         return predictions


# # app = Flask(__name__)

# # @app.route('/')
# # def student():
# #    return render_template('index.html')

# # @app.route('/result',methods = ['POST', 'GET'])
# # def result():
# #    if request.method == 'POST':
# #       result = request.form
# #       return render_template("result.html",result = result)

# # if __name__ == '__main__':
# #    app.run(debug = True)