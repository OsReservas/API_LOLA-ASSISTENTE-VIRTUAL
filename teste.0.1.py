import speech_recognition as sr
import pyttsx3
import wikipedia
import playsound

audio = sr.Recognizer()
maquina = pyttsx3.init()

def executa_comando(pular_lola):

    with sr.Microphone() as source:
        print("Ouvindo")
        voz = audio.listen(source)
    try:
        comando = audio.recognize_google(voz, language="pt-BR")
        comando = comando.lower()

        if "lola" in comando or pular_lola == True:
            comando = comando.replace("lola", "")
            if 'bom dia' in comando.lower():
                maquina.say('bom dia! o que vamos fazer?')
            elif 'boa tarde' in comando.lower():
                maquina.say('boa tarde! o que vamos fazer?')
            elif 'boa noite' in comando.lower():
                maquina.say('boa noite! o que vamos fazer?')

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
            executa_comando(True)
        else:
            print("não detectou lola")
    except:
        print("Não escutei")
        executa_comando(pular_lola)

executa_comando(False)



