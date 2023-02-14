from Megoldas import Megoldas


def main() -> None:
    # beolvasás
    phone: Megoldas = Megoldas('hivas.txt')
    # print(len(phone.phone_calls))  # test hogy működik e a inicializálás

    print('3. feladat')
    all_num: int = 0
    for number in range(8, 12):
        for e in phone.phone_calls:
            if e.First_hour == number:
                all_num += 1
        print(f'{number} óra {all_num} hívás')
        all_num = 0
        
    print('4. Feladat')
    hivas_hossz: int = 0
    sor_szamlalo: int = 0
    for e in phone.phone_calls:
        if e.hivas_hossz > hivas_hossz:
            hivas_hossz = e.hivas_hossz
    for e in phone.phone_calls:
        sor_szamlalo += 1
        if e.hivas_hossz == hivas_hossz:
            break
    print(f'A leghosszabb ideig vonalban lévő hívó {sor_szamlalo} sorban szerepel, a hívás hossza: {hivas_hossz} másodperc.')
    
    print("5. Feladat")
    input_szamok: str = input("Adjon meg egy idopontot! (ora perc masodperc) ")
    print(phone.felvett_hívás_száma(input_szamok))




if __name__ == "__main__":
    main()
