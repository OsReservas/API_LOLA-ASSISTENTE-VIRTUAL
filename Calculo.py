import speech_recognition as sr
import random
#Função para ouvir e reconhecer a fala
def ouvir_microfone():
    #Habilita o microfone do usuário
    microfone = sr.Recognizer()
    
    #usando o microfone
    with sr.Microphone() as source:
        
        #Chama um algoritmo de reducao de ruidos no som
        microfone.adjust_for_ambient_noise(source)
        
        #Frase para o usuario dizer algo
        print("Diga alguma coisa: ")
        
        #Armazena o que foi dito numa variavel
        audio = microfone.listen(source)
        
    try:
        
        #Passa a variável para o algoritmo reconhecedor de padroes
        frase = microfone.recognize_google(audio,language='pt-BR')
        
        if 'somar' in frase:
            num1 = int(input('insira um numero: '))
            num2 = int(input('insira outro numero: '))
            cont= (num1+num2)

            print(f'Quanto é {num1} + {num2}')
            r = int(input('insira o resultado: '))
            if cont == r:
                print('resultado correto')
            else:
                print('resultado incorreto')

        if 'subtrair' in frase:
            num1 = int(input('insira um numero: '))
            num2 = int(input('insira outro numero: ')) 
            cont1= (num1-num2)
            cont2= (num2-num1)

            if num1>num2:
                print(f'Quanto é {num1} - {num2}')
                r = int(input('insira o resultado: '))
                if cont1 == r:
                    print('resultado correto')
                else:
                    print('resultado incorreto')
            elif num2>num1:
                print(f'Quanto é {num2} - {num1}')
                r = int(input('insira o resultado: '))
                if cont2 == r:
                    print('resultado correto')
                else:
                    print('resultado incorreto')
        if 'multiplicar' in frase:
            num1 = int(input('insira um numero: '))
            num2 = int(input('insira outro numero: '))

            cont= (num1*num2)
            print(f'Quanto é {num1} x {num2}')
            r = int(input('insira o resultado: '))
            if cont == r:
                print('resultado correto')
            else:
                print('resultado incorreto')
        if 'dividir' in frase:
            num1 = int(input('insira um numero: '))
            num2 = int(input('insira outro numero: '))
            cont= (num1/num2)

            print(f'Quanto é {num1} \ {num2}')
            r = float(input('insira o resultado: '))
            if cont == r:
                print('resultado correto')
            else:
                print('resultado incorreto')     
        
    #Se nao reconheceu o padrao de fala, exibe a mensagem
    except sr.UnkownValueError:
        print("Não entendi")
        
    return frase
ouvir_microfone()