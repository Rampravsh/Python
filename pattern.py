""" n=int(input('enter the row no : '))

for _ in range(n):
    print('*'*5) """


""" n=int(input('enter the row no : '))
for _ in range(n):
    for i in range(1,n+1):
        print(i,end='')
    print() """

n=int(input('enter number: '))
for i in range(1,n+1):
    for j in range(n-i,0,-1):
        print(' ',end='')
    for j in range(1,i*2):
        print(j,end='')
    print()