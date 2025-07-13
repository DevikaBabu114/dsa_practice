"""You are given an array of integers, arr, and a non-negative integer K. Your task is to find the number of unique pairs (a, b) from the array such that the absolute difference between a and b is exactly K.
A pair (a, b) is considered unique if the values a and b are distinct. The order of elements in a pair does not matter (i.e., (a, b) is the same as (b, a)). If the array contains duplicate numbers, each unique pair of values should be counted only once"""
def Count_Distinct_Pairs(n,arr,k):
    result=[]
    for i in range(n):
        for j in range(i+1,n):
            if abs(arr[i]-arr[j])==k and [arr[i],arr[j]] not in result and [arr[j],arr[i]] not in result:
                result.append([arr[i],arr[j]])
                print([arr[i],arr[j]])
                break
    return len(result)
n =int(input("n:"))
arr=list(map(int,input("array:").split()))
k=int(input("k:"))
print("distinct pairs",Count_Distinct_Pairs(n,arr,k))