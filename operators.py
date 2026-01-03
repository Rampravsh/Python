# Arithmetic operator

print('sum:' ,4+3)
print('difference:' ,4-3)
print('product:' ,4*3)
print('division:' ,4/3)
print('floor division:' ,4//3)
print('remainder:' ,4%3)
print('exponentiation:' ,4**3)

# Assignment Operators

print('sum:' ,4+3)
# Simple assignment
x = 5          # x -> 5

# Augmented arithmetic assignments
x += 3         # x -> 8
x -= 2         # x -> 6
x *= 4         # x -> 24
x /= 2         # x -> 12.0   (true division → float)
x //= 5        # x -> 2      (floor division)
x %= 3         # x -> 2      (modulo)
x **= 2        # x -> 4      (power)

# Bitwise augmented assignments
a = 0b1100     # 12
a &= 0b1010    # a -> 0b1000 (8)
a |= 0b0011    # a -> 0b1011 (11)
a ^= 0b0101    # a -> 0b1110 (14)
a <<= 1        # left shift
a >>= 2        # right shift

# Sequence and mapping assignments
lst = [1, 2]
lst += [3]     # lst -> [1, 2, 3]   (extends list in-place)
lst *= 2       # lst -> [1,2,3,1,2,3] (repeats list)

d = {'a': 1}
d |= {'b': 2}  # dict merge/in-place (Python 3.9+) -> {'a':1,'b':2}

# Assignment expression (walrus operator, Python 3.8+)
if (n := len(lst)) > 3:
    print(n)   # assigns and uses n in the same expression

# 🔍 Comparison operators

5 == 5   # True
5 != 3   # True
5 > 3    # True
5 < 3    # False
5 >= 5   # True
5 <= 4   # False

# 🔀 Logical operators
True and False   # False
True or False    # True
not True         # False
# short-circuit behavior:
0 and 5          # 0
1 or 5           # 1

# 🔗 Identity operators
a = [1,2]
b = a
c = [1,2]
a is b    # True   (same object)
a is c    # False  (same contents, different objects)
a is not c # True

# 📚 Membership operators
3 in [1,2,3]     # True
'p' in 'python'  # True
4 not in {1,2,3} # True


# ❓ Ternary (conditional) expression
x = 5
'positive' if x > 0 else 'non-positive'  # 'positive'