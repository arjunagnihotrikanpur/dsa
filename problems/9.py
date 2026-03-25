# Recursion
# Print Arjun 4 Times
count = 0
def func():
    global count
    if (count > 3):
        return
    print("Arjun")
    count += 1
    func()

func()