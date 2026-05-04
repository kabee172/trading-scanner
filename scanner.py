from fastapi import FastAPI
from scanner import scan

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Trading scanner is running"}

@app.get("/signals")
def get_signals():
    return scan()
