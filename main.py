from Megoldas import Megoldas


def main() -> None:
    # beolvasás
    phone: Megoldas = Megoldas('hivastest.txt')
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
    input_numbers: str = input("Adjon meg egy idopontot! (ora perc masodperc) ")
    # print(phone.accepted_caller_num(input_numbers))
    # print(phone.waiting_people_num(input_numbers))
    # print(f'A várakozók száma: {phone.waiting_people_num(input_numbers)} a beszélo a {phone.accepted_caller_num(input_numbers)}. hívó.')
    print(f'{"Nem volt beszélő" if phone.waiting_people_num(input_numbers) == 0 else f"A várakozók száma: {phone.waiting_people_num(input_numbers)} a beszélo a {phone.accepted_caller_num(input_numbers)}. hívó."}')


if __name__ == "__main__":
    main()
