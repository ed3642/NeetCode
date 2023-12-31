from collections import deque

class Solution:
    # trick was to calculate finish times
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        def carTimeToTarget(pos, vel) -> float:
            return (target - pos) / vel
        
        finish_times = [carTimeToTarget(position[i], speed[i]) for i in range(len(position))]
        cars = sorted(zip(position, finish_times))

        stack = deque([cars.pop()])
        
        for car in cars[::-1]:
            top_car = stack[-1]
            if not car[1] <= top_car[1]: # car and top_car DO NOT become a fleet
                stack.append(car)

        return len(stack)
    
    def carFleet2(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort()
        finish_times = [(target - car[0]) / car[1] for car in cars]
        
        stack = deque([finish_times[-1]])

        for i in range(len(finish_times) - 1, -1, -1):
            time = finish_times[i]
            if time > stack[-1]:
                stack.append(time)

        return len(stack)


s = Solution()

target = 16
pos = [6,11,13,14]
vel = [7,2,6,2]

print(s.carFleet(target, pos, vel))