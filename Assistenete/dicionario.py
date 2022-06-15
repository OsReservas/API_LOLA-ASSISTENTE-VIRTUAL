def diconario():
    import wikipedia
    from voz import maquina_voz
    from microfone1 import abrir_mic
    maquina_voz('Diga a palavra que deseja procurar')
    microfone = abrir_mic()
    procurar = microfone.replace("procure", " ")
    wikipedia.set_lang("pt")
    resultado = wikipedia.summary(procurar, 2)
    maquina_voz(resultado)
