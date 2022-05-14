from googletrans import Translator
from microfone import abrir_mic
from voz import *


def tradutor():
    maquina_voz("O que deseja traduzir?")
    print("Ouvindo")
    trad = Translator()
    traducao = trad.translate(abrir_mic(), dest="en")
    maq_trad = maquina_voz_en(traducao.text)
    return maq_trad

