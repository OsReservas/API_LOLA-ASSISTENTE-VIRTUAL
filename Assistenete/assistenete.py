from microfone import abrir_mic
from voz import maquina_voz
from voz import maquina_voz_en
from jogo import jogo
from calculadora import calculo
from tradutor1 import tradutor


def assistente():
    microfone = abrir_mic()

    if 'jogo' in microfone:
        jogo()
    if 'calcular' in microfone:
        calculo()
    if 'tradutor' in microfone:
        tradutor()

