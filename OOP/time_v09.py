class Time(object):

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def time_to_seconds(self):
        return self.hour * 60 * 60 + self.minute * 60 + self.second

    def is_later_than(self, other):
        return self.time_to_seconds() > other.time_to_seconds()

    def plus(self, other):
        return seconds_to_time(self.time_to_seconds() + other.time_to_seconds())

    def increment(self, other):
        z = self.plus(other)
        self.hour, self.minute, self.second = z.hour, z.minute, z.second

    def __str__(self):
        return "The time is {:02d}:{:02d}:{:02d}".format(self.hour, self.minute, self.second)


def seconds_to_time(s):
    minute, second = divmod(s, 60)
    hour, minute = divmod(minute, 60)
    overflow, hour = divmod(hour, 24)
    return Time(hour, minute, second)
