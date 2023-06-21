class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashset = {}


        for i in range(len(strs)):
            key = ''.join(sorted(strs[i]))
            if key in hashset: hashset[key] = hashset[key] + [strs[i]]
            else: hashset[key] = [strs[i]]
        return hashset.values()
