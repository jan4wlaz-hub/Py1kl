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