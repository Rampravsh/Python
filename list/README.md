# Python Lists: A Comprehensive Guide

This document explains the core concepts of Python lists, ranging from basic operations to advanced techniques, as demonstrated in the accompanying `list.py` script.

## 1. Introduction

Lists are one of the most versatile and commonly used data types in Python. They are:

- **Ordered**: Items have a defined order.
- **Mutable**: You can change, add, and remove items after creation.
- **Heterogeneous**: They can hold items of different data types (strings, integers, objects, etc.).

## 2. Basic Operations

### Creation

You can create a list using square brackets `[]` or the `list()` constructor.

```python
fruits = ['apple', 'mango', 'cherry']
```

### Accessing Elements (Indexing)

- **Positive Indexing**: Starts from `0` (the first item).
- **Negative Indexing**: Starts from `-1` (the last item).

```python
first = fruits[0]   # 'apple'
last = fruits[-1]   # 'cherry'
```

## 3. Slicing

Slicing allows you to access a subset of the list.
**Syntax**: `list[start:stop:step]`

- `start`: Inclusive (default is 0).
- `stop`: Exclusive (default is end of list).
- `step`: The increment (default is 1).

```python
numbers = [0, 1, 2, 3, 4, 5]
subset = numbers[2:5]         # [2, 3, 4]
reversed_list = numbers[::-1] # [5, 4, 3, 2, 1, 0]
```

## 4. Modifying Lists

### Adding Elements

- `append(item)`: Adds an item to the end of the list.
- `insert(index, item)`: Adds an item at a specific position.
- `extend(iterable)`: Merges another list or iterable into the current one.

### Removing Elements

- `remove(value)`: Removes the first occurrence of a specific value.
- `pop(index)`: Removes and returns the item at the given index (default is the last item).
- `del list[index]`: Deletes an item by index or slice.
- `clear()`: Removes all items from the list.

## 5. List Comprehensions

List comprehensions provide a concise way to create lists based on existing lists.
**Syntax**: `[expression for item in iterable if condition]`

```python
# Create a list of squares for even numbers only
squares = [x**2 for x in range(10) if x % 2 == 0]
```

## 6. Sorting

- `sort()`: Sorts the list **in-place** (modifies the original list).
- `sorted(list)`: Returns a **new** sorted list.
- **Custom Sort**: You can use the `key` parameter to define custom sorting logic (e.g., sort by string length).

```python
words = ['apple', 'fig', 'banana']
words.sort(key=len) # Sorts by length of the word
```

## 7. Advanced Concepts

### Unpacking

Python allows you to assign list elements to variables directly. The `*` operator can capture remaining elements.

```python
a, *rest, b = [1, 2, 3, 4, 5]
# Result: a=1, b=5, rest=[2, 3, 4]
```

### Copying: Shallow vs Deep

- **Assignment (`=`)**: Creates a reference, not a copy. Changes to one affect the other.
- **Shallow Copy (`.copy()` or `[:]`)**: Copies the list structure. However, if the list contains mutable objects (like nested lists), those inner objects are still shared references.
- **Deep Copy (`copy.deepcopy()`)**: Recursively copies everything. This is essential for independent copies of nested lists.

```python
import copy
deep_copy_list = copy.deepcopy(original_nested_list)
```

### Iteration with Enumerate

When looping through a list, `enumerate()` allows you to access both the **index** and the **value** simultaneously.

```python
for index, value in enumerate(['a', 'b']):
    print(f"Index: {index}, Value: {value}")
```
