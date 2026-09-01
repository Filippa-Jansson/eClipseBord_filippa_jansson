from fastapi import FastAPI
from backend.data_processing import df1, df2

app = FastAPI()

@app.get("/lunar/data")
def get_lunar_data():
    return df1.head(10).to_dict (orient="records")

@app.get("/solar/data")
def get_solar_data():
    return df2.head(10).to_dict (orient="records")