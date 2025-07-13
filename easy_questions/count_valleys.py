"""Count the number of valleys. 
You are given a string that represent steps in combination of U and D characters.
U represents to take a step up in level. 
D represents to take a step down in level.

You always start at sea level.
A valley is a dip from sea level and back to sea level."""

s=input("enter :")
level=0
valley=0
for ch in s:
    if ch == 'U':
        level+=1
        if level==0:
            valley+=1
    elif ch == 'D':
        level-=1
print(valley)