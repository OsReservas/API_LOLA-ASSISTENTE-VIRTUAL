from voz import *
def tradutor():
    from googletrans import Translator
    from microfone1 import abrir_mic
    maquina_voz("Olá, o que deseja traduzir?")
    mic = abrir_mic()
    trad = Translator()
    traducao = trad.translate(mic, dest="en")
    if not mic:
        return False
    else:
        maquina_voz(f"A tradução da palavra {mic} pra inglês é ")
        maq_trad = maquina_voz_en(traducao.text)

