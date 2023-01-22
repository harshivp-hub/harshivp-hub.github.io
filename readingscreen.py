import speech_recognition as sr
import pyttsx3
import time
import cv2
import mss
import numpy
import pytesseract

ascii_braille = {}
file = open("txt.txt", "r")


def Imagetotext():
    mon = {'top': 280, 'left': 100, 'width': 1600, 'height': 800}

    with mss.mss() as sct:
        im = numpy.asarray(sct.grab(mon))
        im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

        text = pytesseract.image_to_string(im)
        print(text)
        fp = open("txt.txt", "w+")
        fp.write(text)
        fp.close()
Imagetotext()


def read_line(file):
    text = file.read()
    file.close()
    return text


text = read_line(file)



def texttobraille(text):
    final_string = ""
    for char in text:
        char = char.lower()
        if char == "a":
            final_string = final_string + "⠁"
        elif char == "b":
            final_string = final_string + "⠃"
        elif char == "c":
            final_string = final_string + "⠉"
        elif char == "d":
            final_string = final_string + "⠙"
        elif char == "e":
            final_string = final_string + "⠑"
        elif char == "f":
            final_string = final_string + "⠋"
        elif char == "g":
            final_string = final_string + "⠛"
        elif char == "h":
            final_string = final_string + "⠓"
        elif char == "i":
            final_string = final_string + "⠊"
        elif char == "j":
            final_string = final_string + "⠚"
        elif char == "k":
            final_string = final_string + "⠅"
        elif char == "l":
            final_string = final_string + "⠇"
        elif char == "m":
            final_string = final_string + "⠍"
        elif char == "n":
            final_string = final_string + "⠝"
        elif char == "o":
            final_string = final_string + "⠕"
        elif char == "p":
            final_string = final_string + "⠏"
        elif char == "q":
            final_string = final_string + "⠟"
        elif char == "r":
            final_string = final_string + "⠗"
        elif char == "s":
            final_string = final_string + "⠎"
        elif char == "t":
            final_string = final_string + "⠞"
        elif char == "u":
            final_string = final_string + "⠥"
        elif char == "v":
            final_string = final_string + "⠧"
        elif char == "w":
            final_string = final_string + "⠺"
        elif char == "x":
            final_string = final_string + "⠭"
        elif char == "y":
            final_string = final_string + "⠽"
        elif char == "z":
            final_string = final_string + "⠵"
        elif char == "1":
            final_string = final_string + "⠼⠁"
        elif char == "2":
            final_string = final_string + "⠼⠃"
        elif char == "3":
            final_string = final_string + "⠼⠉"
        elif char == "4":
            final_string = final_string + "⠼⠙"
        elif char == "5":
            final_string = final_string + "⠼⠙"
        elif char == "6":
            final_string = final_string + "⠼⠋"
        elif char == "7":
            final_string = final_string + "⠼⠛"
        elif char == "8":
            final_string = final_string + "⠼⠓"
        elif char == "9":
            final_string = final_string + "⠼⠊"
        elif char == "0":
            final_string = final_string + "⠼⠚"
        elif char == " ":
            final_string = final_string + " "
        elif char == "\n":
            final_string = final_string + "\n"
        else:
            continue
    print(final_string)
    return final_string
file = open("braille.txt", "w+", encoding="utf-8")
file.write(texttobraille(text))
file.close()