from phone_numbers import phone_numbers


class Megoldas:
    phone_calls: list[phone_numbers]

    @property
    def call_for_all_hour(self):
        all_num: int = 0
        breaker: int = 0
        for number in range(8, 12):
            for e in self.phone_calls:
                if e.Last_hour == 8 and breaker == 0:
                    all_num += 1
                else:
                    if e.First_hour == number:
                        all_num += 1
                        breaker += 1
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

    # @property
    # def last_caller_wait_time(self):
    #     last_caller_id = self.call_for_all_hour
    #     last_call_object = self.phone_calls[last_caller_id - 1]
    #     last_call_object_mp_value: int = self.mpbe(last_call_object.Last_hour, last_call_object.Last_min, last_call_object.Last_sec)
    #     smaller_than_last_value: int = last_call_object_mp_value
    #     for e in self.phone_calls:
    #         if e.mpbe(e.Last_hour, e.Last_min, e.Last_sec) < last_call_object_mp_value:
    #             smaller_than_last_value = last_call_object_mp_value - e.mpbe(e.Last_hour, e.Last_min, e.Last_sec)
    #     return smaller_than_last_value

    # @property
    # def accepted_caller_num_without_input_check(self) -> int:
    #     previous_values: int = 0
    #     all_check: int = 0
    #     id_all: int = 0
    #     for e in self.phone_calls:
    #         if e.mpbe(e.Last_hour, e.Last_min, e.Last_sec) > previous_values and e.Last_hour >= 8 and e.First_hour <= 11:
    #             all_check += 1
    #             previous_values = e.mpbe(e.Last_hour, e.Last_min, e.Last_sec)
    #         id_all += 1
    #     return id_all

    # @property
    # def accepted_caller_num_without_input_check_num(self) -> int:
    #     previous_values: int = 0
    #     all_check: int = 0
    #     id_all: int = 0
    #     for e in self.phone_calls:
    #         if e.mpbe(e.Last_hour, e.Last_min, e.Last_sec) > previous_values and e.Last_hour >= 8 and e.First_hour <= 11:
    #             all_check += 1
    #             previous_values = e.mpbe(e.Last_hour, e.Last_min, e.Last_sec)
    #         id_all += 1
    #     number: int = self.mpbe(self.phone_calls[id_all - 1].First_hour, self.phone_calls[id_all - 1].First_min, self.phone_calls[id_all - 1].First_sec)
    #     return number

    # @property
    # def accepted_caller_before_final_check(self) -> int:
    #     value: int = self.accepted_caller_num_without_input_check
    #     previous_values: int = 0
    #     all_check: int = 0
    #     id_all: int = 0
    #     mp_value: int = 0
    #     for e in self.phone_calls:
    #         if e.mpbe(e.Last_hour, e.Last_min, e.Last_sec) > previous_values and e.Last_hour >= 8 and e.First_hour <= 11:
    #             all_check += 1
    #             previous_values = e.mpbe(e.Last_hour, e.Last_min, e.Last_sec)
    #         if all_check == value - 1:
    #             break
    #         id_all += 1
    #     mp_item: phone_numbers = self.phone_calls[id_all - 2]
    #     mp_value: int = self.mpbe(mp_item.Last_hour, mp_item.Last_min, mp_item.Last_hour)
    #     return mp_value

    # @property
    # def last_caller_wait_length(self):
    #     side_value: int = self.accepted_caller_num_without_input_check_num
    #     main_value: int = self.accepted_caller_before_final_check
    #     return main_value - side_value¨

    @property
    def F_6_1(self):  # utolsó hívó száma
        all_check: int = 0
        previous_values: int = 0
        for e in self.phone_calls:
            if e.mpbe(e.Last_hour, e.Last_min, e.Last_sec) > previous_values and e.Last_hour >= 8 and e.First_hour <= 11:
                all_check += 1
                previous_values = e.mpbe(e.Last_hour, e.Last_min, e.Last_sec)
        return all_check

    @property
    def F_6_1_5(self):  # utolsó előtti hívó száma
        all_check: int = 0
        previous_values: int = 0
        for e in self.phone_calls:
            if e.mpbe(e.Last_hour, e.Last_min, e.Last_sec) > previous_values and e.Last_hour >= 8 and e.First_hour <= 11:
                all_check += 1
                previous_values = e.mpbe(e.Last_hour, e.Last_min, e.Last_sec)
        return all_check

    @property
    def F_6_2(self):  # utolsó hívó lerakás mpbe
        last_caller: int = self.F_6_1
        all_check: int = 0
        previous_values: int = 0
        value: int = 0
        for e in self.phone_calls:
            value += 1
            if e.mpbe(e.Last_hour, e.Last_min, e.Last_sec) > previous_values and e.Last_hour >= 8 and e.First_hour <= 11:
                all_check += 1
                previous_values = e.mpbe(e.Last_hour, e.Last_min, e.Last_sec)
            if all_check == last_caller:
                break
        value = self.mpbe(self.phone_calls[all_check].Last_hour, self.phone_calls[all_check].Last_min, self.phone_calls[all_check].Last_sec)
        return value

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
