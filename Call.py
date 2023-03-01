class Call:
    _first_hour: int
    _first_min: int
    _first_sec: int
    _last_hour: int
    _last_min: int
    _last_sec: int

    @property
    def first_hour(self):
        return self._first_hour

    @property
    def first_min(self):
        return self._first_min

    @property
    def first_sec(self):
        return self._first_sec

    @property
    def last_hour(self):
        return self._last_hour

    @property
    def last_min(self):
        return self._last_min

    @property
    def last_sec(self):
        return self._last_sec

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
    def call_length(self):
        length: int = 0
        length = self._mpbe(self.last_hour, self.last_min, self.last_sec) - self._mpbe(self.first_hour, self.first_min, self.first_sec)
        return length

    def __init__(self, line: str):
        first_hours, first_mins, first_secs, last_hours, last_mins, last_secs = line.split(' ')
        self._first_hour = int(first_hours)
        self._first_min = int(first_mins)
        self._first_sec = int(first_secs)
        self._last_hour = int(last_hours)
        self._last_min = int(last_mins)
        self._last_sec = int(last_secs)

    def _mpbe(self, hour: int, minute: int, second: int):
        return hour * 3600 + minute * 60 + second
