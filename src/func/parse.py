
import pytesseract
import numpy as np
import cv2
import io


pytesseract.pytesseract.tesseract_cmd = r'tesseract\tesseract.exe'


def parser(attch):

    # create byte object
    byteobj = io.BytesIO(attch)
    # create other object that tesseract can use
    im = cv2.imdecode(np.frombuffer(byteobj.read(), np.uint8), 1)

    text = pytesseract.image_to_string(im)
    print(text)



