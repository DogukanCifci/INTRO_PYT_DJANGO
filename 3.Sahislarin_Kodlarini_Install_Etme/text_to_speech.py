from gtts import gTTS

from playsound import playsound

language = 'de'
tts = gTTS(text="Hallo Welt, Wie geht's dir heute? ", lang=language, slow=False)

tts.save('audio/tts.mp3')
playsound('audio/tts.mp3')

