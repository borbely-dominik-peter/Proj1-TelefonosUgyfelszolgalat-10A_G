from Call import Call


class Megoldas:
    _phone_calls: list[Call]

    @property
    def stat_hours(self):  # 3. task
        stat_h: dict[int, int] = {}
        for e in self._phone_calls:
            if e.first_hour in stat_h:
                stat_h[e.first_hour] += 1
            else:
                stat_h[e.first_hour] = 1
        return stat_h

    @property
    def stat_hours_print(self):  # 3. task
        values: str = ''
        for key, value in self.stat_hours.items():
            values += f'{key} óra {value} hívás\n'
        return values

    # @property
    # def call_for_all_hour(self):
    #     all_num: int = 0
    #     breaker: int = 0
    #     for number in range(8, 12):
    #         for e in self._phone_calls:
    #             if e.last_hour == 8 and breaker == 0:
    #                 all_num += 1
    #             else:
    #                 if e.first_hour == number:
    #                     all_num += 1
    #                     breaker += 1
    #     return all_num

    @property
    def longest_call_length(self):  # 4. task
        call_length: int = 0
        for e in self._phone_calls:
            if e.hivas_hossz > call_length:
                call_length = e.hivas_hossz
        return call_length

    @property
    def longest_call_line(self):  # 4. task
        line_counter: int = 0
        for e in self._phone_calls:
            line_counter += 1
            if e.hivas_hossz == self.longest_call_length:
                break
        return line_counter

    @property
    def accepted_calls(self):  # 5/6.task
        accepted_list: list[Call] = []
        previous_values: int = 0
        for e in self._phone_calls:
            if e.end_in_sec > previous_values and e.last_hour >= 8 and e.first_hour <= 11:
                accepted_list.append(e)
                previous_values = e.end_in_sec
        return accepted_list

    @property
    def last_accepted_call_line(self):  # 6. task
        counter: int = 0
        for e in self._phone_calls:
            if e == self.accepted_calls[-1]:
                counter += 1
                break
            else:
                counter += 1
        return counter

    @property
    def last_caller_waiting_time(self):  # 6. task
        last_value: int = self.accepted_calls[-1].start_in_sec
        second_last_value: int = self.accepted_calls[-2].end_in_sec
        return second_last_value - last_value

    # @property
    # def last_caller_wait(self):
    #     last_caller_id = self.call_for_all_hour
    #     last_call_object = self._phone_calls[last_caller_id - 1]
    #     last_call_object_mp_value: int = self.mpbe(last_call_object.last_hour, last_call_object.last_min, last_call_object.last_sec)
    #     smaller_than_last_value: int = last_call_object_mp_value
    #     for e in self._phone_calls:
    #         if e.end_in_sec < last_call_object_mp_value:
    #             smaller_than_last_value = last_call_object_mp_value - e.end_in_sec
    #     return smaller_than_last_value

    # @property
    # def final_caller_num(self) -> int:
    #     previous_values: int = 0
    #     all_check: int = 0
    #     id_all: int = self.call_for_all_hour - 1
    #     for e in self._phone_calls:
    #         if e.end_in_sec > previous_values and e.last_hour >= 8 and e.first_hour <= 11:
    #             all_check += 1
    #             previous_values = e.end_in_sec
    #     number: int = self.mpbe(self._phone_calls[id_all].first_hour, self._phone_calls[id_all].first_min, self._phone_calls[id_all].first_sec)
    #     return number

    # @property
    # def final_caller(self) -> int:
    #     previous_values: int = 0
    #     all_check: int = 0
    #     id_all: int = self.call_for_all_hour - 1
    #     for e in self._phone_calls:
    #         if e.end_in_sec > previous_values and e.last_hour >= 8 and e.first_hour <= 11:
    #             all_check += 1
    #             previous_values = e.end_in_sec
    #     return all_check

    # @property
    # def accepted_caller_before_final(self) -> int:
    #     value: int = self.final_caller
    #     previous_values: int = 0
    #     all_check: int = 0
    #     mp_value: int = 0
    #     index_count: int = 0
    #     for e in self._phone_calls:
    #         index_count += 1
    #         if e.end_in_sec > previous_values and e.last_hour >= 8 and e.first_hour <= 11:
    #             all_check += 1
    #             previous_values = e.end_in_sec
    #         if all_check == value - 1:
    #             break
    #     mp_item: phone_call = self._phone_calls[index_count - 1]
    #     mp_value: int = self.mpbe(mp_item.last_hour, mp_item.last_min, mp_item.last_sec)
    #     return mp_value

    # @property
    # def last_caller_wait_length(self):
    #     side_value: int = self.final_caller_num
    #     main_value: int = self.accepted_caller_before_final
    #     return main_value - side_value

    def __init__(self, txt_name: str):
        self._phone_calls = []
        self._source_read(txt_name)

    def _source_read(self, txt_name: str) -> None:
        with open(txt_name, 'r', encoding='utf-8') as file:
            for line in file.read().splitlines():
                self._phone_calls.append(Call(line))

    def waiting_people_num(self, line: str):  # 5. task
        waiting_people_candidate: list[Call] = []
        input_hour, input_min, input_sec = line.split(" ")
        a_line: str = ''
        a_line: str = f'{input_hour} {input_min} {input_sec} {input_hour} {input_min} {input_sec}'
        self._phone_calls.append(Call(a_line))
        input_hour = int(input_hour)
        input_min = int(input_min)
        input_sec = int(input_sec)
        a_line_value: int = self._phone_calls[-1].start_in_sec
        for e in self._phone_calls:
            if e.end_in_sec >= a_line_value and e.start_in_sec <= a_line_value:
                waiting_people_candidate.append(e)
        return len(waiting_people_candidate) - 1

    @property
    def accepted_caller_num(self) -> int:  # 5. task
        a_line_value: int = self._phone_calls[-1].start_in_sec
        counter: int = 0
        self._phone_calls.pop()
        for e in self.accepted_calls:
            if e.end_in_sec >= a_line_value:
                break
            else:
                counter += 1
        return counter

    #     previous_values: int = 0
    #     all_check: int = 0
    #     for e in self._phone_calls:
    #         if e.end_in_sec >= self.mpbe(input_hour, input_min, input_sec):
    #             break
    #         if e.end_in_sec > previous_values and e.last_hour >= 8 and e.first_hour <= 11:
    #             all_check += 1
    #             previous_values = e.end_in_sec
    #     return all_check

    # def waiting_people_num(self, line: str) -> int:  # 5. task
    #     all_waiting_peoples: int = 0
    #     first_larger: int = 0
    #     phone_calls_subset: list[Call] = []
    #     input_hour, input_min, input_sec = line.split(" ")
    #     input_hour = int(input_hour)
    #     input_min = int(input_min)
    #     input_sec = int(input_sec)
    #     for e in self._phone_calls:
    #         if e.end_in_sec > self.mpbe(input_hour, input_min, input_sec):
    #             first_larger = e.end_in_sec
    #             break
    #     for e in self._phone_calls:
    #         if e.start_in_sec < self.mpbe(input_hour, input_min, input_sec) and e.first_hour >= 8 and e.first_hour <= 11 and e.end_in_sec != first_larger:
    #             all_waiting_peoples += 1
    #             phone_calls_subset.append(e)
    #     for e in phone_calls_subset:
    #         if e.end_in_sec < first_larger and e.last_hour >= 8 and e.first_hour <= 11:
    #             all_waiting_peoples -= 1
    #     return all_waiting_peoples
