#pip install speechrecognition
#pip install gTTs
#pip install playsound

import speech_recognition as sr
from gtts import gTTS
import os
import time
import playsound
voice_speak = 0
from pygame.mixer import Sound



def speak(text):
    tts = gTTS(text=text, lang='ko')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    s = Sound()
    s.read('voice.mp3')
    s.play()

voice_speak = '나는 빅스비예요'
speak(voice_speak)
