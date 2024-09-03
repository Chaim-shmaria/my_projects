from classes.person import Person

person = Person()  # temp line


class Time:
    def __init__(self):
        self.season = None
        self.current_time = None
        self.day = None


time = Time()

if time.current_time == '00:00':
    person.go_to_sleep()
if time.current_time == '07:00':
    person.wake_up()
if time.current_time == '08:00':
    person.go_to_work()
if time.current_time == '16:00':
    person.return_home()
