from Megoldas import Megoldas


def main() -> None:
    phone: Megoldas = Megoldas('hivas.txt')

    print('3. feladat')
    print(phone.stat_hours_print)

    print('4. Feladat')
    print(f'A leghosszabb ideig vonalban lévő hívó {phone.longest_call_line} sorban szerepel, a hívás hossza: {phone.longest_call_length} másodperc.')

    print("5. Feladat")
    input_numbers: str = input("Adjon meg egy idopontot! (ora perc masodperc) ")
    print(f'{"Nem volt beszélő" if phone.waiting_people_num(input_numbers) <= 0 else f"A várakozók száma: {phone.waiting_people_num(input_numbers)} a beszélo a {phone.accepted_caller_num(input_numbers)}. hívó."}')

    print("6. Feladat")
    print(f'Az utolso telefonalo adatai a(z) {phone.last_accepted_call_line}. sorban vannak, {phone.last_caller_waiting_time} masodpercig vart.')

    print("7. Feladat")
    print(phone.accepted_callers_text)


if __name__ == "__main__":
    main()
