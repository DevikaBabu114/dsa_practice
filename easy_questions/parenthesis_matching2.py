#Write a python program to verify if the given input string, combinations of characters '{'. '}', '[', ']', '(' and ')', is well formed.
def isMatching(s):
    d={'}':'{',']':'[',')':'('}
    stack=[]
    for ch in s :
        if ch in ['{','[','('] :
            stack.append(ch)
        elif ch in ['}',']',')']:
            if len(stack) == 0 or stack[-1] != d[ch]:
                break
            else :
                stack.pop()
    if len(stack) == 0 :
        return "Matching"
    else :
        return "Not Matching"
    
        
s = input("string:")
print(isMatching(s))