from classes.person import Person

person = Person()  # temp line


class Time:
    def __init__(self):
        self.current_time = None
        self.status = 'day' or 'night'
        self.day = None
        self.month = None
        self.year = None
        self.season = None

    def time_pass(self):
        pass




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







# from datetime import datetime, timedelta
#
# def increment_day(input_date_str):
#     # Convert the input string to a datetime object
#     input_date = datetime.strptime(input_date_str, "%Y-%m-%d")
#
#     # Increment the date by one day
#     next_day = input_date + timedelta(days=1)
#
#     # Format the result as a string in the same format
#     next_day_str = next_day.strftime("%Y-%m-%d")
#
#     return next_day_str
#
# # Example usage:
# input_date_str = "2023-2-28"
# next_day_date_str = increment_day(input_date_str)
#
# print(f"The next day after {input_date_str} is {next_day_date_str}")
