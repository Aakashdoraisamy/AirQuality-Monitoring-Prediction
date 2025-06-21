from django.db import models
from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models
#from keras.models import load_model
import cv2
import numpy as np
import pickle
import json
from PIL import Image
import pandas as pd 

# Testing phase
rf = pickle.load(open("RF.pkl", 'rb'))
dt = pickle.load(open("SVM.pkl", 'rb'))


data = pd.read_csv('test_data.csv')
print("+++++++++++++++++")
print(data.head(1))




def predict(algo,row): 
	print(row)
	print(algo)
	filter_data = data.loc[row].values.reshape(1, -1)
	print(filter_data.shape)
	print(filter_data)
	if algo=='rf':
		y_pred= rf.predict(filter_data)
		return y_pred[0]
	else:
		y_pred=dt.predict(filter_data)
		return y_pred[0]

