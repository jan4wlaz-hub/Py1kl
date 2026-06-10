
def main():
    while True:
        print("\nWybierz program do uruchomienia:")
        print("1. NWD, NWW, ")
        print("2. Program 2")
        print("3. Program 3")
        print("4. Wyjdź")
        choice = input("Podaj numer programu: ")    

#tasks:
#Szukanie najmniejszego lub największego elementu w liście, 
#Odwracanie kolejności liter w podanym wyrazie, 
#Zliczanie wystąpień podanego znaku w tekście, 
'''

def liczenie_ilosci_liter(tekst,znak):
    ilosc_liter = 0
    for litera in tekst:
        if litera==znak:
            licznik+=1
        else:
            ilosc_liter[litera] = 1
    return ilosc_liter
    
    
def maksimum(lista):
    max = lista[0]
    for i in range(1, len(lista)):
        if lista[i] > max:
            max = lista[i]
    return max

def minimum(lista):
    min = lista[0]
    for i in range(1, len(lista)):
        if lista[i] < min:
            min = lista[i]
    return min

    '''