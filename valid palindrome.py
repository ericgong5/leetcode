class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s)-1
        while left < right:
            leftWord = s[left]
            rightWord = s[right]
            if not leftWord.isalnum():
                left += 1
            elif not rightWord.isalnum():
                right -= 1
            elif leftWord.lower() != rightWord.lower() :
                return False
            else:
                left += 1
                right -= 1

        return True
