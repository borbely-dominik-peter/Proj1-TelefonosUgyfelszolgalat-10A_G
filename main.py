from Solution import Solution


def main() -> None:
    sol: Solution = Solution('hivas.txt')

    print('3. feladat')
    print(sol.stat_hours_print)

    print('4. Feladat')
    print(f'A leghosszabb ideig vonalban lévő hívó {sol.longest_call_line} sorban szerepel, a hívás hossza: {sol.longest_call_length} másodperc.')

    print("5. Feladat")
    input_numbers: str = input("Adjon meg egy idopontot! (ora perc masodperc) ")
    print(f'{"Nem volt beszélő" if sol.waiting_people_num(input_numbers) <= 0 else f"A várakozók száma: {sol.waiting_people_num(input_numbers)} a beszélő a(z) {sol.accepted_caller_num(input_numbers)}. hívó."}')

    print("6. Feladat")
    print(f'Az utolsó telefonáló adatai a(z) {sol.last_accepted_call_line}. sorban vannak, {sol.last_caller_waiting_time} másodpercig várt.')

    print("7. Feladat")
    print(sol.accepted_callers_text)


if __name__ == "__main__":
    main()
