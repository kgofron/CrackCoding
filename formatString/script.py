# This prints out "Hello, John!"
name = "John"
print("Hello, %s!" % name)

# This prints out "John is 23 years old."
age = 23
print("%s is %d years old." % (name, age))

# This prints out: "A list: [1, 2, 3]"
mylist = [1,2,3]
print("A list: %s" % mylist)

# Basic argument specifiers
#%s - String (or any object with a string representation, like numbers)
#%d - Integers
#%f - Floating point numbers
#%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
#%x/%X - Integers in hex representation (lowercase/uppercase)

#Tuple:  Hello John Doe. Your current balance is $53.44.
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."
print(format_string % data)
format_string = 'Hello {0[0]} {0[1]}. Your current balance is ${0[2]}.'.format(data)
print(format_string)

astring = "Hello world!"
print("single quotes are ' '")
print(len(astring))

print(astring.index("o"))

print(astring.count("l"))

print(astring[3:7])
print(astring[3:7:1])

# This prints the characters of string from 3 to 7 skipping one character. [start:stop:step]
print(astring[3:8:2])

# Reverse string
print(astring[::-1])

# UPPER, lower
print(astring.upper())
print(astring.lower())

# Test starting/ending of string
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))

####################################
s = "Strings are awesome!"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))
########################################

# Conditions
x = 2
print(x == 2) # prints out True
print(x == 3) # prints out False
print(x < 3) # prints out True

# 
name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")

# in
name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")

# if
x = 2
if x == 2:
    print("x equals two!")
else:
    print("x does not equal to two.")

# is operator
x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False

# not operator
print(not False) # Prints out True
print((not False) == (False)) # Prints out False

# Loops: for
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)
# xrange is more efficeint (returns iterator), range returns list with numbers
# Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x)

# Prints out 3,4,5
for x in range(3, 6):
    print(x)

# Prints out 3,5,7
for x in range(3, 8, 2):
    print(x)

# Loop: while; Prints out 0,1,2,3,4
count = 0
while count < 5:
    print(count)
    count += 1  # This is the same as count = count + 1


# break/continue: Prints out 0,1,2,3,4
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)

