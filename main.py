from fastapi import FastAPI

app = FastAPI()


@app.get("/rfid")
async def rfid():
    # TODO: replace the random id below with the return value from the RFID function
    return {"id": "283748374"}


@app.get("/qrcode")
async def qrcode():
    # TODO: replace the random id below with the return value from the QRCODE function
    return {"id": "3789375837"}
