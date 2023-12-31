class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashset = {}

        for i in range(len(nums)):
            if((target-nums[i]) in hashset):
                return [i,hashset[(target-nums[i])]] 
            hashset[nums[i]] = i
