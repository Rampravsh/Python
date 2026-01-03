a=1
b=2
c=3
# how to get 123

a_str=str(a)
b_str=str(b)
c_str=str(c)

final_string=a_str+b_str+c_str
final_str=int(final_string)
# print('Final int:',final_string,type(final_string))

# Try this 
# Write a program to convert temperature from Celsius to Fahrenheit

Celsius=int(input('enter Celsius: -'))
Fehrenheit=(Celsius*(9/5))+32
print(Fehrenheit)