# Python Tuple Examples: Basic to Advanced

# 1. Basic Tuple Creation and Accessing Elements
print("--- 1. Basic Tuple Creation ---")
basic_tuple = (1, 2, 3, "hello", "world")
print(f"Original tuple: {basic_tuple}")
print(f"First element: {basic_tuple[0]}")
print(f"Last element: {basic_tuple[-1]}")
print(f"Slice from index 1 to 3: {basic_tuple[1:4]}")
print("\\n")

# 2. Immutability
print("--- 2. Immutability ---")
# The following line would raise a TypeError because tuples are immutable
# basic_tuple[0] = 99
print("Tuples are immutable. You cannot change their elements after creation.")
try:
    basic_tuple[0] = 99
except TypeError as e:
    print(f"Attempting to change an element raises a TypeError: {e}")
print("\\n")

# 3. Tuple Packing and Unpacking
print("--- 3. Tuple Packing and Unpacking ---")
# Packing
packed_tuple = 10, 20, "thirty" 
print(f"Packed tuple: {packed_tuple}")

# Unpacking
a, b, c = packed_tuple
print("Unpacked variables:")
print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")

# Unpacking with *
d, *e, f = (10, 20, 30, 40, 50)
print("\\nUnpacking with *:")
print(f"d: {d}")
print(f"e: {e}")
print(f"f: {f}")
print("\\n")

# 4. Tuple Methods: count() and index()
print("--- 4. Tuple Methods ---")
method_tuple = (1, 2, 2, 3, 4, 2, 5)
print(f"Tuple for methods: {method_tuple}")
print(f"Count of '2' in the tuple: {method_tuple.count(2)}")
print(f"Index of the first '3': {method_tuple.index(3)}")
print("\\n")

# 5. Nested Tuples
print("--- 5. Nested Tuples ---")
nested_tuple = ((1, 2), ("a", "b"), (True, False))
print(f"Nested tuple: {nested_tuple}")
print(f"Accessing the second element of the first inner tuple: {nested_tuple[0][1]}")
print(f"Accessing the first element of the second inner tuple: {nested_tuple[1][0]}")
print("\\n")

# 6. Tuples with Mixed Data Types
print("--- 6. Mixed Data Types ---")
mixed_tuple = (1, "apple", 3.14, [1, 2, 3], {"key": "value"})
print(f"Tuple with mixed data types: {mixed_tuple}")
# Note: While the tuple is immutable, mutable objects inside it (like a list) can be changed.
mixed_tuple[3].append(4)
print(f"After modifying the list inside the tuple: {mixed_tuple}")
print("\\n")

# 7. Singleton Tuple (Tuple with one element)
print("--- 7. Singleton Tuple ---")
not_a_tuple = (5) # This is just the integer 5
singleton_tuple = (5,) # The trailing comma makes it a tuple
print(f"This is not a tuple: {type(not_a_tuple)}")
print(f"This is a singleton tuple: {type(singleton_tuple)}")
print("\\n")

# 8. Using Tuples as Dictionary Keys
print("--- 8. Tuples as Dictionary Keys ---")
# Since tuples are immutable and hashable, they can be used as dictionary keys.
location_coordinates = {
    (34.0522, -118.2437): "Los Angeles",
    (40.7128, -74.0060): "New York City"
}
print("Dictionary with tuple keys:")
print(location_coordinates)
print(f"City at (40.7128, -74.0060): {location_coordinates[(40.7128, -74.0060)]}")
print("\\n")

# 9. Returning Multiple Values from a Function (as a tuple)
print("--- 9. Returning Multiple Values ---")
def get_user_info():
    name = "Alice"
    age = 30
    city = "Wonderland"
    return name, age, city # This returns a tuple

user_data = get_user_info()
print(f"Function returned a tuple: {user_data}")

# You can directly unpack the result
user_name, user_age, user_city = get_user_info()
print(f"Unpacked directly: Name: {user_name}, Age: {user_age}, City: {user_city}")
print("\\n")

# 10. Advanced: namedtuple (from the collections module)
print("--- 10. namedtuple ---")
from collections import namedtuple

# Create a namedtuple 'class'
Point = namedtuple('Point', ['x', 'y', 'z'])

# Create an instance of the namedtuple
p1 = Point(10, 20, 30)
print(f"A namedtuple instance: {p1}")

# Access fields by name or index
print(f"Access by name (p1.x): {p1.x}")
print(f"Access by index (p1[1]): {p1[1]}")
print(f"Fields of the namedtuple: {p1._fields}")
print("\\n")
