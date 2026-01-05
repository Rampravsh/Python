# # creating a sets
# value={3,3,46,467,53,43}
# #print set
# print(value)

# #check length of set
# print(len(value))

# # check data type of set 
# print(type(value))

# #accessing item of set 

# for x in value:
#     print(x)

# #check if an item exists in a set 

# if 3 in value:
#     print('3 is in the set')

#add elements in set 
names ={'ria','tia','sia'}

# names.add('sia') #not adding in set because duplicates not allowed
# names.add('pia')
# print(names)

#add another sequence in a set 
# names_list=['ria','kia']

# names.update(names_list)
# print(names)

# removing element from a set 
# names.remove('tia')
# names.remove('pia')  # gives error if not present in the set
# print(names)

names.discard('pia')  #it gives error if that item even not present in set
print(names)