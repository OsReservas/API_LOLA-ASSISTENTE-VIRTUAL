import speech_recognition as sr
import pyttsx3
import wikipedia
import datetime
import playsound

audio = sr.Recognizer()
maquina = pyttsx3.init()

def executa_comando(pular_dora):
    with sr.Microphone() as source:
        #audio.adjust_for_ambient_noise(source)
        print("Ouvindo")
        voz = audio.listen(source)
    try:
        comando = audio.recognize_google(voz, language="pt-BR")
        comando = comando.lower()

        if "dora" in comando or pular_dora == True:
            comando = comando.replace("dora", "")
            if 'bom' and 'dia' in comando.lower():
                maquina.say('bom dia! o que vamos fazer?')
            elif 'boa' and 'tarde' in comando.lower():
                maquina.say('boa tarde! o que vamos fazer?')
            elif 'boa' and 'noite' in comando.lower():
                maquina.say('boa noite! o que vamos fazer?')
            elif "horas" in comando:
                hora = datetime.datetime.now().strftime("%H:%M")
                print(hora)
                maquina.say("Agora são " + hora)
            elif "procure " in comando:
                procurar = comando.replace("procure", " ")
                wikipedia.set_lang("pt")
                resultado = wikipedia.summary(procurar, 2)
                maquina.say(resultado)
            elif "soletre" in comando:
                comando = comando.replace("soletre", " ")
                for letra in comando:
                    maquina.say(letra)
            elif "patinho" in comando:
                comando = comando.replace("historia do", "")
                playsound.playsound('patinho.mp3')
            elif "chapeuzinho" in comando:
                comando = comando.replace("historia da", "")
                playsound.playsound('chapeuzinho.mp3')
            elif "porquinho" in comando:
                comando = comando.replace("historia do", "")
                playsound.playsound('porquinho.mp3')
            elif "sair" in comando:
                print("Tchau amiguinho")
                return
            maquina.runAndWait()
            print("Você disse: " + comando)
            executa_comando(True)
        else:
            print("não detectou dora")
    except:
        print("Não escutei")
        executa_comando(pular_dora)

executa_comando(False)
