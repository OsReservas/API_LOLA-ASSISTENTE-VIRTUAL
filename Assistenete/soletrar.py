def soletrar():
    from voz import maquina_voz
    from microfone1 import abrir_mic
    maquina_voz('Diga a palavra que deseja soletrar')
    microfone = abrir_mic()
    comando = microfone.replace("soletre", " ")
    for letra in comando:
        maquina_voz(letra)
