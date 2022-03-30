import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-2].id)

numero1 = float(input('digite um numero: '))
operacao = input('digite o operador: ')
numero2 = float(input('digite outro numero: '))



if operacao == '+':
    print(f'{numero1} + {numero2} = {numero1 + numero2}')
    engine.say(f'{numero1} mais {numero2} = {numero1 + numero2}')
    engine.runAndWait()
elif operacao == '-':
    print(f'{numero1} - {numero2} = {numero1 - numero2}')
    engine.say(f'{numero1} menos {numero2} = {numero1 - numero2}')
    engine.runAndWait()
elif operacao == '/':
    print(f'{numero1} / {numero2} = {numero1/numero2}')
    engine.say(f'{numero1} dividido por {numero2} = {numero1 / numero2}')
    engine.runAndWait()
elif operacao == '*':
    print(f'{numero1} + {numero2} = {numero1 * numero2}')
    engine.say(f'{numero1} vezes {numero2} = {numero1 * numero2}')
    engine.runAndWait()


