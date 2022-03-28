import playsound
import speech_recognition as sr
import pyaudio
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-2].id)


# Função para ouvir e reconhecer a fala
def ouvir_microfone():
    # Habilita o microfone do usuário
    microfone = sr.Recognizer()

    # usando o microfone
    with sr.Microphone() as source:
        # Chama um algoritmo de reducao de ruidos no som
        microfone.adjust_for_ambient_noise(source)

        # Frase para o usuario dizer algo
        print("Diga alguma coisa: ")

        # Armazena o que foi dito numa variavel
        audio = microfone.listen(source)

    try:

        # Passa a variável para o algoritmo reconhecedor de padroes
        frase = microfone.recognize_google(audio, language='pt-BR')

        if 'boa noite' in frase:
            engine.say('Boa noite')
            engine.runAndWait()
        '''elif 'bom dia' in frase:
            engine.say('Bom dia, tudo certo e com voce?')
            engine.runAndWait()
        elif 'boa tarde' in frase:
            engine.say('boa tarde, tudo certo e com voce?')
            engine.runAndWait()'''

        # Retorna a frase pronunciada
        print("Você disse: " + frase)

    # Se nao reconheceu o padrao de fala, exibe a mensagem
    except sr.UnkownValueError:
        print("Não entendi")

    return frase

ouvir_microfone()

def ouvir_microfone():
    # Habilita o microfone do usuário
    microfone = sr.Recognizer()

    # usando o microfone
    with sr.Microphone() as source:
        # Chama um algoritmo de reducao de ruidos no som
        microfone.adjust_for_ambient_noise(source)

        # Frase para o usuario dizer algo
        print("Diga alguma coisa: ")

        # Armazena o que foi dito numa variavel
        audio = microfone.listen(source)

    try:

        # Passa a variável para o algoritmo reconhecedor de padroes
        frase = microfone.recognize_google(audio, language='pt-BR')

        if 'história' in frase:
            playsound.playsound('historia.mp3')

        # Retorna a frase pronunciada
        print("Você disse: " + frase)

    # Se nao reconheceu o padrao de fala, exibe a mensagem
    except sr.UnkownValueError:
        print("Não entendi")

    return frase

ouvir_microfone()