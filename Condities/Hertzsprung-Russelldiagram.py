k = float(input('wat is de temperatuur: '))
l = float(input('wat is de lichtkracht: '))
########################################################################################################################
if l >= 10000:
    print('superreuzen (a)')
elif l < 10000 and l > 1000:
    print('superreuzen (b)')
elif l < 1000 and l > 100 and k < 7500:
    print('heldere reuzen')
elif l < 100 and l > 10 and k < 6000:
    print('reuzen')