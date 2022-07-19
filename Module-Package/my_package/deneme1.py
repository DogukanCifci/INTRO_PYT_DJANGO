def deneme_func() :
    print('Deneme Fonksiyon-Relative Path calisiyor!!!')



if __name__ == '__main__' :
    from playsound import playsound
    from text_to_speech import speak
    speak("Merhaba heyyy arkadaşlar Python dersi nasıl gidiyor", "tr", save=True, file="merhaba.mp3", speak=True)