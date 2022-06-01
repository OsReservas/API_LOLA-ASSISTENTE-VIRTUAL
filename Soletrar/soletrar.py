import speech_recognition as sr
import pyttsx3
import playsound

def soletrar():
    comando = comando.replace("soletre", " ")
    for letra in comando:
        maquina.say(letra)
    maquina.runAndWait()
soletrar()