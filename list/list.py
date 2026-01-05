# --- 1. Basic Creation and Properties ---
fruits = ['apple', 'mango', 'cherry']
print(f"Original List: {fruits}")
print(f"Type: {type(fruits)}")
print(f"Length: {len(fruits)}")

# --- 2. Accessing Elements (Indexing) ---
print(f"First element: {fruits[0]}")
print(f"Last element (Negative Indexing): {fruits[-1]}")

# --- 3. Slicing [start:stop:step] ---
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Slice [2:5]: {numbers[2:5]}")
print(f"Every 2nd number: {numbers[::2]}")
print(f"Reversed List: {numbers[::-1]}")

# --- 4. Modifying Lists ---
# Changing value
fruits[1] = 'banana'

# Adding items
fruits.append('orange')      # Add to end
fruits.insert(1, 'grape')    # Insert at index 1
fruits.extend(['kiwi', 'melon']) # Add multiple items
print(f"Modified List: {fruits}")

# --- 5. Removing Elements ---
fruits.remove('banana')      # Remove by value
popped_item = fruits.pop()   # Remove last item and return it
del fruits[0]                # Delete by index
print(f"After Removal: {fruits}")
print(f"Popped Item: {popped_item}")

# --- 6. List Comprehensions (Intermediate) ---
# Create a new list of squares for even numbers only
squares = [x**2 for x in range(10) if x % 2 == 0]
print(f"List Comprehension (Squares of evens): {squares}")

# --- 7. Sorting ---
random_nums = [5, 2, 9, 1, 5, 6]
random_nums.sort() # Sorts in-place
print(f"Sorted: {random_nums}")

# Custom Sort (Sort by length of string)
words = ['apple', 'fig', 'banana']
words.sort(key=len)
print(f"Sorted by length: {words}")

# --- 8. Advanced: Unpacking ---
a, *rest, b = [1, 2, 3, 4, 5]
print(f"Unpacking: First={a}, Last={b}, Middle={rest}")

# --- 9. Advanced: Shallow vs Deep Copy ---
import copy

# Nested list
original = [[1, 2], [3, 4]]

# Shallow Copy (Standard .copy())
shallow = original.copy()

# Deep Copy (Requires copy module)
deep = copy.deepcopy(original)

# Modify the nested element in original
original[0][0] = 99

print("\n--- Copying Demo ---")
print(f"Original: {original}")
print(f"Shallow (Affected by nested change): {shallow}")
print(f"Deep (Unaffected): {deep}")

# --- 10. Iteration with Enumerate ---
# Gives you both index and value
print("\n--- Enumerate ---")
for index, value in enumerate(['a', 'b', 'c']):
    print(f"Index {index}: {value}")
