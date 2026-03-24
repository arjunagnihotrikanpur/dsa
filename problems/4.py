# Amstrong Number

orignal = int(input("Enter a Number: "))

num = orignal

sum = 0
length = len(str(num))
while (num != 0):
    lastDigit = num % 10
    sum += lastDigit ** length
    num = num // 10
    
print (orignal == sum)

# Time Complexity - O(log10n)