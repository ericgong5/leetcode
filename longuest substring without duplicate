class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dictionary = {}
        maxLength = 0
        substring = []
        
        for i in range(len(s)):
            while s[i] in substring:
                substring.pop(0)

            substring.append(s[i])
            maxLength = max(len(substring),maxLength)
        return maxLength
