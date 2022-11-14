class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        minutes = self.minutes
        seconds = self.seconds
        hours = self.hours

        if minutes < 10:
            minutes = "0" + str(minutes)
        else:
            pass

        if seconds < 10:
            seconds = "0" + str(seconds)
        else:
            pass
        if hours < 10:
            hours = "0" + str(hours)
        else:
            pass

        return f"{hours}:{minutes}:{seconds}"

    def next_second(self):
        self.seconds += 1
        if self.seconds > Time.max_seconds:
            self.seconds = 0
            self.minutes += 1
            if self.minutes > Time.max_minutes:
                self.minutes = 0
                self. hours += 1
                if self.hours > Time.max_hours:
                    self.hours = 0
                else:
                    pass
            else:
                pass
        else:
            pass

        return self.get_time()


time = Time(9, 30, 59)
print(time.next_second())
time = Time(10, 59, 59)
print(time.next_second())
time = Time(23, 59, 59)
print(time.next_second())

