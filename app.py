import numpy as np
import os
import pickle
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from tensorflow.keras.models import load_model

model = load_model(os.path.join("models", "cancel_classifier_20210921"))

with open(os.path.join("scalers", "std_scaler_20210921.pickle"), "rb") as f:
  std_scaler = pickle.load(f)


app = FastAPI()


@app.get("/ping")
def pong():
  return {"ping": "pong!"}

@app.post("/predict/v1")
def get_prediction(payload: dict):
  X = payload["data"]
  
  if not X:
    raise HTTPException(status_code=400, detail="No data was found.")
  
  if type(X) != list:
    raise HTTPException(status_code=400, detail="Data provided is not a array.")
  
  X = np.array(X)
  X_scaled = std_scaler.transform(X)
  predictions = np.round(model.predict(X_scaled), 0).astype(int).ravel().tolist()
  predictions_dict = {"predictions": predictions}
  return JSONResponse(predictions_dict)


