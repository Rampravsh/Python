fruits = ['apple','mango','cherry','banana'] #create a list


""" print(fruits)  #print a list
print(type(fruits)) #check type of list 
print(len(fruits)) #check length of list  """


""" #checking if an item is present in the list 

if 'banana' in fruits:
    print('Banana is part of the list')

# checking if an item is not present in the list 
if 'kiwi' not in fruits:
    print('Kiwi is not part of the list ') """


""" #Accessing  item of list 

print(fruits[1])  #'mango'

print(fruits[-3])
print(fruits[1:3]) """

# adding element to a list 

""" fruits.append('kiwi')
print(fruits)

fruits.insert(2,'gava')
print(fruits)

more_fruits=['kiwi','papaya']
fruits.extend(more_fruits)
print(fruits) """

list =[1,2,3,4,5]

# Removing  elements from a list
""" 
list.remove(4)
print(list)

list.pop()
print(list)

list.pop(2)
print(list)
 """

# changing/updating items in a list

""" list[1]=40
print(list)

list[1:4]=[20,30,40]
print(list)
 """

""" # sorting a list 
print(fruits)

fruits.sort()
print(fruits)

#sortin in reverse 

fruits.sort(reverse=True)
print(fruits) """

# reverse the list

# fruits.reverse()
# print(fruits)

#list conprehension

new_fruits= [fruit for fruit in fruits if 'a' in fruit]
print(new_fruits)