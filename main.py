import NWD_NWW
import sito_erastostelesa
import module_27VI2026
import iteracja_rekurencja
import obliczanie_silni_rekurencyjnie_i_iteracyjnie
import szyfr_cezara
import z_dziesietnego_binarny_i_odwrotnie
import tekstowe_funkcje
import rozklad_na_czynniki_pierwsze

def main():
    while True:
        print("\n" + "="*50)
        print("MENU - Wybierz program do uruchomienia:")
        print("="*50)
        print("1. NWD_NWW")
        print("2. sito_erastostelesa")
        print("3. module_27VI2026")
        print("4. iteracja_rekurencja")
        print("5. obliczanie_silni_rekurencyjnie_i_iteracyjnie")
        print("6. szyfr_cezara")
        print("7. z_dziesietnego_binarny_i_odwrotnie")
        print("8. tekstowe_funkcje")
        print("9. rozklad_na_czynniki_pierwsze")
        print("0. Wyjście")
        print("="*50)
        
        choice = input("Podaj numer programu (0-7): ").strip()
        
        if choice == "1":
            NWD_NWW.main() if hasattr(NWD_NWW, 'main') else print("Brak funkcji main w module NWD_NWW")
        elif choice == "2":
            sito_erastostelesa.main() if hasattr(sito_erastostelesa, 'main') else print("Brak funkcji main w module sito_erastostelesa")
        elif choice == "3":
            module_27VI2026.main() if hasattr(module_27VI2026, 'main') else print("Brak funkcji main w module module_27VI2026")
        elif choice == "4":
            iteracja_rekurencja.main() if hasattr(iteracja_rekurencja, 'main') else print("Brak funkcji main w module iteracja_rekurencja")
        elif choice == "5":
            obliczanie_silni_rekurencyjnie_i_iteracyjnie.main() if hasattr(obliczanie_silni_rekurencyjnie_i_iteracyjnie, 'main') else print("Brak funkcji main w module obliczanie_silni_rekurencyjnie_i_iteracyjnie")
        elif choice == "6":
            szyfr_cezara.main() if hasattr(szyfr_cezara, 'main') else print("Brak funkcji main w module szyfr_cezara")
        elif choice == "7":
            z_dziesietnego_binarny_i_odwrotnie.main() if hasattr(z_dziesietnego_binarny_i_odwrotnie, 'main') else print("Brak funkcji main w module z_dziesietnego_binarny_i_odwrotnie")
        elif choice == "8":
            tekstowe_funkcje.main() if hasattr(tekstowe_funkcje, 'main') else print("Brak funkcji main w module tekstowe_funkcje")
        elif choice == "9":
            rozklad_na_czynniki_pierwsze.main() if hasattr(rozklad_na_czynniki_pierwsze, 'main') else print("Brak funkcji main w module rozklad_na_czynniki_pierwsze")
        elif choice == "0":
            print("Do widzenia!")
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")


if __name__ == "__main__":
    main()    

