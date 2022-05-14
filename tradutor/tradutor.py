from googletrans import Translator
from defs.microfone import abrir_mic
from defs.voz import *


def tradutor():
    maquina_voz("O que deseja traduzir?")
    mic = abrir_mic()
    trad = Translator()
    traducao = trad.translate(mic, dest="en")
    if not mic:
        return False
    else:
        maquina_voz(f"A tradução da palavra {mic} pra inglês é ")
        maq_trad = maquina_voz_en(traducao.text)
tradutor()
