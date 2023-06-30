class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []

        for i in tokens:
            if i == "+":
                secondTerm = stack.pop()
                firstTerm = stack.pop()
                result = int(firstTerm) + int(secondTerm)
                stack.append(str(result))
            elif i == "-":
                secondTerm = stack.pop()
                firstTerm = stack.pop()
                result = int(firstTerm) - int(secondTerm)
                stack.append(str(result))
            elif i == "*":
                secondTerm = stack.pop()
                firstTerm = stack.pop()
                result = int(firstTerm) * int(secondTerm)
                stack.append(str(result))
            elif i == "/":
                secondTerm = stack.pop()
                firstTerm = stack.pop()
                result = int(firstTerm) / int(secondTerm)
                if abs(result) < 1:
                    result = 0
                stack.append(str(result))
            else:
                stack.append(i)
        print(stack[0])
        return int(stack[-1])
        
