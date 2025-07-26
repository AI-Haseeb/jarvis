import os
import re
from playsound import playsound
import eel
from engine.command import speak
from engine.config import Assistant_Name
import pywhatkit as kit

# Playing Assistant Sound Function

@eel.expose
def playAssisstantSound(sound):
    music_dir = "www\\assets\\Audio\\start_sound.mp3"
    playsound(music_dir)

def openCommand(query):
    query = query.replace(Assistant_Name, "")  # Remove the word 'open' from the command
    query = query.replace("open", "") 
    query.lower()   

    if query != "":
        speak("Opening" +query)
        os.system("start" +query)
    else:
        speak("Please specify the application to open.")

def playYoutube(query):
    search_term = extract_yt_term(query)
    speak("Playing "+search_term+" on YouTube")
    kit.playonyt(search_term)

def extract_yt_term(command):
    # Define a regular expression pattern to capture the song name
    pattern = r'play\s+(.*?)\s+on\s+youtube'   
    # Use re.search to find the match in the command 
    match = re.search(pattern, command, re.IGNORECASE) 
    # If a match is found, return the extracted song name; otherwise, return None
    return match.group(1) if match else None