from collections import deque

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        fleet_count = 0
        cars = sorted(zip(position, speed))

        def carFinalPos(car: tuple[int, int]):
            return car[0] + car[1] # pos + vel * 1 unit time

        def move(cars: list[tuple[int, int]]) -> deque:
            nonlocal fleet_count
            stack = deque()

            for i in range(len(cars) - 1, -1, -1):
                car = cars[i]
                curr_final_pos = carFinalPos(car)
                if curr_final_pos >= target:
                    fleet_count += 1
                    continue
                curr_final_car = (curr_final_pos, car[1])
                if curr_final_pos <= target and not stack:
                    stack.append(curr_final_car)
                elif stack:
                    top_final_pos = stack[-1][0]
                    if top_final_pos > curr_final_pos:
                        stack.append(curr_final_car)
            return stack

        while cars:
            stack = move(cars)
            temp = []
            print(stack)
            while stack:
                temp.append(stack.pop())
            cars = temp

        return fleet_count


s = Solution()

target = 12
pos = [10,8,0,5,3]
vel = [2,4,1,1,3]

print(s.carFleet(target, pos, vel))