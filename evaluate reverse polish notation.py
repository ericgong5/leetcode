class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(c))
        return stack[0]


###
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
        
