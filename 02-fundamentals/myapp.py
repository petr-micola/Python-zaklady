import physics

hmotnost = int(input('Zadejte hmotnost: '))

print('Těleso s hmotností', hmotnost, 'bude na Zemi přitahováno silou', physics.gravitacniSilaZeme(hmotnost),
      'N | na Měsíci silou', physics.gravitacniSilaMesic(hmotnost), 'N | energie tohoto tělesa je',
      physics.energie(hmotnost), 'MJ.')

cas = int(input('Zadejte čas v sekundách: '))

print('Zvuk za', cas, 's urazí vzdálenost', physics.vzdalenostZvuk(cas), 'm.')
