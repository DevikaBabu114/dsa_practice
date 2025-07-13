""" Design an algorithm that takes as input an array A[] and 
a number k, and determine if there are three entries 
in the array (Not necessarily distinct) which add up to 
the specified number k."""
def threeSum(a,k):
    a.sort()
    index1 = 0
    length = len(a)
    while index1 < length  :
        index2 = index1
        index3 = length - 1
        target = k - a[index1]
        while index2 <= index3  :
            if a[index2] + a[index3] == target:
                return True
            elif a[index2] + a[index3] < target:
                index2 += 1
            else:
                index3 -= 1
        index1 +=1
    return False
a = list(map(int,input().split()))
k=int(input())
print(threeSum(a,k)) 