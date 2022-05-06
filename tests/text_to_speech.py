from gtts import gTTS
import os
mytext= """Presentarte como una persona profesional"""
language='es'
myobj=gTTS(text=mytext,lang=language)
myobj.save("test.mp3")

os.system("mpg321 test.mp3")