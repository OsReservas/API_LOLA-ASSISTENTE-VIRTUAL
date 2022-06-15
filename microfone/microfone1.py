def abrir_mic():
    import speech_recognition as sr
    import unidecode
    from voz import maquina_voz
    from time import sleep
    comando = None
    flags = True
    while flags:
        audio = sr.Recognizer()
        with sr.Microphone() as source:
            sleep(0.5)
            maquina_voz("Ouvindo")
            voz = audio.listen(source)
        try:
            comando = audio.recognize_google(voz, language="pt-BR")
            comando = comando.lower()
            comando = unidecode.unidecode(comando)
            flags = False
        except:
            maquina_voz('Desculpe não entendi, poderia repetir?')
    print(comando)
    return comando

abrir_mic()