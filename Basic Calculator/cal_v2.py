def calculator_v2():
   print("Basic Calculator\n")
   num1 = int(input("First Number: "))
   s = input("Select: + - x /\n")
   num2 = int(input("Second Number: "))

   add = "+"
   sub = "-"
   mul = "x"
   div = "/"

   if s == add:
      c = int(num1) + int(num2)
      print("{} {} {} = {}".format(num1, add, num2, c))

   elif s == sub:
      c = int(num1) - int(num2)
      print("{} {} {} = {}".format(num1, sub, num2, c))

   elif s == mul:
      c = int(num1) * int(num2)
      print("{} {} {} = {}".format(num1, mul, num2, c))

   else:
     c = int(num1) / int(num2)
     print("{} {} {} = {}".format(num1, div, num2, c))

calculator_v2()