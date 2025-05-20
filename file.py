name = input("enter your name: ")
print("welcome", name)
print("hello world")

val = input("Enter some value:")
print(type(val) ,val)

# A program to input two numbers and print their sum.
a = int(input("enter your number= "))
b = int(input("enter your number= "))
print("sum =" , a * b)

# A program to input side of a square and print its area
side = float(input("enter side square=: "))
print ("area = ", side **2)

# A program to input two int num a and b, print true if a is greater or equal to b . if not false
a = int(input("enter your number= "))
b = int(input("enter your number= "))
print(a >= b)

#A program to input yur name and find its length
name = input("enter your name: ")
print("length: ", len(name))

#A program to check if a number by the user is even or odd.
num = int(input("enter a number: "))
rem = num % 2

if(rem == 0):
    print("EVEN")
else:
    print("ODD")