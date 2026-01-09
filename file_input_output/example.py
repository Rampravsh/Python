"""
This file contains examples of file input and output in Python, from basic to advanced.
"""

# =============================================================================
# Basic File I/O
# =============================================================================

# -----------------------------------------------------------------------------
# 1. Writing to a file
# -----------------------------------------------------------------------------

# Open a file for writing. If the file doesn't exist, it will be created.
# If it does exist, its contents will be overwritten.
with open("sample.txt", "w") as f:
    f.write("Hello, world!\n")
    f.write("This is a sample file.\n")

print("--- Created and wrote to sample.txt ---")

# -----------------------------------------------------------------------------
# 2. Reading from a file
# -----------------------------------------------------------------------------

# Reading the entire file at once
print("\n--- Reading entire file: ---")
with open("sample.txt", "r") as f:
    content = f.read()
    print(content)

# Reading a file line by line
print("\n--- Reading file line by line: ---")
with open("sample.txt", "r") as f:
    for line in f:
        print(line, end="")

# Reading all lines into a list
print("\n\n--- Reading all lines into a list: ---")
with open("sample.txt", "r") as f:
    lines = f.readlines()
    print(lines)

# -----------------------------------------------------------------------------
# 3. Appending to a file
# -----------------------------------------------------------------------------

with open("sample.txt", "a") as f:
    f.write("This line is appended.\n")

print("\n--- Appended to sample.txt, new content: ---")
with open("sample.txt", "r") as f:
    print(f.read())


# =============================================================================
# Working with different data structures
# =============================================================================

# -----------------------------------------------------------------------------
# 4. CSV Files
# -----------------------------------------------------------------------------
import csv

# Writing to a CSV file
header = ["name", "age", "city"]
data = [
    ["Alice", 25, "New York"],
    ["Bob", 30, "Los Angeles"],
    ["Charlie", 35, "Chicago"],
]

with open("sample.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)

print("\n--- Created and wrote to sample.csv ---")

# Reading from a CSV file
print("\n--- Reading from sample.csv: ---")
with open("sample.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# -----------------------------------------------------------------------------
# 5. JSON Files
# -----------------------------------------------------------------------------
import json

# Writing to a JSON file
data_dict = {
    "name": "John Doe",
    "age": 30,
    "isStudent": False,
    "courses": [{"title": "History", "credits": 3}, {"title": "Math", "credits": 4}],
}

with open("sample.json", "w") as f:
    json.dump(data_dict, f, indent=4)

print("\n--- Created and wrote to sample.json ---")

# Reading from a JSON file
print("\n--- Reading from sample.json: ---")
with open("sample.json", "r") as f:
    loaded_data = json.load(f)
    print(json.dumps(loaded_data, indent=4))


# =============================================================================
# Advanced File I/O
# =============================================================================

# -----------------------------------------------------------------------------
# 6. Binary Files (e.g., images, executables)
# -----------------------------------------------------------------------------

# Writing binary data
with open("sample.bin", "wb") as f:
    f.write(b"\xDE\xAD\xBE\xEF")

print("\n--- Created and wrote to sample.bin ---")

# Reading binary data
with open("sample.bin", "rb") as f:
    binary_content = f.read()
    print(f"\n--- Reading from sample.bin: {binary_content} ---")


# -----------------------------------------------------------------------------
# 7. In-memory file-like objects
# -----------------------------------------------------------------------------
import io

# Using StringIO for in-memory text streams
string_io = io.StringIO()
string_io.write("This is a line in a string buffer.\n")
string_io.write("Another line.")

# To read it, we need to reset the cursor
string_io.seek(0)
print("\n--- Reading from in-memory StringIO: ---")
print(string_io.read())
string_io.close()

# -----------------------------------------------------------------------------
# 8. Pickling - Serializing Python Objects
# -----------------------------------------------------------------------------
import pickle

class MyObject:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"MyObject(name='{self.name}')"

my_obj = MyObject("Test Object")

# Serialize and write to a file
with open("data.pkl", "wb") as f:
    pickle.dump(my_obj, f)

print("\n--- Serialized and saved object to data.pkl ---")

# Deserialize and read from the file
with open("data.pkl", "rb") as f:
    loaded_obj = pickle.load(f)
    print(f"\n--- Deserialized object from data.pkl: {loaded_obj} ---")

print("\nAll file I/O examples have been created.")
