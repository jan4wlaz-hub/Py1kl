def caesar_cipher(text: str, shift: int) -> str:
    result = []
    
    for char in text:
        # Sprawdzamy małe litery (ASCII: 97 do 122)
        if 'a' <= char <= 'z':
            # Odejmujemy 97, żeby operować na zakresie 0-25
            shifted = (ord(char) - 97 + shift) % 26
            # Dodajemy 97 z powrotem, by wrócić do właściwego kodu ASCII
            result.append(chr(shifted + 97))
            
        # Sprawdzamy wielkie litery (ASCII: 65 do 90)
        elif 'A' <= char <= 'Z':
            # Odejmujemy 65, żeby operować na zakresie 0-25
            shifted = (ord(char) - 65 + shift) % 26
            # Dodajemy 65 z powrotem
            result.append(chr(shifted + 65))
            
        else:
            # Reszta znaków (spacje, wykrzykniki, cyfry) zostaje bez zmian
            result.append(char)
            
    return "".join(result)

################

tekst=input("podaj txt")
przesuniecie=int(input("podaj przesuniecie"))

zaszyfrowany = caesar_cipher(tekst, przesuniecie)
odszyfrowany = caesar_cipher(zaszyfrowany, -przesuniecie)

print(f"Oryginał: {tekst}")
print(f"Szyfr:    {zaszyfrowany}")
print(f"Odszyfr:  {odszyfrowany}")