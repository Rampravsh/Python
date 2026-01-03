num1=int(input('Enter number 1: '))
num2=int(input('Enter number 2: '))
operator=input('Enter operator: ')

match operator:
    case '+':
        print('sum is',num1+num2)
    case '-':
        print('differece is',num1-num2)
    case '*':
        print('product is',num1*num2)
    case '/':
        print('division is ',num1/num2)
    case _ :
        print('Enter a valid orerator')