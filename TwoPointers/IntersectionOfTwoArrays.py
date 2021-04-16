# Given two integer arrays nums1 and nums2, return an array of their intersection. 
# Each element in the result must appear as many times as it shows in both arrays and 
# you may return the result in any order.

# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.

from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = self.makeDict(nums1)
        dict2 = self.makeDict(nums2)
        res = []
        for num in dict1.keys():
            if dict2.get(num):
                count = dict1[num] if dict1[num] < dict2[num] else dict2[num]
                for i in range(count):
                    res.append(num)
        return res
    def makeDict(self, nums: List[int]) -> dict:
        dict = {}
        for num in nums:
            if num not in dict.keys():
                dict[num] = 1
            else:
                dict[num] += 1
                
        return dict

obj = Solution()

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

print(f"Intersection of two arrays: {obj.intersect(nums1, nums2)}")