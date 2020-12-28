from os import spawnl
from urllib.request import DataHandler
import pyttsx3 
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
# pyttsx3 is text-to-sspeech library

engine = pyttsx3.init('sapi5') 
# sapi is speech to app programming interface by microsoft
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning')
    elif hour>=12 and hour <18:
        speak('Good Afternoon')
    else:
        speak('Good Evening')
    
    speak('How may i help you')

def takecommand():
    '''
    it takes microphone input from user and returns string output
    '''
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        rec.pause_threshold =0.8       # pause_threshold is minimum time brfore breaking flow
        audio = rec.listen(source)

    try:
        print('Recognizing...')
        query = rec.recognize_google(audio , language='en-in')
        print(f'User said: {query}\n')

    except Exception as e:
        # print(e)
        print("say that again please....")
        return "None"
    return query

# specifying chrome path
chrome_path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(chrome_path))


def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('abcd123@gmail.com','#PASSWORD')
    server.sendmail('abcd123@gmail.com',to,content)
    server.close()


if __name__ == '__main__':
    wishme()
    while True:
        query = takecommand().lower()
    # Logic for executing bases on quert
        if 'wikipedia' in query:
            speak('Searching in Wikipedia...')
            query = query.replace('wikipedia','')
            result = wikipedia.summary(query, sentences=2)
            speak('According to wikipedia')
            print(result)
            speak(result)


        elif 'open youtube' in query:
            webbrowser.get("chrome").open_new_tab('youtube.com')

        elif 'open google' in query:
            webbrowser.get("chrome").open_new_tab('google.com')

        elif 'open stack overflow'  in query:
            webbrowser.get("chrome").open_new_tab('stackoverflow.com')
        
        elif 'open mail'  in query:
            webbrowser.get("chrome").open_new_tab('http://www.gmail.com/')

        elif 'play music' in query:
            music_dir = 'E:\\Project_BoB\\music'
            songs = os.listdir(music_dir)
            r_song = random.choice(songs)
            # can use random.sample without replacement
            os.startfile(os.path.join(music_dir, r_song))
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        
        elif 'today' in query:
            strTime = datetime.datetime.now().strftime("%d:%A:%B:%Y")
            speak(f"Today is {strTime}")

        elif 'creator' in query:
            speak('My creator is Anurag..')
        
        elif "visual studio" in query:
            codepath = "C:\\Users\\Anurag\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        
        elif "email to anurag" in query:
            try:
                speak("what should i say??")
                content = takecommand()
                to = "abcd123@gmail.com"
                sendEmail(to,content)
                speak('Email has been sent')
            except Exception as e:
                #print(e)
                speak('Sorry Email has not been sent!!')
        if 'quit' in query:
            exit()

        
            
         