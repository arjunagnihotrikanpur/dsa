# Find Factors of a Number

# Brute Force Approach
# TC: O(n)
result = []
num = int(input("Enter Number: "))

for i in range(1, num+1):
    if (num % i == 0):
        result.append(i)
    
print(result)




# Approach 2 - Iterate till n/2
# TC: O(n/2) => O(n)
num = int(input("Enter a Number: "))
factors = []
for i in range(1, int(num/2)+1):
    if (num % i == 0):
        factors.append(i)


for factor in factors:
    print(factor)
print(num)


# Optimal Approach - Approach 3 - Iterate till sqrt(n)
# O(sqrt(n))
from math import sqrt

result = []
num = int(input("Enter A Number: "))
for i in range(1, int(sqrt(num)) + 1):
    if (num % i == 0):
        result.append(i)
        result.append(int(num / i))
result.pop() # Remove last duplicate
print(result)