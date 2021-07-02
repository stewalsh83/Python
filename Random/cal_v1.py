def calculator_v1():
   num1 = int(input("Enter Number: "))
   num2 = int(input("Second Number: "))
   print("\n+ - x /")

   add = "+"
   sub = "-"
   mul = "x"
   div = "/"

   s = input("Select: ")

   if s == add:
      c = int(num1) + int(num2)
      print(c)

   elif s == sub:
      c = int(num1) - int(num2)
      print(c)

   elif s == mul:
      c = int(num1) * int(num2)
      print(c)

   else:
     c = int(num1) / int(num2)
     print(c)

calculator_v1()