def threeSum(nums):
    nums.sort()
    result=[]
    index1 = 0
    length = len(nums)
    while index1 < length  :
        if index1>0 and nums[index1] == nums[index1-1] :
            index1 += 1
            continue
        index2 = index1 + 1
        index3 = length - 1
        target = 0 - nums[index1]
        while index2 < index3  :
            if nums[index2] + nums[index3] == target:
                result.append([nums[index1],nums[index2],nums[index3]])
                index2 += 1
                index3 -= 1
                while index2<index3 and nums[index2]==nums[index2-1]:
                    index2+=1
            elif nums[index2] + nums[index3] < target:
                index2 += 1
            else:
                index3 -= 1
        index1 +=1
    return result
a = list(map(int,input().split()))
print(threeSum(a)) 