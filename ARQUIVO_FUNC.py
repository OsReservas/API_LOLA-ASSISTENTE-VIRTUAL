import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import datetime
import playsound

audio = sr.Recognizer()
maquina = pyttsx3.init()

def executa_comando():
    try:
        with sr.Microphone() as source:
            print("Ouvindo")
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language="pt-BR")
            comando = comando.lower()
            if "dora" in comando:
                comando = comando.replace("dora", "")
                maquina.runAndWait()
                if "horas" in comando:
                    hora = datetime.datetime.now().strftime("%H horas e %M minutos")
                    maquina.say("Agora são" + hora)
                    maquina.runAndWait()
                elif "procure " in comando:
                    procurar = comando.replace("procure", " ")
                    wikipedia.set_lang("pt")
                    resultado = wikipedia.summary(procurar, 2)
                    maquina.say(resultado)
                    maquina.runAndWait()
                elif "soletre" in comando:
                    comando = comando.replace("soletre", " ")
                    for letra in comando:
                        maquina.say(letra)
                        maquina.runAndWait()
                elif "patinho" in comando:
                    comando = comando.replace("historia do", "")
                    playsound.playsound('patinho.mp3')
                elif "chapeuzinho" in comando:
                    comando = comando.replace("historia da", "")
                    playsound.playsound('chapeuzinho.mp3')
                elif "porquinho" in comando:
                    comando = comando.replace("historia do", "")
                    playsound.playsound('porquinho.mp3')



    except:
        print("Não escutei")
    return comando

executa_comando()
