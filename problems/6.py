# Frequency Map - Approach 1
# TC: O(n)

nums = [5,6,7,7,1,9,111,1,1,5,1,1]

freq_map = {}

for i in range(0, len(nums)):
    if (nums[i] in freq_map):
        freq_map[nums[i]] += 1
    else:
        freq_map[nums[i]] = 1
        
print(freq_map)


# Approach- 2 - Using get() method
hash_map = {}
n = len(nums)
for i in range(0, n):
    hash_map[nums[i]] = hash_map.get(nums[i], 0) + 1

print(hash_map)

# {}.get => If key is present in the dictionary, it returns the value of that key. If key is not present, it returns the default value provided as the second argument to the get() method. If the default value is not provided, it returns None.
# Here, 0 is the default value