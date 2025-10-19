# while loops
i = 20
while i>= 1:
    print(i)
    i -= 1

print('loop ended')

# multiplication of a number
n= int(input('entera number'))

i = 1
while i <= 10:
    print(n * i)
    i +=1

# Print the numbers in the list using loop
num =[1, 4, 9, 16, 25 , 36, 49, 64, 81, 100]

i=0
while i < len(num):
    print(num[i])
    i += 1

# Find a number using while loop

num =[1, 4, 9, 16, 25 , 36, 49, 64, 81, 100]
x = 36
i = 0
while i < len(num):
   if(num[i] == x):
       print('item found' , i)
       i += 1