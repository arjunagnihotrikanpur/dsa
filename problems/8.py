# Same as problem 7 in character version
# Count q[i] in s
# TC: O(S+Q)
# SC: O(1)

s = "azyxyyzaaaa"
q = ["d", "a", "y", "x"]

hash_list = [0] * 26
for ch in s:
    ascii_value = ord(ch)
    index = ascii_value - 97
    hash_list[index] += 1

for ch in q:
    ascii_value = ord(ch)
    index = ascii_value - 97
    print(ch, ":", hash_list[index])