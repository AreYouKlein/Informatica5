a = float(input('De lengte van de eerste rechkshoekzijde: '))
b = float(input('De lengte van de tweede rechtshoekzijde: '))

a = '{:.2f}'.format(a)
b = '{:.2f}'.format(b)


from math import sqrt


c = sqrt((float(a) ** 2) + (float(b) ** 2))
c = '{:.2f}'.format(c)
print('In een rechthoekige driehoek met rechthoekszijden a = ' + str(a), 'en b = ' + str(b), 'is de schuine zijde ' + str(c))

