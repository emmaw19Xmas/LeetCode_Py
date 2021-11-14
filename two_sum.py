"""Emma - Fisrt Try"""
from typing import List


def twoSum(nums, target):
    for i in range(0,len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target:
                print(i,j)

# nums = [3, 2, 4]
# target = 7
twoSum(nums=[3,2,4],target=7)

