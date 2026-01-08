n=int(input('enter a number: '))
# sum =0
# for i in range(1,n+1):
#     sum+=i
# print(sum)

def sum(n):
    sum=0
    for i in range (1,n+1):
        sum+=i
    return sum

print(sum(n))

print(sum(n+34))