def nwd_odejmowanie(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

def nwd_modulo(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def nww(a, b):
    return (a * b) // nwd_modulo(a, b)

def main():
    try:
        liczba1 = int(input("Podaj pierwszą liczbę: "))
        liczba2 = int(input("Podaj drugą liczbę: "))
        print("NWD (odejmowanie):", nwd_odejmowanie(liczba1, liczba2))
        print("NWD (modulo):", nwd_modulo(liczba1, liczba2))
        print("NWW:", nww(liczba1, liczba2))
    except ValueError:
        print("Nieprawidłowa wartość. Wprowadź liczbę całkowitą.")

if __name__ == "__main__":
    main()