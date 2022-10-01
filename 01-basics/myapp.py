body = 0

print('''Jednoduchý test z českého jazyka.
---------------------------------''')

print('Sněhuláci stál_.')
pismeno = input('Doplňte písmeno: ')
if pismeno == 'i':
    body += 1

print('''1) Zapomněl jsem na datový typ FLOAT.
2) Zapoměl jsem na datový typ FLOAT.
3) Zapoměl jsem na datový tip FLOAT.
4) Zapomněl jsem na datový tip FLOAT.''')
cislo = input('Zadejte číslo pravopisně správně napsané věty: ')
if int(cislo) == 1:
    body += 1

print('Navštívil (Ch/ch)rám (S/s)vatého (V/v)íta v (P/p)raze.')
pocet = input('Zadejte číslo počtu velkých písmen v této větě: ')
if int(pocet) == 3:
    body += 1

print('Dosáhli jste maximálního počtu bodů :).' if body == 3 else 'Získali jste {} bodů.'.format(body))
