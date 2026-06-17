def dziesietny_na_binarny ():
    liczba = int(input("Podaj liczbe do konwersji z dziesietnego na binarny: "))
    # Konwersja z dziesietnego na binarny
    binarny = ""
    temp = liczba
    while temp > 0:
        binarny = str(temp % 2) + binarny
        temp = temp // 2
    print(f"{liczba} w systemie binarnym to: {binarny}")

def binarny_na_dziesietny():
    # Konwersja z binarnego na dziesietny
    binarny_input = input("Podaj liczbe w systemie binarnym: ")
    dziesietny = int(binarny_input, 2)
    print(f"{binarny_input} w systemie dziesietnym to: {dziesietny}")

if __name__ == "__main__":
    dziesietny_na_binarny()
    binarny_na_dziesietny()