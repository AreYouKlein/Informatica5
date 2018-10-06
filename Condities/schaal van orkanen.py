x = int(input('de windsnelheid is: '))

if x >= 250:
    print('categorie 5')
elif x < 250 and x >= 210:
    print('categorie 4')
elif x < 210 and x >= 178:
    print('categorie 3')
elif x < 178 and x >= 154:
    print('categorie 2')
elif x < 154 and x >= 119:
    print('categorie 1')
else:
    print('geen orkaan')
