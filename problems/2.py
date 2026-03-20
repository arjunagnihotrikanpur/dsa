# Count Number Of Digits in an integer

# Approach 1: Using Loop : O(log10N)
n = int(input("Enter N: "))
count = 0
while (n > 0):
    n = n // 10
    count += 1
    
print("Number Of Digits: " + str(count))


# Approach 2: Using Logarithmic Function : O(1)
import math

n = int(input("Enter a Number: "))
print(int(1 + math.log(n, 10)))