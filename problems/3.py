# Problem 3 - Check if a number is pallindrome or not

newNum = 0

num = int(input("Enter a number: "))
numCopy = num
while (numCopy != 0):
    lastDigit = numCopy % 10
    newNum = (newNum * 10) + lastDigit 
    numCopy = numCopy // 10

print(newNum)
if (num == newNum):
    print("Pallindrome!")
else:
    print("Not a pallindrome!")
    