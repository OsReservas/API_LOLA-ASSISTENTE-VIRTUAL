def historia():
    import microfone
    import playsound
    from voz import maquina_voz
    from time import sleep
    maquina_voz('Podemos ouvir a história dos 3 Porquinhos, da Chapeuzinho Vermelho ou do Patinho feio')
    maquina_voz('Oque vamos ouvir? ')
    mic = microfone.abrir_mic()
    if 'patinho' in mic:
        playsound.playsound('patinho.mp3')
    if 'chapeuzinho' in mic:
        playsound.playsound('chapeuzinho.mp3')
    if 'porquinho' in mic:
        playsound.playsound('porquinho.mp3')


