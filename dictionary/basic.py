#creating a dictionary

phones={
    'john':93874,
    'ria':279834,
    'joy':3982
}

#printing the dict

print("Initial dictionary:")
print(phones)

#checking type of dic
print("\nType of the data structure:")
print(type(phones))

#checking length of dict
print("\nLength of the dictionary:")
print(len(phones))

#access items of the dict
print("\nAccessing items:")
print("Value for 'john':", phones['john'])
print("Value for 'john' using get():", phones.get('john'))
print("All keys:", phones.keys())

#update value in dict
print("\nUpdating a value:")
phones['john']=398479823
print(phones)


#add elements in dict
print("\nAdding elements:")
phones['pia']=283478273
print(phones)

print("\nAdding elements from another dictionary:")
more_phones={
    'kia':9834792
}
phones.update(more_phones)
print(phones)

#remove elements from the dict
print("\nRemoving elements:")
print("Removing 'john':")
phones.pop('john')
print(phones)

print("Removing the last inserted item:")
phones.popitem()
print(phones)


# Advanced Dictionary Examples

print("\n--- Advanced Dictionary Examples ---")

# Nested Dictionaries
print("\nNested Dictionaries:")
users = {
    'user1': {
        'name': 'Alice',
        'email': 'alice@example.com'
    },
    'user2': {
        'name': 'Bob',
        'email': 'bob@example.com'
    }
}
print(users)
print("Accessing nested dictionary element:", users['user1']['name'])

# Dictionary Comprehension
print("\nDictionary Comprehension:")
squares = {x: x*x for x in range(6)}
print("Squares from 0 to 5:", squares)

# fromkeys() - creating a dictionary with specified keys and value
print("\nfromkeys():")
keys = {'a', 'b', 'c'}
value = 0
fromkeys_dict = dict.fromkeys(keys, value)
print("Dictionary from keys with default value:", fromkeys_dict)

# setdefault() - returns the value of a key, or inserts it if it does not exist
print("\nsetdefault():")
person = {'name': 'John', 'age': 30}
print("Original person dict:", person)
# Get the value of 'age'
print("Age:", person.setdefault('age', 35))
# 'city' key does not exist, so it will be added with the default value 'New York'
print("City:", person.setdefault('city', 'New York'))
print("Updated person dict:", person)

# Merging Dictionaries (Python 3.9+)
print("\nMerging Dictionaries (Python 3.9+):")
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = dict1 | dict2
print("Merged dictionary:", merged_dict)

# Merging with unpacking (Python 3.5+)
print("\nMerging with unpacking (Python 3.5+):")
dict3 = {'e': 5, 'f': 6}
merged_unpack_dict = {**merged_dict, **dict3}
print("Merged with unpacking:", merged_unpack_dict)

# Looping through keys and values
print("\nLooping through keys and values using items():")
for key, value in merged_unpack_dict.items():
    print(f"Key: {key}, Value: {value}")


#clearing the dict
print("\nClearing the dictionary:")
merged_unpack_dict.clear()
print(merged_unpack_dict)