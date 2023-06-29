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
