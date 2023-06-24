class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hashset = {}
        occurence = [[] for i in range(len(nums) + 1)]
        answer = []
        count = k

        for i in range(len(nums)):
            hashset[nums[i]] = 1 + hashset.get(nums[i],0)

        for j in hashset.keys():
            occurence[hashset[j]].append(j)

        for k in range(len(nums),0,-1):
                for m in occurence[k]:  
                    answer.append(m)
                    count = count - 1
                    if count == 0:
                        return answer
        
        return answer
