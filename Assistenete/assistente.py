def assistente():
    from microfone1 import abrir_mic
    from jogo1 import jogo
    from calculadora import calculo
    from tradutor import tradutor
    from voz import maquina_voz
    from soletrar import soletrar
    from dicionario import diconario
    from escovar import escovar_dentes
    from historia import historia
    from time import sleep
    from alarm import alarme
    maquina_voz('Olá, me chamo Lola!')
    while True:
        maquina_voz('Em que posso ajudar?')
        sleep(0.1)
        maquina_voz('podemos jogar pedra, papel e tesoura, calcular, traduzir do inglês para português')
        sleep(0.05)
        maquina_voz('Soletrar uma palavra, aprender escovar os dentes e também posso te contar uma história')
        sleep(0.05)
        maquina_voz('conhecer o significado de palavras com o dicionário ou posso ativar um alarme para você')
        sleep(0.05)
        maquina_voz('ou encerrar se você quiser!')
        microfone = abrir_mic()
        if 'jogar' in microfone:
            jogo()
        if 'calcular' in microfone:
            calculo()
        if 'traduzir' in microfone:
            tradutor()
        if 'soletrar' in microfone:
            soletrar()
        if 'dicionario' in microfone:
            diconario()
        if 'escovar' in microfone:
            escovar_dentes()
        if 'historia' in microfone:
            historia()
        if 'alarme' in microfone:
            alarme()
        if 'encerrar' in microfone:
            maquina_voz('Obrigado por brincar comigo! Até a próxima')
            break

assistente()