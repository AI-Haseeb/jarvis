import pyttsx3
import speech_recognition as sr
import eel
import time

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Set to the first voice
    engine.setProperty('rate', 185)  # Set speech rate
    engine.setProperty('volume', 1)  # Set volume level (0.0 to 1.0)
    eel.DisplayMessage(text)
    engine.say(text)
    engine.runAndWait()

@eel.expose
def takecommand():


    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        eel.DisplayMessage("Listening...")
        r.pause_threshold = 1  # Adjust this value based on your environment
        r.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise 
        audio = r.listen(source, 10, 6)

    try:
        print("Recognizing...")
        eel.DisplayMessage("Recognizing...")
        # Use the recognize_google method to convert speech to text
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        eel.DisplayMessage(query)
        time.sleep(2)
        
    except Exception as e:
        print("Sorry, I did not understand that. Please try again.")
        return("Say that again please...")
    return query.lower()   

# text = takecommand()
# speak(text)

@eel.expose
def allCommands():

    query = takecommand()
    print(f"Command received: {query}")
    
    if 'open' in query:
        from engine.features import openCommand
        openCommand(query)
    elif "on youtube" in query:
        from engine.features import playYoutube
        playYoutube(query)  
    else:
        print("Command not recognized. Please try again.")    
    eel.ShowHood()    