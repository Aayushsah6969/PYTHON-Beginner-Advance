import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine=pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__=="__main__":
    speak("Initializing Jarvis...")
    while True:
        r=sr.Recognizer()
        
        print("recognizing...")
        try:
            with sr.Microphone()as source:
                print("Listening...")
                audio=r.listen(source, timeout=2, phrase_time_limit=1)
        
            word=r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("Yes master")
                with sr.Microphone()as source:
                    print("Listening...")
                    audio=r.listen(source, timeout=2, phrase_time_limit=1)
        
            print(command)
        except Exception as e:
            print("Error: {0}".format(e))