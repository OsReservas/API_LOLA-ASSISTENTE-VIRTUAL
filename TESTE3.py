import speech_recognition as sr
import pyttsx3

audio = sr.Recognizer()
maquina = pyttsx3.init()

def ouvir_microfone():
    # Habilita o microfone do usuário
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        # Chama um algoritmo de reducao de ruidos no som
        microfone.adjust_for_ambient_noise(source)

def executa_comando():

    try:
        with sr.Microphone() as source:
            print("Ouvindo")
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language="pt-BR")
            comando = comando.lower()
            if "dora" in comando:
                comando = comando.replace("dora", " ")
                maquina.say(comando)
                maquina.runAndWait()

    except:
        print("Microfone não está ok")

def comando_voz_usuario():
    comando = executa_comando()
    if "soletrar" in comando:
        soletre = comando.replace("Soletrar", " ")
        for letra in soletre:
        maquina.say("Soletrando" + print)
        maquina.runAndWait()

comando_voz_usuario()