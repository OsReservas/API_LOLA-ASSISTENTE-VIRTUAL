def alarme():
    from microfone import abrir_mic
    from voz import maquina_voz
    from time import localtime
    import playsound

    maquina_voz('fale a hora que você quer despertar')
    H = int(abrir_mic())
    maquina_voz('fale o minuto que você quer despertar')
    M= int(abrir_mic())
    maquina_voz(f'O alarme ficou marcado para as {H} horas e {M} minutos')
    while True:
        if localtime().tm_hour == int(H) and localtime().tm_min == int(M):
            maquina_voz("ACORDE")
            playsound.playsound("despertador.mp3")
            break