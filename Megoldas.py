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
    
    def felvett_hívás_száma(self, sor: str) -> int:
        elozo_ertek: int = 0
        osszes: int = 0
        input_hour, input_min, input_sec = sor.split(" ")
        input_hour = int(input_hour)
        input_min = int(input_min)
        input_sec = int(input_sec)
        for e in self.phone_calls:
            if e.mpbe(e.Last_hour, e.Last_min, e.Last_sec) >= self.mpbe(input_hour, input_min, input_sec):
                break
            if e.mpbe(e.Last_hour, e.Last_min, e.Last_sec) > elozo_ertek and e.Last_hour >= 8 and e.First_hour <= 11:
                osszes += 1
                elozo_ertek = e.mpbe(e.Last_hour, e.Last_min, e.Last_sec)
        return osszes
