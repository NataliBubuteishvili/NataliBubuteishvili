def Task1():
   num = 1
   while num <= 10:
      print(num)
      num += 1

# Task1()

def Task2():
   for i in range(5):
     for x in range(1, i + 2):
       print(x,end="")
     print()

# Task2()

def Task3():
    num = int(input("enter a number:"))
    sum = 0
    for i in range(1, num + 1):
        sum +=i
    print("sum is", sum)

Task3()


def Task4():
