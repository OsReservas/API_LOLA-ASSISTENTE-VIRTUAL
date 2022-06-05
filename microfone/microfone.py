from sys import flags
from turtle import back


def abrir_mic():
    import speech_recognition as sr
    import unidecode
    from voz import maquina_voz
    comando = None
    flags = True
    while flags:
        audio = sr.Recognizer()
        with sr.Microphone() as source:
            print("Ouvindo")
            voz = audio.listen(source)
        try:
            comando = audio.recognize_google(voz, language="pt-BR")
            comando = comando.lower()
            comando = unidecode.unidecode(comando)
            flags = False

        except:
            print("Não escutei")
            maquina_voz('Desculpe não entendi, poderia repetir')
    print(comando)
    return comando
