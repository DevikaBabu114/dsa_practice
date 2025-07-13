"""A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forwards and backwards.
Your task is to write a program that determines whether a given string S is a palindrome according to this definition."""
def isPalindrome(s):
    r=""
    for  ch in s:
        if ch.isalnum():
            r+=ch.lower()
    for i in range(len(r)//2):
        if r[i]!=r[len(r)-i-1]:
            return False 
    return True

s=input("string:")
print(isPalindrome(s))