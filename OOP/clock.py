from time_v09 import Time
from time import sleep
from datetime import datetime

# Get current time
now = datetime.now()

# Instantiate a Time object with the current time
t = Time(now.hour, now.minute, now.second)

# Instantiate a time object with the increment
i = Time(0, 0, 1)

# Loop forever
while True:
    # Display the current time
    # print(t)
    print(f'\r{t}', end='', flush=True)

    # sleep for 1 second
    sleep(1)

    # increment the time by 1 second
    t.increment(i)
