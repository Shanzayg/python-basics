#WAP to input users first name and priny its length
name = input('Enter your name :')
length = len(name)
print('length of a string is :' , length)

#WAP to find the occurence of '$' in a string
country = 'malaysia'
country.find('$')
if(country == '$'):
    print('found')
else:
    print('not found')
    
#WAP to find a palindrome
first_word = ['a','b','r','a','c','a']
second_word = ['r','a','c','e','c','a','r']

word_one = first_word.copy()
word_one.reverse()

word_two = second_word.copy()
word_two.reverse()

if(first_word == word_one or second_word == word_two):
  print('palindrome')
else:
   print('not palindrome')

#wap to check if a number entered by the user is odd or even
number = int(input("enter a value :"))

if( number % 2 == 0):
   print('even')
else:
   print('odd')

#WAP to find the greatest of 3 numbers entered by the user.
a = int(input('enter a number:'))
b = int(input('enter a number:'))
c = int(input('enter a number:'))
if(a>b and a>c):
   print('a is greater than b and c')
elif(b>c):
   print('b is greater than a and c')
else:
   print('c is greater than a and b')

#WAP to check if a number is a multiple of 7 or not
a = int(input('enter:'))
if (a % 7 == 0):
   print('multiple of 7')
else:
   print('not a multiple of 7')

   