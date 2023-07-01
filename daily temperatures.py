class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        answer = [0] * len(temperatures)
        stack = []
        indexes = []
        stack.append(temperatures[0])
        indexes.append(0)
        for i in range(1,len(temperatures)):
            while stack and stack[-1] < temperatures[i]:
                days = i - indexes[-1]
                answer[indexes[-1]] = days
                stack.pop()
                indexes.pop()

            stack.append(temperatures[i])
            indexes.append(i)
        return answer
