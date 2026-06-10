

def nwd_odejmowanie(a,b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

def nwd_modulo(a,b):
    while b != 0:
        a, b = b, a % b
    return a

def nww(a,b):
    return (a * b) // nwd_modulo(a,b)

def maksimum(lista):
    max = lista[0]
    for i in range(1, len(lista)):
        if lista[i] > max:
            max = lista[i]
    return max

def minimum(lista):
    min = lista[0]
    for i in range(1, len(lista)):
        if lista[i] < min:
            min = lista[i]
    return min

def liczenie_ilosci_liter(tekst,znak):
    ilosc_liter = 0
    for litera in tekst:
        if litera==znak:
            licznik+=1
        else:
            ilosc_liter[litera] = 1
    return ilosc_liter

def gaderypoluki(tekst):
    wynik = ""
    for litera in tekst:
        if litera in "aeiouyAEIOUY":
            wynik += "g"
        elif litera in "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ":
            wynik += "d"
        else:
            wynik += litera
    return wynik

print(ord("a"))
tekst = input("Podaj tekst: ")
litera = input("Podaj literę: ")
print(liczenie_ilosci_liter(tekst))
print(f"Ilość wystąpień litery {litera}: {liczenie_ilosci_liter(tekst).get(litera, 0)}")
print (ord(liczba1))
print (ord(liczba2))
liczba1 = int(input("Podaj pierwszą liczbę: "))
liczba2 = int(input("Podaj drugą liczbę: "))
lista = [liczba1, liczba2]
print(nwd_odejmowanie(liczba1, liczba2))
print(nwd_modulo(liczba1, liczba2))
print(nww(liczba1, liczba2))
print (maksimum(lista))
print (minimum(lista))