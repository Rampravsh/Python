# 1. Basic Function
def greet():
    """This function prints a greeting."""
    print("Hello, welcome to our program!")

print("--- Example 1: Basic Function ---")
greet()
print("-" * 20)


# 2. Function with Parameters
def greet_user(name):
    """This function greets the user by name."""
    print(f"Hello, {name}!")

print("--- Example 2: Function with Parameters ---")
greet_user("Alice")
greet_user("Bob")
print("-" * 20)


# 3. Function with Return Value
def add_numbers(a, b):
    """This function returns the sum of two numbers."""
    return a + b

print("--- Example 3: Function with Return Value ---")
sum_result = add_numbers(5, 3)
print(f"The sum is: {sum_result}")
print(f"The sum of 10 and 20 is: {add_numbers(10, 20)}")
print("-" * 20)


# 4. Function with Default Parameter Value
def display_info(name, age=30):
    """This function displays user information with a default age."""
    print(f"Name: {name}, Age: {age}")

print("--- Example 4: Function with Default Parameter Value ---")
display_info("Charlie")  # Age will be the default value (30)
display_info("David", 45)  # Age is provided
print("-" * 20)


# 5. Function with Arbitrary Arguments (*args)
def print_fruits(*fruits):
    """This function prints all the fruits passed as arguments."""
    print("List of fruits:")
    for fruit in fruits:
        print(f"- {fruit}")

print("--- Example 5: Function with Arbitrary Arguments (*args) ---")
print_fruits("Apple", "Banana", "Cherry")
print("-" * 20)


# 6. Function with Keyword Arguments (**kwargs)
def build_profile(**user_info):
    """This function builds a user profile from keyword arguments."""
    print("User Profile:")
    for key, value in user_info.items():
        print(f"- {key.title()}: {value}")

print("--- Example 6: Function with Keyword Arguments (**kwargs) ---")
build_profile(name="Eve", location="Cityville", occupation="Engineer")
print("-" * 20)


# 7. Lambda Function
multiply = lambda x, y: x * y

print("--- Example 7: Lambda Function ---")
product = multiply(4, 5)
print(f"The product is: {product}")
print("-" * 20)


# 8. Recursive Function
def factorial(n):
    """This function calculates the factorial of a number recursively."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print("--- Example 8: Recursive Function ---")
num = 5
print(f"The factorial of {num} is: {factorial(num)}")
print("-" * 20)
