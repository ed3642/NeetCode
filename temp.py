class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        
        stack = [] # mono dec stack from left
        res = [0] * len(temperatures)

        for i in range(len(temperatures) - 1, -1, -1):
            temp = temperatures[i]

            while stack and temp >= temperatures[stack[-1]]:
                stack.pop()
            # record days until next warmer
            if stack:
                res[i] = stack[-1] - i

            stack.append(i)

        
        return res