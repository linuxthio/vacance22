from gtts import gTTS
import os
txt="je m'appelle Djibril Thiongane et je suis un bon codeur."


def domp3(txt,nom='untitled'):
    ts=gTTS(txt,lang='fr')
    ts.save(nom+".mp3")
    os.system(f"vlc {nom}.mp3")


domp3(txt,'djiby')


