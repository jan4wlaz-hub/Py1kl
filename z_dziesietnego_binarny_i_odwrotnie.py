def dziesietny_na_binarny():
    try:
        liczba = int(input("Podaj liczbę do konwersji z dziesiętnego na binarny: "))
    except ValueError:
        print("Nieprawidłowa liczba.")
        return

    binarny = ""
    temp = liczba
    if temp == 0:
        binarny = "0"
    while temp > 0:
        binarny = str(temp % 2) + binarny
        temp //= 2
    print(f"{liczba} w systemie binarnym to: {binarny}")

def binarny_na_dziesietny():
    binarny_input = input("Podaj liczbę w systemie binarnym: ")
    try:
        dziesietny = int(binarny_input, 2)
    except ValueError:
        print("Nieprawidłowy format liczby binarnej.")
        return
    print(f"{binarny_input} w systemie dziesiętnym to: {dziesietny}")


def main():
    dziesietny_na_binarny()
    binarny_na_dziesietny()

if __name__ == "__main__":
    main()