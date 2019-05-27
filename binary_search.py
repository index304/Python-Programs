

import random

a = 0
def wysz(p, k, tab, wart):
    p = 0
    while (k - p > 1 ):
        global a
        a = a + 1
        mid = int ((k + p)/2)
        print (a, " ) ", tab[mid])
        if tab[mid] >= wart:
            k = mid
        else:
            p = mid
    return k


numbers = []

print ("Wprowadz ilosc elementow w ciagu")
ilosc = int (input())

for x in range (0, ilosc):
    numbers.append (random.randint(1, 101))

print ("To są liczby w mojej tablicy")
numbers.sort ()
print (numbers)

losuj = random.randint(1, 101)
print ("Szukana liczba to: ", losuj)
print ("Szukana liczba jest tym elementem w tabeli lub jest mniejsza od niego: ", wysz(0, ilosc, numbers, losuj))
