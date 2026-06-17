def rozklad_na_czynniki(n):
    if n < 2:
        return []
    czynniki = []
    dzielnik = 2
    while dzielnik * dzielnik <= n:
        while n % dzielnik == 0:
            czynniki.append(dzielnik)
            n //= dzielnik
        dzielnik += 1 if dzielnik == 2 else 2
    if n > 1:
        czynniki.append(n)
    return czynniki


def main():
    try:
        liczba = int(input("Podaj liczbę do rozkładu na czynniki pierwsze: "))
    except ValueError:
        print("Nieprawidłowa wartość. Wprowadź liczbę całkowitą.")
        return

    czynniki = rozklad_na_czynniki(liczba)
    if not czynniki:
        print("Liczba musi być większa niż 1, aby miała czynniki pierwsze.")
    else:
        print(f"Rozkład na czynniki pierwsze dla {liczba}: {czynniki}")


if __name__ == "__main__":
    main()
