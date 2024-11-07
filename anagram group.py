class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashset = {}
        fullList = []
        for string in strs:
            sortedString = "".join(sorted(string))
            hashset[sortedString] = hashset.get(sortedString , []) + [string]

        for stringSet in hashset:
            fullList.append(hashset[stringSet])

        return fullList



## get function for dicitonaries with default return value
## append on lists if mutable
## join method
