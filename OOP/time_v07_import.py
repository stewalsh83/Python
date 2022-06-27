from time_v07 import Time

t1 = Time(13, 58, 23)
t2 = Time(0, 10, 0)
t3 = t1.plus(t2)
t3.show_time()

t4 = Time(16, 18, 36)
t5 = Time(12, 10, 19)
t6 = t4.plus(t5)
t6.show_time()
