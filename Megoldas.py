from phone_numbers import phone_numbers


class Megoldas:
    phone_calls: list[phone_numbers]

    def __init__(self, txt_name: str):
        self.phone_calls = []
        self.source_read(txt_name)

    def source_read(self, txt_name: str) -> None:
        with open(txt_name, 'r', encoding='utf-8') as file:
            for line in file.read().splitlines():
                self.phone_calls.append(phone_numbers(line))

    def mpbe(self, hour: int, minute: int, second: int):
        return hour * 3600 + minute * 60 + second
