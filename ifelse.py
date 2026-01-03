# Take integer input and tell if it is positive or negative
""" input=input('Enter an integer: -')
num=int(input)
if num>0:
    print('The number is positive')
elif num<0:
    print('The number is negative')
else:
    print('The number is zero') """

# Take positive integer input and tell if it is even or odd

""" input = int(input('Enter an number '))
 
if input%2==0:
    print('the number is even')
else:
    print('the number is odd') """

# if cost price and selling price of an item is input through the keyboard, 
# write a prgram to determine whether the seller has made profit or incurred loss
# or no profit loss. Also determine how much profit he made or loss he incurred.

""" cost =int(input('Enter the cost price of the product '))
selling =int(input('Enter the selling price of the product '))

if selling>cost:
    print('you made profit on this product ',selling-cost)
elif cost>selling:
    print('you made loss on this product ',cost-selling)
else:
    print('no loss no profit on this product') """


# Take input percentage of a student and print the Grade according to marks:

""" marks=int(input('Enter the marks percentage '))
if marks>80:
    print('Very Good')
elif marks>60:
    print('Good')
elif marks>40:
    print('Average')
else:
    print('Fail') """

# Multiple condition using "and" and "or"

""" eng_marks=int(input('Enter marks in english: '))
math_marks=int(input('Enter marks in math: '))

if eng_marks>80 and math_marks>80:
    print('A')
elif eng_marks>80 or math_marks>80:
    print('B')
else :
    print('C') """

#Take positive integer input and tell if it is a four digit number or not
number=int(input('Enter number '))
if number>=1000 and number <= 9999:
    print('the given number is four digit number')
else:
    print('false')