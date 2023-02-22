from Megoldas import Megoldas


def main() -> None:
    # beolvasás
    phone: Megoldas = Megoldas('hivastest.txt')
    # print(len(phone.phone_calls))  # test hogy működik e a inicializálás

    print('3. feladat')
    print(phone.stat_print)

    print('4. Feladat')
    print(f'A leghosszabb ideig vonalban lévő hívó {phone.longest_call_line} sorban szerepel, a hívás hossza: {phone.longest_call_length} másodperc.')

    print("5. Feladat")
    input_numbers: str = input("Adjon meg egy idopontot! (ora perc masodperc) ")
    print(f'{"Nem volt beszélő" if phone.waiting_people_num(input_numbers) == 0 else f"A várakozók száma: {phone.waiting_people_num(input_numbers)} a beszélo a {phone.accepted_caller_num(input_numbers)}. hívó."}')

    print("6. Feladat")
    print(f'Az utolso telefonalo adatai a(z) {phone.call_for_all_hour}. sorban vannak, {phone.last_caller_wait_length} masodpercig vart.')


if __name__ == "__main__":
    main()
