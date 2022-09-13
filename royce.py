
import pyttsx3
import datetime
import speech_recognition as sr
import sys,time,os
import wikipedia,webbrowser

engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    typewriter(f'Royce : {audio}\n')
    engine.say(audio)
    engine.runAndWait()
    
def typewriter(audio):
    for char in audio:
        sys.stdout.write(char) 
        sys.stdout.flush()
        time.sleep(0.005)

def typewriter(message):
    for char in message:
        sys.stdout.write(char) 
        sys.stdout.flush()
        time.sleep(0.005)

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour < 12 :
       speak('Good Morning !')
    elif hour>=12 and  hour < 18:
        speak('Good Afternoon !')
    elif hour >=18 and hour <=24 :
        speak('Good Evening !')
    
    speak('This is Royce , How may I help you ?')

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
      message = 'Royce : Listening...\n'
      typewriter(message)
      r.pause_threshold = 1
      audio = r.listen(source)
  
    try:
        message = 'Royce : Recognising...\n'
        typewriter(message)
        query = r.recognize_google(audio, language='en-in')
        print(f"User : {query}")
  
    except Exception as e :
        message = "Could you repeat it again !\n"
        typewriter(message)
        return "None"
    return query

 
  



if __name__ == "__main__":
    wish()
    while True :
        query = take_command().lower()


        if 'information' in query:
            speak('searching...')
            query = query.replace('can i get some information about', " ")
            results = wikipedia.summary(query, sentences=1)
            typewriter('Royce : According to Wikipedia...\n')
            speak(results)
        
        elif 'search' in query:
            query= query.replace('search'," ")
            webbrowser.open(query)

        elif 'open google' in query:
            speak('opening google...')
            webbrowser.open('google.com')
        elif 'open youtube' in query:
            speak('opening youtube...')
            webbrowser.open('youtube.com')

        elif 'play music' in query:
            speak('Playing Music...')
            music_path = 'E:\\songs'
            songs = os.listdir(music_path)
            print(songs)
            os.startfile(os.path.join(music_path, songs[0]))

        elif "wallpapers" in query:
            os.startfile('C:\\Users\\SRUJAN\\Pictures\\wallpapers')
        elif 'any app' in query:
            os.startfile("C:\\Users\\SRUJAN\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Resso\\Resso.lnk")

        elif "introduce" in query:
            speak("I'm Royce , your Personal Assistant !.. I can help you while browsing or while completing tasks related to Operating System of this Computer. Give me a task...")
        
        elif "well done" in query:
            speak("I would love to hear that from you. Give me another task...")
        elif "quit" in query:
            break
            

    speak("Thank you...Have a Nice Day !")


    
 
# C:\Users\SRUJAN\Royce\royce.py



    