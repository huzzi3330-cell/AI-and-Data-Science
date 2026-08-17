# Python Operators Assignment

# ==========================================
# Part 1: Arithmetic Operators
# ==========================================

a = 15
b = 4

print("Addition: a + b =", a + b)
print("Subtraction: a - b =", a - b)
print("Multiplication: a * b =", a * b)
print("Division: a / b =", a / b)
print("Floor Division: a // b =", a // b)
print("Modulus: a % b =", a % b)
print("Exponentiation: a ** b =", a ** b)

# Expected:
# Floor Division = 3
# Modulus = 3


# ==========================================
# Part 2: Arithmetic Assignment Operators
# ==========================================

x = 10

print("\nInitial value of x:", x)

x += 5
print("After x += 5:", x)

x *= 2
print("After x *= 2:", x)

x -= 4
print("After x -= 4:", x)

x /= 2
print("After x /= 2:", x)

# Expected final value = 13.0


# ==========================================
# Part 3: Comparison Operators
# ==========================================

a = 7
b = 10

print("\na == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

# True comparisons:
# a != b
# a < b
# a <= b


# ==========================================
# Part 4: Logical Operators
# ==========================================

x = True
y = False

print("\nx and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)


# ==========================================
# Part 5: Membership Operators
# ==========================================

institute = "Saylani Mass IT"

print("\n's' in institute:", "s" in institute)
print("'Mass' in institute:", "Mass" in institute)
print("'Saylani' not in institute:", "Saylani" not in institute)


# ==========================================
# Part 6: Identity Operators
# ==========================================

a = 5
b = 5
c = 1000

print("\na is b:", a is b)
print("a is c:", a is c)
print("c is not b:", c is not b)


# ==========================================
# Bonus Challenge
# ==========================================

username = input("\nEnter username: ")
password = input("Enter password: ")

if username == "Talha" and password == "Axiom123":
    print("Login successful")
else:
    print("Invalid username or password")
