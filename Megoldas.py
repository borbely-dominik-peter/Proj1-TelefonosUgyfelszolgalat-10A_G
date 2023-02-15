from phone_numbers import phone_numbers


class Megoldas:
    phone_calls: list[phone_numbers]
        
    @property
    def call_for_all_hour(self):
        all_num: int = 0
        for number in range(8, 12):
            for e in self.phone_calls:
                if e.First_hour == number:
                    all_num += 1
            print(f'{number} óra {all_num} hívás')
        return all_num

    @property
    def longest_call_length(self):
        call_length: int = 0
        for e in self.phone_calls:
            if e.hivas_hossz > call_length:
                call_length = e.hivas_hossz
        return call_length

    @property
    def longest_call_line(self):
        line_counter: int = 0
        for e in self.phone_calls:
            line_counter += 1
            if e.hivas_hossz == self.longest_call_length:
                break
        return line_counter

    @property
    def last_caller_num(self):
        previous_values: int = 0
        all_check: int = 0
        call_counter: int = 0
        for e in self.phone_calls:
            if e.mpbe(e.Last_hour, e.Last_min, e.Last_sec) > previous_values and e.Last_hour >= 8 and e.First_hour <= 11:
                all_check += 1
                previous_values = e.mpbe(e.Last_hour, e.Last_min, e.Last_sec)
        return all_check

    def __init__(self, txt_name: str):
        self.phone_calls = []
        self.source_read(txt_name)

    def source_read(self, txt_name: str) -> None:
        with open(txt_name, 'r', encoding='utf-8') as file:
            for line in file.read().splitlines():
                self.phone_calls.append(phone_numbers(line))

    def mpbe(self, hour: int, minute: int, second: int):
        return hour * 3600 + minute * 60 + second


    def accepted_caller_num(self, line: str) -> int:
        previous_values: int = 0
        all_check: int = 0
        input_hour, input_min, input_sec = line.split(" ")
        input_hour = int(input_hour)
        input_min = int(input_min)
        input_sec = int(input_sec)
        for e in self.phone_calls:
            if e.mpbe(e.Last_hour, e.Last_min, e.Last_sec) >= self.mpbe(input_hour, input_min, input_sec):
                break

            if e.mpbe(e.Last_hour, e.Last_min, e.Last_sec) > previous_values and e.Last_hour >= 8 and e.First_hour <= 11:
                all_check += 1
                previous_values = e.mpbe(e.Last_hour, e.Last_min, e.Last_sec)
        return all_check

    def waiting_people_num(self, line: str) -> int:
        all_waiting_peoples: int = 0
        first_larger: int = 0
        phone_calls_subset: list[phone_numbers] = []
        input_hour, input_min, input_sec = line.split(" ")
        input_hour = int(input_hour)
        input_min = int(input_min)
        input_sec = int(input_sec)
        for e in self.phone_calls:
            if e.mpbe(e.Last_hour, e.Last_min, e.Last_sec) > self.mpbe(input_hour, input_min, input_sec):
                first_larger = e.mpbe(e.Last_hour, e.Last_min, e.Last_sec)
                break
        for e in self.phone_calls:
            if e.mpbe(e.First_hour, e.First_min, e.First_sec) < self.mpbe(input_hour, input_min, input_sec) and e.First_hour >= 8 and e.First_hour <= 11 and e.mpbe(e.Last_hour, e.Last_min, e.Last_sec) != first_larger:
                all_waiting_peoples += 1
                phone_calls_subset.append(e)
        for e in phone_calls_subset:
            if e.mpbe(e.Last_hour, e.Last_min, e.Last_sec) < first_larger and e.Last_hour >= 8 and e.First_hour <= 11:
                all_waiting_peoples -= 1
        return all_waiting_peoples

