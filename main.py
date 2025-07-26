import os 
import eel 

from engine.features import *
from engine.command import *

eel.init('www')

playAssisstantSound("start_sound.mp3")

os.system('start "" "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe" --app=http://localhost:8000/index.html')

eel.start('index.html', mode=None, host='localhost', block=True)