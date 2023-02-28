import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def get_audio():
     # This method takes microphone input from user and return string
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        audio = r.listen(source)
        said = ""

        try:
            
            said = r.recognize_google(audio)
            
        except Exception as e:
            return "please say again"

    return said
   

    
def speak(audio):
    #This method used by our A.I voice to speak
    engine.say(audio)
    engine.runAndWait()
def wish():
    #This method execute in beggining to greet user
    hour=int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12:
        speak("good morning sir")
    elif hour>=12 and hour<=19:
        speak("good afternoon sir")
    else:
        speak("good evening sir")
    speak("Hello my name is Dakshesh patel. How can i help you")
wish()

s=get_audio().lower()
 
if 'wikipedia' in s:
     s=s.replace('wikipedia',' ')
     results=wikipedia.summary(s,sentences=2)
     speak("according to wikipedia")
     speak(results)
elif 'open youtube' in s:
     speak('opening youtube')
     webbrowser.open('youtube.com')
elif 'open google' in s:
     speak('opening google')
     webbrowser.open('google.com')
elif 'favourite' in s:
     speak('playing your favourite song')
     webbrowser.open('https://www.youtube.com/watch?v=lzEop75AeOk&list=RDlzEop75AeOk&start_radio=1')
elif 'time' in s:
     time=datetime.datetime.now().strftime('%H:%M:%S')
     speak("sir, the time is",time)
else:
     speak('sorry sir, till now we dont provide this functionality right now')