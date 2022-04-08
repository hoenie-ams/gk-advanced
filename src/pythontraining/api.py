from typing import Optional

from fastapi import FastAPI, HTTPException
import pandas as pd

url = "https://www.knmi.nl/nederland-nu/weer/waarnemingen"
dfs = pd.read_html(url)
df = dfs[0].set_index("Station")

app = FastAPI()

db = {"EHRL": "weather data",
      "EDQR": "other weather data",
      "TRLN": "more weather data"}


@app.get("/")
def read_root():
    return {"Hello": "Universe"}


# Exercise: endpoint for weather data
@app.get("/weather/{station_id}")
def read_weather(station_id: str):
    station_id = station_id.upper()
    if station_id not in db:
        raise HTTPException(status_code=404,
                            detail="Weather station not in the database")
    return {"station_id": station_id, "result": db[station_id]}


@app.get("/waarnemingen/{station_name}")
def read_waarneming(station_name: str):
    if station_name not in df.index:
        raise HTTPException(status_code=404,
                            detail="Weather station not in the database")
    return {"station_name": station_name,
            "result": df.loc[station_name].to_dict()}
