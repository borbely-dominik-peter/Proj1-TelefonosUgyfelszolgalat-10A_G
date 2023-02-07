class phone_numbers:
    First_hour: int
    First_min: int
    First_sec: int
    Last_hour: int
    Last_min: int
    Last_sec: int

    def __init__(self, line: str):
        First_hours, First_mins, First_secs, Last_hours, Last_mins, Last_secs = line.split(' ')
        self.First_hour = int(First_hours)
        self.First_min = int(First_mins)
        self.First_sec = int(First_secs)
        self.Last_hour = int(Last_hours)
        self.Last_min = int(Last_mins)
        self.Last_sec = int(Last_secs)
