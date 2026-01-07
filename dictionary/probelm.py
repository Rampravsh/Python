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

# given a string and a number N, we need to mirror the characters from the N-th position up 
# to the length of the string in alphabetical order . in mirror operation , we change 'a' to 
# "z" ,"b"to "y",and so on.

res=''
string ="paradox"
n=3
for i in range(len(string)):
    if i>=n-1:
        acii=ord(string[i])
        res+=chr(122-(acii-97))
    else:
        res+=string[i]

print(res)
