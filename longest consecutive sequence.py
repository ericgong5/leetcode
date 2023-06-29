class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashset = {}
        longest = 0
        for i in nums:
            hashset[i] = 1
        for j in nums:
            curr = j
            count = 1
            if curr-1 not in hashset:
                while True:
                    if curr+1 in hashset:
                        count += 1
                        curr += 1
                    else:
                        break
                if count > longest:
                    longest = count
        
        return longest
