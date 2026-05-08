# -----------------------------------
# 1. Sum of Two Numbers
# -----------------------------------
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum_result = num1 + num2
print("Sum =", sum_result)
print("-----------------------------------")
# -----------------------------------
# 2. Odd or Even Checker
# -----------------------------------
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(number, "is Even")
else:
    print(number, "is Odd")
print("-----------------------------------")
# -----------------------------------
# 3. Factorial Calculation
# -----------------------------------
n = int(input("Enter a number for factorial: "))
factorial = 1
for i in range(1, n + 1):
    factorial = factorial * i
print("Factorial =", factorial)
print("-----------------------------------")
# -----------------------------------
# 4. Fibonacci Sequence
# -----------------------------------
terms = int(input("Enter number of terms: "))
a = 0
b = 1
print("Fibonacci Sequence:")
for i in range(terms):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
print()
print("-----------------------------------")
# -----------------------------------
# 5. String Reverse
# -----------------------------------
text = input("Enter a string: ")
reverse_text = text[::-1]
print("Reversed String =", reverse_text)
print("-----------------------------------")
# -----------------------------------
# 6. Palindrome Check
# -----------------------------------
word = input("Enter a word: ")
if word == word[::-1]:
    print(word, "is a Palindrome")
else:
    print(word, "is NOT a Palindrome")
print("-----------------------------------")
# -----------------------------------
# 7. Leap Year Check
# -----------------------------------
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year")
else:
    print(year, "is NOT a Leap Year")
print("-----------------------------------")
# -----------------------------------
# 8. Armstrong Number
# -----------------------------------
num = int(input("Enter a number: "))
order = len(str(num))
sum_val = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum_val += digit ** order
    temp = temp // 10
if num == sum_val:
    print(num, "is an Armstrong Number")
else:
    print(num, "is NOT an Armstrong Number")
print("-----------------------------------")