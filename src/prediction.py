import joblib
import pandas as pd

# Load model
model = joblib.load('models/RF.pkl')  # or SVM.pkl

# Predict for a sample input
sample_input = pd.DataFrame([[55, 102, 19, 45, 37, 15, 0.5, 6, 28]], 
                            columns=['PM2.5', 'PM10', 'NO', 'NO2', 'NOx', 'NH3', 'CO', 'SO2', 'O3'])

prediction = model.predict(sample_input)
print("Predicted Air Quality:", prediction)
