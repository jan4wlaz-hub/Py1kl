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

liczba1 = int(input("Podaj pierwszą liczbę: "))
liczba2 = int(input("Podaj drugą liczbę: "))
print(nwd_odejmowanie(liczba1, liczba2))
print(nwd_modulo(liczba1, liczba2))
print(nww(liczba1, liczba2))