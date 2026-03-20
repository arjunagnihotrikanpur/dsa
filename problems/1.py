# Extraction Of Digits

n = int(input("Enter a number: "))

while (n > 0):
    digit = n % 10
    print(digit)
    n = n // 10
