# 1. Hello world ... by YOUR_NAME
name = "Aasiya"   # replace with your actual name
print("Hello World ... by", name)


# 2. Create 2 variables cost_price, selling_price and calculate profit or loss
cost_price = float(input("Enter cost price: "))
selling_price = float(input("Enter selling price: "))

if selling_price > cost_price:
    profit = selling_price - cost_price
    print("Profit:", profit)
elif cost_price > selling_price:
    loss = cost_price - selling_price
    print("Loss:", loss)
else:
    print("No profit, no loss")


# 3. Check whether the number is odd or even
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")


# 4. Check whether the age is valid and eligible for voting or not
age = int(input("Enter your age: "))

if age < 0 or age > 120:
    print("Invalid age")
elif age >= 18:
    print("Valid age - Eligible for voting")
else:
    print("Valid age - Not eligible for voting")


# 5. Check whether word1 and word2 are Anagrams or not
word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

# Ignore case and spaces, then compare sorted letters
if sorted(word1.lower().replace(" ", "")) == sorted(word2.lower().replace(" ", "")):
    print(word1, "and", word2, "are Anagrams")
else:
    print(word1, "and", word2, "are NOT Anagrams")