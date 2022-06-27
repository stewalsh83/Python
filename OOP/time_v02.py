class Time(object):

    def set_time(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def show_time(self):
        print("The time is {:02}:{:02}:{:02}"
              .format(self.hour, self.minute, self.second))

# a = Time()
# a.set_time(10, 59, 30)
# a.show_time()
