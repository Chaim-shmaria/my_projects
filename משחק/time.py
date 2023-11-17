from classes.person import Person
from datetime import datetime, timedelta

person = Person()  # temp line


class Time:
    def __init__(self):
        initial_date = "1987-02-13"
        self.date = datetime.strptime(initial_date, "%Y-%m-%d")
        self.current_time = None
        self.status = 'day' or 'night'
        self.season = None

    def time_pass(self):
        self.date = self.date + timedelta(days=1)

    def __str__(self):
        return self.date.strftime("%Y-%m-%d")

# time = Time()
#
# if time.current_time == '00:00':
#     person.go_to_sleep()
# if time.current_time == '07:00':
#     person.wake_up()
# if time.current_time == '08:00':
#     person.go_to_work()
# if time.current_time == '16:00':
#     person.return_home()
