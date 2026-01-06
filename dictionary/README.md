# Python Dictionaries

A dictionary in Python is an unordered collection of data values, used to store data values like a map, which, unlike other Data Types that hold only a single value as an element, holds a key:value pair. Key-value pairs provide a way to store data in a structured way and allow for fast lookups.

## 1. Creating a Dictionary

You can create a dictionary by placing a comma-separated list of key:value pairs in curly braces `{}`.

```python
# An empty dictionary
my_dict = {}
print(my_dict)

# A dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}
print(my_dict)

# A dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}
print(my_dict)

# Using the dict() constructor
my_dict = dict({1:'apple', 2:'ball'})
print(my_dict)

my_dict = dict([(1,'apple'), (2,'ball')])
print(my_dict)
```

## 2. Accessing Elements

You can access items of a dictionary by referring to its key name, inside square brackets `[]`.

```python
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

# Accessing a value by its key
print(my_dict['name'])  # Output: John

# Using the get() method
print(my_dict.get('age')) # Output: 25

# The difference between [] and get()
# Using [] for a non-existent key will raise a KeyError
# print(my_dict['country']) # This would raise a KeyError

# Using get() for a non-existent key will return None by default
print(my_dict.get('country')) # Output: None

# You can also provide a default value to return
print(my_dict.get('country', 'USA')) # Output: USA
```

## 3. Adding and Updating Items

You can add new items or change the value of existing items using an assignment operator.

```python
my_dict = {'name': 'John', 'age': 25}

# Update an existing item
my_dict['age'] = 26
print(my_dict) # Output: {'name': 'John', 'age': 26}

# Add a new item
my_dict['city'] = 'New York'
print(my_dict) # Output: {'name': 'John', 'age': 26, 'city': 'New York'}

# Using the update() method
my_dict.update({'country': 'USA', 'name': 'John Doe'})
print(my_dict) # Output: {'name': 'John Doe', 'age': 26, 'city': 'New York', 'country': 'USA'}
```

## 4. Removing Items

You can remove items from a dictionary using several methods.

```python
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

# Using pop() - removes the item with the specified key and returns its value
age = my_dict.pop('age')
print(f"Removed age: {age}") # Output: Removed age: 25
print(my_dict) # Output: {'name': 'John', 'city': 'New York'}

# Using popitem() - removes the last inserted item (in Python 3.7+)
item = my_dict.popitem()
print(f"Removed item: {item}") # Output: Removed item: ('city', 'New York')
print(my_dict) # Output: {'name': 'John'}

# Using the 'del' keyword
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
del my_dict['age']
print(my_dict) # Output: {'name': 'John', 'city': 'New York'}

# Using clear() - removes all items from the dictionary
my_dict.clear()
print(my_dict) # Output: {}
```

## 5. Looping Through a Dictionary

You can iterate through the keys, values, or key-value pairs of a dictionary.

```python
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

# Iterate through keys (this is the default)
print("Keys:")
for key in my_dict:
    print(key)

# Iterate through keys using keys() method
print("\nKeys using .keys():")
for key in my_dict.keys():
    print(key)

# Iterate through values
print("\nValues:")
for value in my_dict.values():
    print(value)

# Iterate through key-value pairs
print("\nItems (key-value pairs):")
for key, value in my_dict.items():
    print(f"{key}: {value}")
```

## 6. Dictionary Comprehension

A concise way to create dictionaries.

```python
# Create a dictionary of squares from 1 to 5
squares = {x: x*x for x in range(1, 6)}
print(squares) # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Create a dictionary from an existing dictionary
old_prices = {'apple': 1.0, 'banana': 0.5, 'orange': 0.75}
new_prices = {key: value * 1.1 for key, value in old_prices.items()}
print(new_prices) # Output: {'apple': 1.1, 'banana': 0.55, 'orange': 0.825}
```

## 7. Nested Dictionaries

A dictionary can contain other dictionaries.

```python
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

print(users['user1']['name'])      # Output: Alice
print(users['user2']['email'])     # Output: bob@example.com
```

## Real-Life Use Cases

### 1. Storing User Profiles
Dictionaries are perfect for storing structured information about a user.

```python
user_profile = {
    'username': 'johndoe',
    'email': 'john.doe@example.com',
    'date_joined': '2023-10-27',
    'preferences': {
        'theme': 'dark',
        'notifications': True
    }
}
```

### 2. Configuration Settings
Applications often use dictionaries to manage configuration settings. This makes it easy to read, modify, and manage settings.

```python
db_config = {
    'host': 'localhost',
    'port': 5432,
    'user': 'admin',
    'password': 'secret_password',
    'database': 'my_app_db'
}
```

### 3. Representing JSON Data
JSON (JavaScript Object Notation) is a popular data format. When you load a JSON object in Python (e.g., from a file or an API response), it is typically converted into a dictionary.

**JSON Data:**
```json
{
  "name": "Product A",
  "price": 34.99,
  "in_stock": true,
  "tags": ["electronics", "gadgets"]
}
```

**Python Dictionary:**
```python
import json

json_string = '{"name": "Product A", "price": 34.99, "in_stock": true, "tags": ["electronics", "gadgets"]}'
product_data = json.loads(json_string)

print(product_data['name'])       # Output: Product A
print(product_data['price'])      # Output: 34.99
```

### 4. Caching Results
Dictionaries can be used as a simple in-memory cache to store the results of expensive function calls, avoiding re-computation for the same inputs.

```python
import time

_cache = {}

def expensive_function(arg):
    if arg in _cache:
        print(f"(Returning from cache for {arg})")
        return _cache[arg]

    print(f"(Computing for {arg})")
    time.sleep(2) # Simulate a long computation
    result = arg * arg
    _cache[arg] = result
    return result

print(expensive_function(4))
print(expensive_function(10))
print(expensive_function(4)) # This will be fast
```

### 5. Counting Frequencies
A common task is to count the occurrences of items in a list. A dictionary is an efficient way to do this.

```python
words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

print(word_counts) # Output: {'apple': 3, 'banana': 2, 'orange': 1}
```
