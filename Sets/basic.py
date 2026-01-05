# Sets in Python

# A set is an unordered collection of unique items.

# -------------------------------------------------------------------

# 1. Creating a Set
# Sets can be created by enclosing comma-separated items in curly braces {}.
# Duplicate elements are automatically removed.

my_set = {1, 2, 3, 4, 5, 1, 2}
print(f"Initial set: {my_set}")  # Output: {1, 2, 3, 4, 5}

# Creating a set from a list
list_items = ['apple', 'banana', 'cherry', 'apple']
set_from_list = set(list_items)
print(f"Set from list: {set_from_list}")  # Output: {'banana', 'cherry', 'apple'}

# Creating an empty set
empty_set = set()
print(f"Empty set: {empty_set}")

# -------------------------------------------------------------------

# 2. Adding items to a Set

# add(): Adds a single element to the set.
my_set.add(6)
print(f"After adding 6: {my_set}")

# update(): Adds multiple items from an iterable (like a list, tuple, or another set).
my_set.update([7, 8, 2])
print(f"After updating with [7, 8, 2]: {my_set}")

# -------------------------------------------------------------------

# 3. Removing items from a Set

# remove(): Removes a specified element. Raises a KeyError if the element is not found.
my_set.remove(8)
print(f"After removing 8: {my_set}")

# discard(): Removes a specified element. Does not raise an error if the element is not found.
my_set.discard(9)  # 9 is not in the set, but no error is raised.
my_set.discard(1)
print(f"After discarding 1 and 9: {my_set}")

# pop(): Removes and returns an arbitrary element from the set. Raises a KeyError for an empty set.
popped_element = my_set.pop()
print(f"Popped element: {popped_element}")
print(f"Set after pop: {my_set}")

# clear(): Removes all elements from the set.
my_set.clear()
print(f"After clearing the set: {my_set}")

# -------------------------------------------------------------------

# 4. Set Operations

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print(f"\nSet A: {set_a}")
print(f"Set B: {set_b}")

# Union: Returns a new set containing all items from both sets.
union_set = set_a.union(set_b)
# Alternatively: union_set = set_a | set_b
print(f"Union of A and B: {union_set}")

# Intersection: Returns a new set containing only items present in both sets.
intersection_set = set_a.intersection(set_b)
# Alternatively: intersection_set = set_a & set_b
print(f"Intersection of A and B: {intersection_set}")

# Difference: Returns a new set with items in the first set but not in the second.
difference_set = set_a.difference(set_b)  # Elements in A but not in B
# Alternatively: difference_set = set_a - set_b
print(f"Difference A - B: {difference_set}")

difference_set_b = set_b.difference(set_a) # Elements in B but not in A
# Alternatively: difference_set_b = set_b - set_a
print(f"Difference B - A: {difference_set_b}")

# Symmetric Difference: Returns a new set with items in either set, but not in both.
sym_diff_set = set_a.symmetric_difference(set_b)
# Alternatively: sym_diff_set = set_a ^ set_b
print(f"Symmetric Difference of A and B: {sym_diff_set}")

# -------------------------------------------------------------------

# 5. Set Membership Test
print(f"Is 3 in Set A? {3 in set_a}")        # Output: True
print(f"Is 7 in Set A? {7 not in set_a}")   # Output: True

# -------------------------------------------------------------------

# 6. Set Methods for Subsets and Supersets

set_c = {1, 2, 3}
set_d = {1, 2, 3, 4, 5}

# issubset(): Checks if all elements of a set are present in another set.
print(f"Is C a subset of D? {set_c.issubset(set_d)}")  # Output: True

# issuperset(): Checks if a set contains all elements of another set.
print(f"Is D a superset of C? {set_d.issuperset(set_c)}")  # Output: True

# -------------------------------------------------------------------

# 7. Looping through a Set
print("\nLooping through Set D:")
for item in set_d:
    print(item)

# -------------------------------------------------------------------

# 8. Set Comprehension
# A concise way to create sets.
squared_set = {x**2 for x in range(1, 6)}
print(f"\nSet of squares from 1 to 5: {squared_set}")
