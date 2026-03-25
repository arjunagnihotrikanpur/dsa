# Sum of 1 to n using Functional Recursion

def func(n):
    if (n == 1):
        return 1
    return n + func(n-1)


print(func(4))