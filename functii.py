a = int(input('a='))
b = int(input('b='))


def suma(a, b):
    s = a + b
    return s


def produs(a, b):
    p = a * b
    return p


def media(a, b):
    m = (a + b) / 2
    return m


def divizoriComuni(a, b):
    comun = []

    for i in range(1, int(max(a, b) / 2) + 1):
        if a % i == 0 and b % i == 0:
            comun.append(i)

    return comun


def maximdivizor():
    div = divizoriComuni(a, b)
    maxd = div[0]

    for i in range(1, len(div)):
        if div[i] > maxd:
            maxd = div[i]

    return maxd


def multiplicomuni(a, b):
    multiplia = []
    multiplib = []
    comun = []

    for i in range(1, max(a, b)):
        multiplia.append(a*i)
        multiplib.append(b*i)

    for i in multiplia:
        if i in multiplib:
            comun.append(i)

    return comun[0:5]


def minmultiple():
    multipli = multiplicomuni(a, b)
    minm = multipli[0]

    for i in range(1, len(multipli)):
        if multipli[i] < minm:
            minm = multipli[i]

    return minm


def minim(a, b):
    if (a < b):
        return a
    else:
        return b


def maxim(a, b):
    if (a > b):
        return a
    else:
        return b


def suma2(a, b):
    return str(a) + ' + ' + str(b) + ' = ' + str(suma(a, b))


def produs2(a, b):
    return str(a) + ' * ' + str(b) + ' = ' + str(produs(a, b))


def cifreidentice(a, b):
    cifre = []

    for i in str(a):
        for j in str(b):
            if i == j:
                cifre.append(i)

    return cifre


def cifrediferite(a, b):
    cifre = []

    for i in str(a):
        if i not in str(b):
            cifre.append(i)

    return cifre


def prietene(a, b):
    diva = []
    divb = []

    for i in range(1, int(a / 2) + 1):
        for j in range(1, int(b / 2) + 1):
            if a % i == 0:
                diva.append(i)
            if b % j == 0:
                divb.append(j)

    if len(diva) == len(divb):
        return "PRIETENE"
    else:
        return "Nu sunt prietene"


print(suma(a, b))
print(produs(a, b))
print(media(a, b))
print(maximdivizor())
print(minmultiple())
print(minim(a, b))
print(maxim(a, b))
print(suma2(a, b))
print(produs2(a, b))
print(divizoriComuni(a, b))
print(multiplicomuni(a, b))
print(cifreidentice(a, b))
print(cifrediferite(a, b))
print(prietene(a, b))
