'''
Iteracja

1. Stwórz program służący do obliczania silni za pomocą pętli.

2. Stwórz program wypisujący wszystkie liczby od 1 do 100, ale:

a. Jeżeli liczba podzielna jest przez 3 – wypisz słowo „Fizz”

b. Jeżeli liczba podzielna jest przez 5 – wypisz słowo „Buzz”

c. Jeżeli liczba podzielna jest jednocześnie przez 3 i 5 – wypisz „FizzBuzz”

3. Stwórz program znajdujący najmniejszą wartość z listy.

4. Stwórz program odwracający podany ciąg znaków np. słowo „owca” powinno zostać zamienione na „acwo”.

5. Stwórz program rysujący odwrócony trójkąt złożony z symboli „*”.

6. Stwórz program zliczający wystąpienia danej litery w podanym ciągu.

7. Stwórz program wczytujący liczby całkowite aż do wystąpienia liczby niedodatniej, a następnie obliczający średnią wprowadzonych liczb.

8. Stwórz program wypisujący na ekranie tabliczkę mnożenia liczb naturalnych od 1 do 20.

9. Stwórz program wypisujący na ekranie szachownicę złożoną ze znaków „O” i „X” ułożonych naprzemiennie,

10. Stwórz program obliczający kolejne wartości ciągu Fibonacciego.

Rekurencja

1. Stwórz program, który wypisze liczby od 1 do n rosnąco.

2. Stwórz program obliczający silnię podanej liczby.

3. Stwórz program obliczanie kolejnych wartości ciągu Fibonacciego.

4. Stwórz program odwracający podany ciąg znaków np. słowo „owca” powinno zostać zamienione na „acwo”.

5. Stwórz program sumujący wszystkie elementy listy.



'''



#1
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

#2
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
#3
def najmniejsza_wartosc(lista):
    if not lista:
        return None
    najmniejsza = lista[0]
    for liczba in lista:
        if liczba < najmniejsza:
            najmniejsza = liczba
    return najmniejsza

#4
def odwroc_ciag(ciag):
    odwrocony = ""
    for i in range(len(ciag) - 1, -1, -1):
        odwrocony += ciag[i]
    return odwrocony

#1 rekurencja
import sys

def licz_rosnaco(n):
    if n < 1:
        return
    
    if n == 1:
        print(1)
    else:
        licz_rosnaco(n - 1)
        print(n)

try:
    liczba = int(input("Podaj liczbę: "))
    licz_rosnaco(liczba)
except RecursionError:
    print("i'm actually not sure about that (⁠๑⁠•⁠﹏⁠•⁠) - liczba jest za duża dla rekurencji!")
except Exception as e:
    print(f"Wystąpił błąd....")

def wypisz_rosnaco(n):
    if n < 1:
        return
    wypisz_rosnaco(n - 1)
    print(n)

#2 rekurencja
def silnia_rekurencyjna(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * silnia_rekurencyjna(n - 1)