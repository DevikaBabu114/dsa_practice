#Write a python program to verify if the given input string, combinations of characters '{' and '}', is well formed.
def isMatching(s):
    count = 0
    for ch in s:
        if ch == '{' :
            count+=1
        elif ch == '}' :
            count-=1
        if count == -1 :
            break
    if count == 0 :
        return "Matching"
    else :
        return "Not Matching"
            
s = input("string :")
print(isMatching(s))