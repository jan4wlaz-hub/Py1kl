def liczenie_ilosci_liter(tekst, znak):
    """Zlicza, ile razy w tekście występuje podany znak."""
    return sum(1 for litera in tekst if litera == znak)


def maksimum(lista):
    """Zwraca największy element listy."""
    if not lista:
        raise ValueError("Lista nie może być pusta")
    max_wartosc = lista[0]
    for element in lista[1:]:
        if element > max_wartosc:
            max_wartosc = element
    return max_wartosc


def minimum(lista):
    """Zwraca najmniejszy element listy."""
    if not lista:
        raise ValueError("Lista nie może być pusta")
    min_wartosc = lista[0]
    for element in lista[1:]:
        if element < min_wartosc:
            min_wartosc = element
    return min_wartosc


def main():
    tekst = input("Podaj tekst: ")
    znak = input("Podaj znak do zliczenia: ")
    if len(znak) != 1:
        print("Wprowadź dokładnie jeden znak.")
        return

    print("Liczba wystąpień:", liczenie_ilosci_liter(tekst, znak))

    lista = input("Podaj liczby rozdzielone spacją: ").split()
    try:
        liczby = [int(x) for x in lista]
    except ValueError:
        print("Nieprawidłowy format liczb.")
        return

    print("Maksimum:", maksimum(liczby))
    print("Minimum:", minimum(liczby))


if __name__ == "__main__":
    main()
