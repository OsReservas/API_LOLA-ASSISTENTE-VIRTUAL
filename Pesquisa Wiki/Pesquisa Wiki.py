import speech_recognition as sr
import pyttsx3
import wikipedia
import playsound

def procure():
    procurar = comando.replace("procure", " ")
    wikipedia.set_lang("pt")
    resultado = wikipedia.summary(procurar, 2)
    maquina.say(resultado)
    maquina.runAndWait()
procure()

