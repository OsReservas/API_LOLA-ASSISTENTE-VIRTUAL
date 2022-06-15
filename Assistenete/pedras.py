import speech_recognition as sr
import pyttsx3
import wikipedia
import datetime
import playsound
from random import randint
from time import sleep

audio = sr.Recognizer()
maquina = pyttsx3.init()
voices = maquina.getProperty('voices')
maquina.setProperty('voice', voices[-2].id)


def executa_comando(pular_dora):
    with sr.Microphone() as source:
        print("Ouvindo")
        voz = audio.listen(source)
    try:
        comando = audio.recognize_google(voz, language="pt-BR")
        comando = comando.lower()

        if "lola" in comando or pular_dora == True:
            comando = comando.replace("dora", "")
            if 'bom dia' in comando.lower():
                maquina.say('bom dia! o que vamos fazer?')
            elif 'boa tarde' in comando.lower():
                maquina.say('boa tarde! o que vamos fazer?')
            elif 'boa noite' in comando.lower():
                maquina.say('boa noite! o que vamos fazer?')
            elif "horas" in comando:
                hora = datetime.datetime.now().strftime("%H:%M")
                print(hora)
                maquina.say("Agora são " + hora)
            elif "procure " in comando:
                procurar = comando.replace("procure", " ")
                wikipedia.set_lang("pt")
                resultado = wikipedia.summary(procurar, 2)
                maquina.say(resultado)
            elif "soletre" in comando:
                comando = comando.replace("soletre", " ")
                for letra in comando:
                    maquina.say(letra)
            elif "patinho" in comando:
                comando = comando.replace("historia do", "")
                playsound.playsound('patinho.mp3')
            elif "chapeuzinho" in comando:
                comando = comando.replace("historia da", "")
                playsound.playsound('chapeuzinho.mp3')
            elif "porquinho" in comando:
                comando = comando.replace("historia do", "")
                playsound.playsound('porquinho.mp3')
            elif 'jogar' in comando:

                itens = ('pedra', 'papel', 'tesoura')
                computador = randint(0,2)

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

                        if 1 and 2 and 3 in frase:

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

            elif "sair" in comando:
                print("Tchau amiguinho")
                return

            maquina.runAndWait()
            print("Você disse: " + comando)
            executa_comando(True)
        else:
            print("não detectou dora")
    except:
        print("Não escutei")
        executa_comando(pular_dora)


executa_comando(False)