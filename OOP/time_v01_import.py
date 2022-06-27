from time_v01 import Time

a = Time()
Time.set_time(a, 13, 43, 6)
print(a.hour)
print(a.minute)
print(a.second)

b = Time()
Time.set_time(b, 21, 8, 36)
print(b.hour)
print(b.minute)
print(b.second)

c = Time()
Time.set_time(c, 4, 44, 51)
print(c.hour)
print(c.minute)
print(c.second)

print("---------------------\n")

a = Time()
Time.set_time(a, 13, 43, 6)
Time.show_time(a)

b = Time()
Time.set_time(b, 21, 8, 36)
Time.show_time(b)

c = Time()
Time.set_time(c, 4, 44, 51)
Time.show_time(c)

print("---------------------\n")

# easier to write this way
a = Time()
a.set_time(10, 54, 20)
a.show_time()

b.show_time()

c.show_time()
