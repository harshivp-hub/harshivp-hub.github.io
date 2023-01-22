from flask import Flask, jsonify, request
from PIL import ImageGrab
import pytesseract
import cv2
import numpy
from readingscreen import TextToBraille

app = Flask(__name__)

@app.route('/braille', methods=['GET','POST'],)
def get_braille():
    # capture the screen
    img = ImageGrab.grab()
    # convert to grayscale
    gray = cv2.cvtColor(numpy.array(img), cv2.COLOR_RGB2GRAY)
    # extract text
    text = pytesseract.image_to_string(gray)
    # convert to braille
    final_string=TextToBraille(text)
    print(text)

    return final_string

if __name__ == '__main__':
    app.run(debug=True,port=5000)
