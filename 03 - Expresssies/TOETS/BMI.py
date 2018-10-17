# De variabelen
l = float(input('Geef de lengte van beide personen: '))
n_1 = input('Geef de naam van de eerste persoon: ')
g_1 = float(input('geef het gewicht van de eerste persoon: '))
n_2 = input('Geef de naam van de tweede persoon: ')
g_2 = float(input('Geef het gewicht van de tweede persoon: '))
# Welke naam heeft het hoogste BMI?
if g_1 > g_2:
    n = n_1
else:
    n = n_2
# Bereken BMI
BMI_1 = g_1 / (l ** 2)
BMI_2 = g_2 / (l ** 2)
# Welke waarde is het grootst?
BMI = max(BMI_1, BMI_2)
# Oplossing
if BMI < 18.5:
    message = (n, 'heeft het hoogste BMI (' + '{:.2f}'.format(BMI), ') en heeft ondergewicht.')
elif BMI < 25 and BMI >= 18.5:
    message = str(n) heeft het hoogste BMI (str(BMI))
elif BMI < 30 and BMI >= 25:
    message = (n, 'heeft het hoogste BMI (' + '{:.2f}'.format(BMI), ') en heeft overgewicht.')
else:
    message = (n, 'heeft het hoogste BMI (' + '{:.2f}'.format(BMI), ') en is obees.')
print(message)


