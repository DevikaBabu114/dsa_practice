#Check if two strings are anagrams of each other.
def isAnagram(s1,s2):
    if len(s1) != len(s2) :
        return False
    count = {}
    for i in range(len(s1)):
        count[s1[i]] = count.get(s1[i],0) + 1
        count[s2[i]] = count.get(s2[i],0) - 1
        
    for counts in count.values():
        if counts != 0:
            return False
    return True
        
s1 = input("string 1:")
s2 = input("string 2:")
print(isAnagram(s1,s2))