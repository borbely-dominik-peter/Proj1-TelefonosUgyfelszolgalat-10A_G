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


if __name__ == "__main__":
    main()
