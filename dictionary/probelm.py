#Given a dictionary in python, write a python program to find the sum of all items in the dictionary

dict ={
    'a':100,
    'b':200,
    'c':300
}
res = 0
for x in dict.values():
    res+=x

# print(res)
# print('The sum of dict values is: ',sum(dict.values()))

