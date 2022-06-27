class Time(object):

    def set_time(time_object, hour, minute, second):
        time_object.hour = hour
        time_object.minute = minute
        time_object.second = second

    def show_time(time_object):
        print("The time is {:02d}:{:02d}:{:02d}".format(time_object.hour, time_object.minute, time_object.second))
