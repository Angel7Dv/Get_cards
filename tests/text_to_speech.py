from gtts import gTTS
import os
mytext= """Presentarte como una persona profesional va mucho más allá de tu CV y tu perfil en LinkedIn. Ya sea si quieres tener un negocio propio, una agencia, quieres ser freelancer o quieres un mejor empleo, debes saber que tu presencia en línea lo es todo para alcanzar tus metas profesionales."""
language='es'
myobj=gTTS(text=mytext,lang=language)
myobj.save("test.mp3")

os.system("mpg321 test.mp3")