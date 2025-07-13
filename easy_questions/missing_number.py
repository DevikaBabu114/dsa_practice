"""You are given an array nums containing n distinct numbers. These n numbers are taken from the range [0, n]. Your task is to find and return the only number in the range [0, n] that is missing from the array."""
def missing_number(n,arr):
    array_sum=0
    largest=0
    for num in arr:
        largest=max(largest,num)
        array_sum+=num
    largest=max(largest,n)
    total=(largest*(largest+1))//2
    missing_no=total-array_sum
    return missing_no
n =int(input("n:"))
arr=list(map(int,input("array:").split()))
print(missing_number(n,arr))