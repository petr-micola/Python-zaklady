'''
Konstanty v Pythonu

Konstanta je vlastně speciální typ proměnné, jejíž hodnota nemůže být změněna.
V Pythonu jsou konstanty obvykle deklarovány a přiřazovány v modulu, který bývá importován do souboru aplikace.
Konstanty jsou pojmenovány velkými písmeny a jednotlivá slova jsou oddělována podtržítky.
'''

EARTH_GRAVITY = 9.807 #? normální pozemské tíhové zrychlení
MOON_GRAVITY = 1.62 #? měsíční gravitace
SPEED_OF_LIGHT = 299792458 #? rychlost světla ve vakuu
SPEED_OF_SOUND = 343 #? rychlost zvuku při teplotě 20 °C v suchém vzduchu

''' 
Úkol:
1. Doplňte správně hodnoty uvedených konstant.
2. Doplňte physics.py o několik výpočtových funkcí (opatřené docstrings), v nichž využijete minimálně všechny výše uvedené konstanty.
Samozřejmě můžete své řešení rozšířit i o jiné fyzikální konstanty.
3. Vytvořte z tohoto souboru samostatný modul v Pythonu podle návodu, který si sami najdete na internetu.      
4. Vytvořte vlastní aplikaci myapp.py, do níž tento modul importujte. Demonstrujte v ní na jednoduchých příkladech využití vámi
připravených funkcí.  
'''


def gravitacniSilaZeme(m):
    '''
    Funkce vypočítá gravitaci na Zemi, kterou je těleso o hmotnosti m přitahováno.
    '''
    return m * EARTH_GRAVITY


def gravitacniSilaMesic(m):
    '''
    Funkce vypočítá gravitaci na Měsíci, kterou je těleso o hmotnosti m přitahováno.
    '''
    return m * MOON_GRAVITY


def energie(m):
    '''
    Funkce vypočítá energii tělesa o hmotnosti m.
    '''
    return m * SPEED_OF_LIGHT ** 2


def vzdalenostZvuk(t):
    '''
    Funkce vypočítá vzdálenost, kterou urazil zvuk za čas t.
    '''
    return SPEED_OF_SOUND * t
