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
    
    def hivas_hossz(self, first_hour: int, first_minute: int, first_second: int, last_hour: int, last_minute: int, last_second: int):
        hossz: int = 0
        hossz = self.mpbe(last_hour, last_minute, last_second) - self.mpbe(first_hour, first_minute, first_second)
        return hossz
    
    def leghosszabb_hivas(self):
        for e in self.phone_calls:
            self.hivas_hossz(e.First_hour, e.First_min, e.First_sec, e.Last_hour, e.Last_min, e.Last_sec)


