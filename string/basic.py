name1='John'
name2="Doe"
name3='''Smith'''
full_name = name1 + " " + name2 + " " + name3
print(full_name)
print(type(full_name))
print(len(full_name))

# Slicing
print(full_name[0:4])
print(full_name[5:])
print(full_name[:4])
print(full_name[-5:-1])

# upper and lower
print(full_name.upper())
print(full_name.lower())

# strip
name4 = "   leading and trailing spaces   "
print(name4.strip())

# replace
print(full_name.replace("John", "Jane"))

# split
print(full_name.split(" "))

# find
print(full_name.find("Doe"))

# format
age = 30
txt = "My name is John, and I am {}"
print(txt.format(age))

# f-strings (Python 3.6+)
print(f"My name is {full_name} and I am {age}")