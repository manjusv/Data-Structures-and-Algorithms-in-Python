# input string
s = "This is a program to find missing characters to make a string Anagram"
res = ""
# list to keep track of characters already present
present = [False] * 26
for i in range(len(s)):
    if s[i] >= 'A' and s[i] <= 'Z':
        present[ord(s[i]) - ord('A')] = True
    elif s[i] >= 'a' and s[i] <= 'z':
        present[ord(s[i]) - ord('a')] = True

for i, item in enumerate(present):
    if item is False:
        res += chr(i + ord('a'))
print(res)
