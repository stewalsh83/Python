class Time(object):
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def is_later_than(self, other):
        if self.hour > other.hour:
            return True
        if self.hour < other.hour:
            return False

        if self.minute > other.minute:
            return True
        if self.minute < other.minute:
            return False

        if self.second > other.second:
            return True

        return False

    def show_time(self):
        print("The time is {:02d}:{:02d}:{:02d}".format(self.hour, self.minute, self.second))
