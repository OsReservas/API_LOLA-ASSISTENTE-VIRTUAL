def historia():
    import microfone1
    import playsound
    from voz import maquina_voz
    from time import sleep
    maquina_voz('Podemos ouvir a história dos 3 Porquinhos, da Chapeuzinho Vermelho ou do Patinho feio')
    maquina_voz('Oque vamos ouvir? ')
    mic = microfone1.abrir_mic()
    if 'patinho' in mic:
        playsound.playsound('patinho.wav')
    if 'chapeuzinho' in mic:
        playsound.playsound('chapeuzinho.wav')
    if 'porquinho' in mic:
        playsound.playsound('porquinho.wav')

