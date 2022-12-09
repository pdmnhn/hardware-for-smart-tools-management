from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
)


@app.get("/rfid")
async def rfid():
    # TODO: replace the random id below with the return value from the RFID function
    return {"id": "283748374"}


@app.get("/qrcode")
async def qrcode():
    # TODO: replace the random id below with the return value from the QRCODE function
    return {"id": "3789375837"}
