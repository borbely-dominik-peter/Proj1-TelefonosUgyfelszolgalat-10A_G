class Call:
    first_hour: int
    first_min: int
    first_sec: int
    last_hour: int
    last_min: int
    last_sec: int

    @property
    def start_in_sec(self):
        time: int = 0
        time: int = self._mpbe(self.first_hour, self.first_min, self.first_sec)
        return time

    @property
    def end_in_sec(self):
        time: int = 0
        time: int = self._mpbe(self.last_hour, self.last_min, self.last_sec)
        return time

    @property
    def hivas_hossz(self):
        hossz: int = 0
        hossz = self._mpbe(self.last_hour, self.last_min, self.last_sec) - self._mpbe(self.first_hour, self.first_min, self.first_sec)
        return hossz

    def __init__(self, line: str):
        first_hours, first_mins, first_secs, last_hours, last_mins, last_secs = line.split(' ')
        self.first_hour = int(first_hours)
        self.first_min = int(first_mins)
        self.first_sec = int(first_secs)
        self.last_hour = int(last_hours)
        self.last_min = int(last_mins)
        self.last_sec = int(last_secs)

    def _mpbe(self, hour: int, minute: int, second: int):
        return hour * 3600 + minute * 60 + second
