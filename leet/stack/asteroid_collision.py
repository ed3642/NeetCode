class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        # like car traffic problem

        stack = []

        for obj in asteroids:
            if obj < 0:
                opposing = 0
                result = obj
                while stack and stack[-1] > 0 and result <= 0:
                    opposing = stack.pop()
                    if abs(obj) < opposing:
                        result = opposing
                    elif abs(obj) > opposing:
                        result = obj
                    else:
                        result = 0
                        break
                if result != 0:
                    stack.append(result)
            else:
                stack.append(obj)

        return stack