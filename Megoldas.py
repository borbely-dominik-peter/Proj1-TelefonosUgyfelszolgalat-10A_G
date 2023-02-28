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
        last_value: int = 0
        second_last_value: int = 0
        for e in self._phone_calls:
            if e == self.accepted_calls[-1]:
                last_value = e.start_in_sec
                break
            elif e == self.accepted_calls[-2]:
                second_last_value = e.end_in_sec
        return second_last_value - last_value

    @property
    def accepted_callers_text(self): #7. Task
        index_checker: int = 0
        for e in self._phone_calls:
            if e in self.accepted_calls:
                with open('sikeres.txt','a',encoding='UTF-8') as file:
                    file.write(f'{index_checker} {e.first_hour} {e.first_min} {e.first_sec} {e.last_hour} {e.last_min} {e.last_sec}\n')
            index_checker += 1
        return "sikeres.txt elkészült"
                break
            else:
                counter += 1
        return counter

    @property
    def last_caller_waiting_time(self):  # 6. task
        last_value: int = self.accepted_calls[-1].start_in_sec
        second_last_value: int = self.accepted_calls[-2].end_in_sec
        return second_last_value - last_value

    def __init__(self, txt_name: str):
        self._phone_calls = []
        self._source_read(txt_name)

    def _source_read(self, txt_name: str) -> None:
        with open(txt_name, 'r', encoding='utf-8') as file:
            for line in file.read().splitlines():
                self._phone_calls.append(Call(line))

    def waiting_people_num(self, line: str) -> int:  # 5. task
        waiting_people_candidate: list[Call] = []
        input_hour, input_min, input_sec = line.split(" ")
        a_line: str = ''
        a_line: str = f'{input_hour} {input_min} {input_sec} {input_hour} {input_min} {input_sec}'
        self._phone_calls.append(Call(a_line))
        input_hour = int(input_hour)
        input_min = int(input_min)
        input_sec = int(input_sec)
        a_line_value: int = self._phone_calls[-1].start_in_sec
        self._phone_calls.pop()
        for e in self._phone_calls:
            if e.end_in_sec >= a_line_value and e.start_in_sec <= a_line_value:
                waiting_people_candidate.append(e)
        return len(waiting_people_candidate) - 1

    def accepted_caller_num(self, line: str) -> int:  # 5. task
        input_hour, input_min, input_sec = line.split(" ")
        a_line: str = ''
        a_line: str = f'{input_hour} {input_min} {input_sec} {input_hour} {input_min} {input_sec}'
        self._phone_calls.append(Call(a_line))
        a_line_value: int = self._phone_calls[-1].start_in_sec
        counter: int = 0
        self._phone_calls.pop()
        for e in self.accepted_calls:
            if e.end_in_sec >= a_line_value:
                break
            else:
                counter += 1
        return counter
