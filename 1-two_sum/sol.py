# Python2
# Question: https://leetcode.com/problems/two-sum/
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        cnum = []
        for indx in range(len(nums)):
          if nums[indx] in cnum:
            return [cnum.index(nums[indx]), indx]
          else: cnum.append(target - nums[indx])
        return []
        
