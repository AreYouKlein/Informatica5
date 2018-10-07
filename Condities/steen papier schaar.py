speler1 = str(input('Speler 1 kiest voor: '))
speler2 = str(input('Speler 2 kiest voor: '))

if speler1 == 'blad' and speler2 == 'steen':
    print('speler 1 wint')
elif speler1 == 'blad' and speler2 == 'schaar':
    print('speler 2 wint')
elif speler1 == 'steen' and speler2 == 'blad':
    print('speler 2 wint')
elif speler1 == 'steen' and speler2 == 'schaar':
    print('speler 1 wint')
elif speler1 == 'schaar' and speler2 == 'steen':
    print('speler 2 wint')
elif speler1 == 'schaar' and speler2 == 'blad':
    print('speler 1 wint')
else:
    print('onbeslist')
