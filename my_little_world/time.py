from datetime import datetime, timedelta

INITIAL_DATE = "1987-02-13"
DAY_LENGTH = 4


class Time:
    def __init__(self, initial_date):
        self.clock_time = (5, 50)
        self.date = datetime.strptime(initial_date, "%Y-%m-%d")
        self.status = True  # 'day' or 'night'
        self.game_days = 0
        self.season = None

    def time_pass(self):
        minute = (self.clock_time[1] + 30) % 60
        hour = self.clock_time[0]
        if minute == 0:
            hour = (self.clock_time[0] + 1) % 24
        self.clock_time = (hour, minute)
        if hour == 0:
            self.day_pass()

    def day_pass(self):
        if self.game_days % DAY_LENGTH == 0:
            self.status = not self.status
        else:
            self.game_days += 1
        self.date = self.date + timedelta(days=1)

    def current_time(self):
        date_str = self.date.strftime("%Y-%m-%d")
        # year = date_str[:4]
        # month = date_str[5:7]
        # day = date_str[8:]
        return "date: {} clock: {:02d}:{:02d}".format(date_str, self.clock_time[0], self.clock_time[1])

# a = Time(INITIAL_DATE)
# print(a.current_time())