'''
Iteracja

1. Stwórz program służący do obliczania silni za pomocą pętli.

2. Stwórz program wypisujący wszystkie liczby od 1 do 100, ale:

a. Jeżeli liczba podzielna jest przez 3 – wypisz słowo „Fizz”

b. Jeżeli liczba podzielna jest przez 5 – wypisz słowo „Buzz”

c. Jeżeli liczba jest jednocześnie przez 3 i 5 – wypisz „FizzBuzz”

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

def silnia(n):
    wynik = 1
    for i in range(1, n + 1):
        wynik *= i
    return wynik


def silnia_rekurencyjna(n):
    if n == 0 or n == 1:
        return 1
    return n * silnia_rekurencyjna(n - 1)


def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)


def najmniejsza_wartosc(lista):
    if not lista:
        return None
    najmniejsza = lista[0]
    for liczba in lista:
        if liczba < najmniejsza:
            najmniejsza = liczba
    return najmniejsza


def odwroc_ciag(ciag):
    odwrocony = ''
    for i in range(len(ciag) - 1, -1, -1):
        odwrocony += ciag[i]
    return odwrocony


def licz_rosnaco(n):
    if n < 1:
        return
    if n == 1:
        print(1)
        return
    licz_rosnaco(n - 1)
    print(n)


def main():
    print('Wybierz działanie modułu iteracja_rekurencja:')
    print('1. Oblicz silnię iteracyjnie i rekurencyjnie')
    print('2. Wypisz FizzBuzz od 1 do 100')
    print('3. Odwróć ciąg znaków')
    print('4. Wypisz liczby od 1 do n rosnąco')
    print('0. Powrót')

    choice = input('Podaj numer opcji: ').strip()
    if choice == '1':
        try:
            n = int(input('Podaj liczbę: '))
            print('Silnia iteracyjna:', silnia(n))
            print('Silnia rekurencyjna:', silnia_rekurencyjna(n))
        except ValueError:
            print('Nieprawidłowa wartość. Wprowadź liczbę całkowitą.')
    elif choice == '2':
        fizzbuzz()
    elif choice == '3':
        text = input('Podaj ciąg znaków: ')
        print('Odwrócony ciąg:', odwroc_ciag(text))
    elif choice == '4':
        try:
            n = int(input('Podaj liczbę: '))
            licz_rosnaco(n)
        except ValueError:
            print('Nieprawidłowa wartość. Wprowadź liczbę całkowitą.')
    elif choice == '0':
        return
    else:
        print('Nieznana opcja.')

if __name__ == '__main__':
    main()
