from time_v09 import Time

t = Time(23, 59, 59)
i = Time(0, 0, 1)
t.increment(i)
print(t)
