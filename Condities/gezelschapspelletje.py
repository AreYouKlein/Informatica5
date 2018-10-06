a1 = int(input('eerste dobbelsteen: '))
a2 = int(input('tweede dobbelsteen: '))
a3 = int(input('derde dobbelsteen: '))
v1 = int(input('vierde dobbelsteen: '))
v2 = int(input('vijfde dobbelsteen: '))
########################################################################################################################
if a1 >= a2 and a1 >= a3:
    x = a1
elif a2 >= a1 and a2 >= a3:
    x = a2
elif a3 >= a1 and a3 >= a2:
    x = a3
########################################################################################################################
if v1 >= v2:
    y = v1
else:
    y = v2
########################################################################################################################
if x == a1 and a2 >= a3:
    d = a2
elif x == a1 and a3 >= a2:
    d = a3
elif x == a2 and a1 >= a3:
    d = a1
elif x == a2 and a3 >= a1:
    d = a3
elif x == a3 and a1 >= a2:
    d = a1
elif x == a3 and a2 >= a1:
    d = a2
########################################################################################################################
if y == v1:
    e = v2
else:
    e = v1
########################################################################################################################
if y >= x and e >= d:
    print('aanvaller verliest 2 legers, verdediger verliest 0 legers')
elif x > y and d > e:
    print('aanvaller verliest 0 legers, verdediger verliest 2 legers')
else:
    print('aanvaller verliest 1 leger, verdediger verliest 1 leger')


