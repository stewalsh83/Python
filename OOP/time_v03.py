class Time(object):

    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def show_time(self):
        print("The time is {:02d}:{:02d}:{:02d}".format(self.hour, self.minute, self.second))
