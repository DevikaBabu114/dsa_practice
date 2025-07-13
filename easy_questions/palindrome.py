# Given a string, test for palindrome over any of its permutations.
s=input("string:")
s=s.lower()
d=[0] * 26
for ch in s:
    d[ord(ch)-ord('a')]+=1
odd_count=0
for char_count in d:
    if char_count % 2 != 0:
        odd_count+=1
    if odd_count>1:
        break
print(odd_count<=1)