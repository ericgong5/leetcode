class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')' : '(', '}' : '{', ']' : '['}
        stack = []
        
        for char in s:
            if char in mapping:
                if stack and stack[-1] == mapping[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return True if not stack else False




use mapping instead







###
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = ['a']
        for i in s:
            if i == '}':
                if stack[-1] != '{':
                    return False
                stack.pop()
            elif i == ')':
                if stack[-1] != '(':
                    return False
                stack.pop()
            elif i == ']':
                if stack[-1] != '[':
                    return False
                stack.pop()
            else:
                stack.append(i)
        if stack[-1] == 'a':
            return True
        return False
###
