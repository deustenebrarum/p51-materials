DAYS_PER_YEAR = 365
HOURS_PER_DAY = 24
MINUTES_PER_HOUR = 60
SECONDS_PER_MINUTE = 60


class LifeDates:
    def __init__(self, days, hours, minutes, seconds):
        self.days = days
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds


def calculate_life_time_formats(age):
    days = age * DAYS_PER_YEAR
    hours = days * HOURS_PER_DAY
    minutes = hours * MINUTES_PER_HOUR
    seconds = minutes * SECONDS_PER_MINUTE

    return LifeDates(days, hours, minutes, seconds)
