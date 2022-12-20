import RPi.GPIO as GPIO
import MFRC522
import cv2

GPIO.setmode(GPIO.BOARD)  # Set GPIO pin numbering


def read_qr():
    # set up camera object
    cap = cv2.VideoCapture(0)  # Selecting the PRIMARY camera
    detector = cv2.QRCodeDetector()
    # get the image
    img = cap.read()[1]
    # get bounding box coords and data
    data = detector.detectAndDecode(img)[0]

    return data if data else ""


def read_rfid():
    MIFAREReader = MFRC522.MFRC522()
    GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    if (GPIO.input(12) == False):
        (status, uid) = MIFAREReader.MFRC522_Anticoll()
        if status == MIFAREReader.MI_OK:
            data = "".join(map(str, uid))
            return data

    return ""
