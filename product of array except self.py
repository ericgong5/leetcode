class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        answer = [1] * len(nums)

        pre = 1
        for i in range(len(nums)):
            answer[i] = pre * answer[i]
            pre = pre * nums[i]
        post = 1
        for j in range(len(nums)-1,-1,-1):
            answer[j] = post * answer[j]
            post = post * nums[j]
        
        return answer
