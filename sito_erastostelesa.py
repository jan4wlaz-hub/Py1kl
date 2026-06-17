def sito_eratostelesa(n):
    if n < 2:
        return []

    sieve = [True] * (n + 1)
    sieve[0] = False
    sieve[1] = False

    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    return [i for i, is_prime in enumerate(sieve) if is_prime]


def main():
    try:
        num = int(input("Podaj maksymalną liczbę do sprawdzenia: "))
        if num < 0:
            print("Podano liczbę ujemną. Będę liczyć dla jej wartości bezwzględnej.")
            num = abs(num)

        primes = sito_eratostelesa(num)
        if primes:
            print(f"Liczby pierwsze od 2 do {num}:")
            print(primes)
        else:
            print("Brak liczb pierwszych w tym zakresie.")
    except ValueError:
        print("To nie jest liczba!")
    except Exception as e:
        print(f"Wystąpił nieoczekiwany błąd: {e}")

if __name__ == "__main__":
    main()