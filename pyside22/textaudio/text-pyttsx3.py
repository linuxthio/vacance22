import pyttsx3
engine = pyttsx3.init()
txt="I will speak this text"
# engine.say(txt)
voices = engine.getProperty('voices')       #getting details of current voice
# engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female
engine.setProperty('rate', 150)     # setting up new voice rate

"""VOLUME"""
engine.setProperty('volume',1)    # setting up volume level  between 0 and 1
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.save_to_file(txt, 'txt.mp3')
engine.runAndWait()
import os 
os.system("vlc txt.mp3")
