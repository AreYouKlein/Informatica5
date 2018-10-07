e = int(input('aantal elektronen: '))

if e <= 2:
    print('De K-schil is de buitenste schil van een stabiel atoom met ' + str(e), 'elektronen.')
elif e > 2 and e <= 10:
    print('De L-schil is de buitenste schil van een stabiel atoom met ' + str(e), 'elektronen.')
elif e > 10 and e <= 28:
    print('De M-schil is de buitenste schil van een stabiel atoom met ' + str(e), 'elektronen.')
elif e > 28 and e <= 60:
    print('De N-schil is de buitenste schil van een stabiel atoom met ' + str(e), 'elektronen.')
elif e > 60 and e <= 92:
    print('De O-schil is de buitenste schil van een stabiel atoom met ' + str(e), 'elektronen.')
elif e > 92 and e <= 124:
    print('De P-schil is de buitenste schil van een stabiel atoom met ' + str(e), 'elektronen.')
else:
    print('De Q-schil is de buitenste schil van een stabiel atoom met ' + str(e), 'elektronen.')



