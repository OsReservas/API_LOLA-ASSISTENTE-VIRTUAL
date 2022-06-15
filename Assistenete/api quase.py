import playsound
import speech_recognition as sr
import pyaudio
import pyttsx3
import os

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

        elif 'bom dia' in frase:
            engine.say('Bom dia')
            engine.runAndWait()

        elif 'boa tarde' in frase:
            engine.say('boa tarde')
            engine.runAndWait()
        elif 'jogar' in frase:

            itens = ('pedra', 'papel', 'tesoura')
            computador = randint(0, 2)

            print('Vamos jogar Jokenpo!!!')
            maquina.say('Vamos jogar JOKÊNPO')
            sleep(2)
            print('-=-' * 15)
            print('''Faça sua jogada :
                            [0] Pedra
                            [1] Papel
                            [2] tesoura''')
            maquina.say('''Faça sua jogada!
                            Diga 0 para pedra
                            Diga 1 para papel
                            Diga 2 para tesoura''')
            print('-=-' * 15)
            sleep(2)
            jogador = int(input('Qual a sua jogada? '))
            maquina.say('Qual sua jogada?')

            def ouvir_mic():
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
                    frase = str(frase)
                    if '1' and '2' and '3' in frase:

                        sleep(2)
                        print('JO')
                        sleep(1.3)
                        print('KEN')
                        sleep(1.3)
                        print('PO')
                        sleep(1.3)
                        print('-=-' * 15)
                        print(f'Computador jogou: {itens[computador].upper()}')
                        print(f'Jogador jogou: {itens[frase].upper()}')
                        print('-=-' * 15)
                        sleep(1)
                        print('PROCESSANDO...')
                        sleep(3)
                        if computador == 0:
                            if jogador == 0:
                                print('EMPATE')
                            elif jogador == 1:
                                print('JOGADOR GANHOU')
                            elif jogador == 2:
                                print('COMPUTADOR GANHOU')
                            else:
                                print('OPCAO ESCOLHIDA INVALIDA')
                        elif computador == 1:
                            if jogador == 0:
                                print('COMPUTADOR GANHOU')
                            elif jogador == 1:
                                print('EMPATE')
                            elif jogador == 2:
                                print('JOGADOR GANHOU')
                            else:
                                print('OPCAO ESCOLHIDA INVALIDA')
                        elif computador == 2:
                            if jogador == 0:
                                print('JOGADOR GANHOU')
                            elif jogador == 1:
                                print('COMPUTADOR GANHOU')
                            elif jogador == 2:
                                print('EMPATE')
                            else:
                                print('OPCAO ESCOLHIDA INVALIDA')
    # Se nao reconheceu o padrao de fala, exibe a mensagem
    except sr.UnknownValueError:
        print("Não entendi")

    return

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
    except sr.UnknownValueError:
        print("Não entendi")

    return frase
ouvir_microfone()