import numpy as np
import os
import pickle
from fastapi import FastAPI, HTTPException
from tensorflow.keras.models import load_model

#Load Tensorflow model
model = load_model(os.path.join("models", "cancel_classifier_20210921"))

#Load Scaler
with open(os.path.join("scalers", "std_scaler_20210921.pickle"), "rb") as f:
  std_scaler = pickle.load(f)

app = FastAPI()

#GET method to test API
@app.get("/ping")
def pong():
  return {"ping": "pong!"}

#POST method to send data and get predictions
@app.post("/predict/v1")
def get_prediction(payload: dict):
  X = payload["data"]
  
  if not X:
    raise HTTPException(status_code=400, detail="No data was found.")
  
  if type(X) != list:
    raise HTTPException(status_code=400, detail="Data provided is not a array.")
  
  #Convert list of lists to np.array
  X = np.array(X)

  #Apply scaler to data
  X_scaled = std_scaler.transform(X)

  #Get predictions from scaled data
  predictions = np.round(model.predict(X_scaled), 0).astype(int).ravel().tolist()

  #Send predictions
  predictions_dict = {"predictions": predictions}
  return predictions_dict


