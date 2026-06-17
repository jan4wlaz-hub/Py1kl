

def silnia(n):
    wynik = 1
    for i in range(1, n + 1):
        wynik *= i
    return wynik


def silnia_rekurencyjna(n):
    if n == 0 or n == 1:
        return 1
    return n * silnia_rekurencyjna(n - 1)


def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_iteracyjnie(n):
    if n <= 0:
        return []
    if n == 1:
        return [1]
    seq = [1, 1]
    for _ in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq


def main():
    try:
        n = int(input("Podaj liczbę: "))
    except ValueError:
        print("Nieprawidłowa wartość. Wprowadź liczbę całkowitą.")
        return

    print("Silnia iteracyjna:", silnia(n))
    print("Silnia rekurencyjna:", silnia_rekurencyjna(n))
    print("Ciąg Fibonacciego iteracyjnie:", fibonacci_iteracyjnie(n))
    print("N-ty wyraz Fibonacciego rekurencyjnie:", fibonacci(n))

if __name__ == "__main__":
    main()