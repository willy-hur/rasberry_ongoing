# import sys
# from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QLabel, QPushButton)
# from keypad_shape import*
import keyboard
import cv2
import matplotlib
from matplotlib import pyplot as plt

'''
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
pad = MyApp()
pad.initUI()
BUTTON_start = 0 
BUTTON_up = 1
BUTTON_down = 2
BUTTON_input = 3
BUTTON_cancel = 4
BUTTON_enter = 5
BUTTON_correction = 6
BUTTON_consonant = 7
BUTTON_number = 8
BUTTON_vowels = 9
'''

# but0_value = GPIO.input(BUTTON_up)
# but1_value = GPIO.input(BUTTON_down)
fig = plt.figure()
rows = 1
cols = 2

im = cv2.imread('C:/Users\/JunJe Hur/Desktop/picture/0/001.png')
im2 = cv2.imread('C:/Users\/JunJe Hur/Desktop/picture/0/002.png')

img1 = cv2.imread('IMG01.jpg')
img2 = cv2.imread('IMG03.jpg')

ax1 = fig.add_subplot(rows, cols, 1)
ax1.imshow(cv2.cvtColor(im, cv2.COLOR_BGR2RGB))
ax1.set_title('Jumok community')
ax1.axis("off")

ax2 = fig.add_subplot(rows, cols, 2)
ax2.imshow(cv2.cvtColor(im2, cv2.COLOR_BGR2RGB))
ax2.set_title('Withered trees')
ax2.axis("off")

plt.show()



cv2.waitKey(0)
cv2.destroyAllWindows()

# start
while True:
    if keyboard.read_key() == "s":
        print("You pressed p")
        break
