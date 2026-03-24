# Question:
# Give an array n and array m, find how many time each element of m is present in n.
# Constraints:
# 1 <= n[i] <= 10
# n amd m can both have 10^8 elements

# Approach 1:
# TC: O(n*m)
# -> Might Give TLE as 10^8 x 10^8 = 10^16 operations

n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,6,7,2]

for num in m:
    count = 0
    for x in n:
        if (num == x):
            count += 1
    print(f"{num}: {count}")


# Approach 2 - Using Hash List
# TC: O(N+M)
# SC: O(1) - Since we are using a hash list of fixed size 11, the space complexity is O(1)
hash_list = [0] * 11 # Since n[i] <= 10, we can create a hash list of size 11 (0 to 10)
for num in n::
    if ((x < 1) or (x > 10)):
        print(0)
    else:
        print(hash_list[x])
    