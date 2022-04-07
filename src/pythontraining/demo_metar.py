from metar import Metar

example = """METAR EHEH 071355Z AUTO 26021G37KT 210V340 9999 -RA FEW025CB SCT043
BKN047 10/04 Q0986
BLU TEMPO 26030G43KT 4000 SHRA FEW010 SCT015CB BKN016="""

obj = Metar.Metar(example)

print(obj)
