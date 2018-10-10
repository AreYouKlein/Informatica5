a = float(input('De lengte van de eerste rechkshoekzijde: '))
b = float(input('De lengte van de tweede rechtshoekzijde: '))




from math import sqrt


c = sqrt((float(a) ** 2) + (float(b) ** 2))
print('In een rechthoekige driehoek met rechthoekszijden a = ' + '{:.2f}'.format(a), 'en b = ' + '{:.2f}'.format(b), 'is de schuine zijde ' + '{:.2f}'.format(c))

