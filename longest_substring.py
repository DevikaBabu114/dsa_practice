#length of longest sub string of a given string which contains exactly k unique characters.
def longest_substring(s,k):
    l,r=0,0
    d={}
    maxlen=0
    while r<len(s) and l<=r:

        if s[r] not in d:
            d[s[r]]=1
        else:
            d[s[r]]+=1

        while len(d)>k: 
            d[s[l]]-=1
            if d[s[l]] == 0:
                d.pop(s[l])
            l+=1

        if len(d) == k:
            maxlen=max(maxlen,r-l+1)
            r+=1
        elif len(d) < k:
            r+=1

    return maxlen

s=input("string:")
k=int(input("k:"))
print(longest_substring(s,k))