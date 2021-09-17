#!/usr/bin/python
# -*- coding: utf-8 -*-

import speech_recognition as sr
import pyautogui
import time
import webbrowser
from gtts import gTTS
import os
import random
import winsound
import playsound
import scrap_diki
from selenium import webdriver
# import SeleniumLibrary


def Alexa_respond(text: str, lang='en-US'):
    gts_sound = gTTS(text, lang=lang)
    r = random.randint(1, 1000000)
    file_path = 'audio-' + str(r) + '.mp3'
    gts_sound.save(file_path)
    playsound.playsound(file_path)
    os.remove(file_path)


def listen_function(src, ask=False):
    global recording
    try:
        audio = recording.listen(src)
        text = recording.recognize_google(audio)
        text.lower()
        print(text)
        if str(text) in ["make screenshot", "shot", "screenshot", "make screen", "screen"]:
            pyautogui.press('PrtSc')
        elif "what time is it" in str(text):
            url = 'https://www.google.com/search?q=czas'
            Alexa_respond(f'It is {time.ctime()}', 'pl')
            webbrowser.get().open(url)
        elif 'search' in str(text):
            search_data = str(text)[7:]
            url = f'https://www.google.com/search?q={search_data}'
            webbrowser.get().open(url)
        elif 'location' in str(text):
            search_data = str(text)[8:]
            url = f'https://google.pl/maps/place/{search_data}/&amp;'
            webbrowser.get().open(url)
        elif 'chess' in str(text) or 'play chess' in str(text):
            url = 'https://lichess.org/'
            webbrowser.get().open(url)
        elif 'idiot' in str(text):
            webbrowser.open('maja.jpg')
        elif 'awesome' in str(text):
            webbrowser.open("ja.jpg")
        elif 'what is the weather' in str(text):
            url = 'https://www.google.com/search?q=pogoda'
            webbrowser.get().open(url)
            Alexa_respond('Weather sucks today')
        elif 'exit this' in str(text):
            exit()
        elif 'find website' in str(text):
            # driver = webdriver.Chrome(
            #     executable_path=r'C:/Users/gacek/Desktop/Projekty IT/Python/Voice_Recognition/chromeDriver/chromedriver.exe')
            url = driver.current_url
            synn = scrap_diki.find_connected_words(url)
            for key, value in synn.items():
                # Alexa_respond(f'{key} means {value}')
                Alexa_respond(f'{key}', lang='pl')
                Alexa_respond(f'means {value}') 
    except sr.UnknownValueError as e:
        Alexa_respond("Sorry I didn't understand")

    except sr.RequestError as e:
        pass


if __name__ == "__main__":
    import os

    # os.chmod('C:/Users/gacek/Desktop/Projekty IT/Python/Voice_Recognition/chromeDriver', 755)
    driver = webdriver.Chrome(
        executable_path=r'C:/Users/gacek/Desktop/Projekty IT/Python/Voice_Recognition/chromeDriver/chromedriver.exe')
    recording = sr.Recognizer()
    with sr.Microphone() as source:

        while True:
            before = time.time()
            before2 = time.time()
            listen_function(source)
