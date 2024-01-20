#!/usr/bin/python3
import speech_recognition as aa
import pyttsx3
import pywhatkit
import datetime
import pyautogui
import wikipedia
import webbrowser
from googlesearch import search
import os


listener = aa.Recognizer()

machine = pyttsx3.init()

def talk(text):
    machine.say(text)
    machine.runAndWait()

def input_instruction():
    global instruction
    try:
        with aa.Microphone() as origin:
            print("listening.....")
            speech = listener.listen(origin, timeout=5)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()

            if "jasper" in instruction:
                instruction = instruction.replace("jasper", "").strip()
            print(instruction)
    except Exception as e:
        print(f"Error capturing voice input: {e}")
    return instruction


def play_jasper():
    instruction = input_instruction()
    # print(instruction)
    try:
        if "on youtube search" in instruction:
            song = instruction.replace('on youtube search', "").strip()
            talk("playing" + song)
            pywhatkit.playonyt(song)

        elif "time" in instruction:

            time = datetime.datetime.now().strftime('%I:%M%p')
            talk('Current time' + time)

        elif "date" in instruction:
            date = datetime.datetime.now().strftime("%d /%m /%Y")
            talk("Today's date " + date)

        elif "how are you" in instruction:
            talk("I'm fine, how about you")

        elif "what is your name" in instruction:
            talk("I am Jasper, what do you want me to do for you?")

        elif "on wikipedia search" in instruction:
            human = instruction.replace('on wikipedia search', '').strip()
            info = wikipedia.summary(human, 2)
            print(info)
            talk(info)

        elif "on web browser open" in instruction:
            url = instruction.replace('on web browser open', '').strip()
            info = webbrowser.open(url)

        elif "on chrome search" in instruction:
            query = instruction.replace('on chrome search', '').strip()
            os.startfile('C:\Program Files\Google\Chrome\Application\chrome.exe')
            talk(query)

            pyautogui.write(query)
            pyautogui.press('enter')

        else:
            talk("Please repeat!!")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        talk("Sorry, there was an error. Please try again.")


def whatsapp_jasper():
    instruction = input_instruction()    
    try:
        if "whatsapp" in instruction:
            instruction.replace("whatsapp", "").strip()
            if "number" in instruction:
                print("whatsapp number: ")
                num = input_instruction()
                talk(num)
                # continue
            if "message" in instruction:
                print("what message do you want to send to this number ")
                message = input_instruction()
                talk(message)

        # num = input("whatsapp number: ")
        # message = input("Enter message you want to send: ")

        pywhatkit.sendwhatmsg_instantly(num, message)
        # else:
        #     talk("Please try again."

    except Exception as e: 
        print(f"An error occurred: {e}")
        

# whatsapp_jasper()
play_jasper()
