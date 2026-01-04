""" n=int(input('enter the row no : '))

for _ in range(n):
    print('*'*5) """


n=int(input('enter the row no : '))
for _ in range(n):
    for i in range(1,n+1):
        print(i,end='')
    print()