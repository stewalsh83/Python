from time_v05 import Time

t1 = Time(12, 9, 6)
t2 = Time(13, 11, 40)
t3 = Time(12, 59, 59)
t4 = Time(12, 9, 7)

print(t2.is_later_than(t1))
print(t1.is_later_than(t2))
print(t3.is_later_than(t2))
print(t4.is_later_than(t1))
