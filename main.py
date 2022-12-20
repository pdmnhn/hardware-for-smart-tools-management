from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from time import time
from read import read_qr, read_rfid

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
)


@app.get("/rfid")
async def rfid():
    start = time()
    while (time() - start) < 10:
        data = read_rfid()
        if data:
            return {"id": data}

    return {"error": "Couldn't read from the RFID"}


@app.get("/qrcode")
async def qrcode():
    start = time()
    while (time() - start) < 10:
        data = read_qr()
        if data:
            return {"id": data}

    return {"error": "Couldn't read from the QR Code"}
