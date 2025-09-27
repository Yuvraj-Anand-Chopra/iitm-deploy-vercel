from fastapi import FastAPI
from fastapi.responses import JSONResponse
import json
import os

app = FastAPI()

# Load latency data from JSON file
def load_latency_data():
    file_path = os.path.join(os.path.dirname(__file__), 'telemetry', 'q-vercel-latency.json')
    with open(file_path, 'r') as file:
        return json.load(file)

@app.get("/latency")
def get_latency_data():
    data = load_latency_data()
    return JSONResponse(content=data)