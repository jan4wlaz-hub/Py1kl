'''
Generowanie wyrazów ciągu Fibonacciego iteracyjne, 
Generowanie wyrazów ciągu Fibonacciego rekurencyjnie, 
Obliczanie silni iteracyjnie, 
Obliczanie silni rekurencyjnie, '''

#silnia iteracyjnie
def silnia(n):
    wynik = 1
    for i in range(1, n + 1):
        wynik *= i
    return wynik
n=input("Podaj liczbę: ")
print(silnia(n))

def silnia_rekurencyjna(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * silnia_rekurencyjna(n - 1)
n=input("Podaj liczbę: ")
print(silnia_rekurencyjna(n))

#2 silnia rekurencyjnie
def silnia_rekurencyjna(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * silnia_rekurencyjna(n - 1)
    
#3 fibbonacci rekurencyjnie
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)