# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# defined API
class Robot:
   def move(self):
       """
       Returns true if the cell in front is open and robot moves into the cell.
       Returns false if the cell in front is blocked and robot stays in the current cell.
       :rtype bool
       """

   def turnLeft(self):
       """
       Robot will stay in the same cell after calling turnLeft/turnRight.
       Each turn will be 90 degrees.
       :rtype void
       """

   def turnRight(self):
       """
       Robot will stay in the same cell after calling turnLeft/turnRight.
       Each turn will be 90 degrees.
       :rtype void
       """

   def clean(self):
       """
       Clean the current cell.
       :rtype void
       """

class Solution:
    def cleanRoom(self, robot: Robot):
        """
        :type robot: Robot
        :rtype: None
        """

        def reset_position():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnLeft()
            robot.turnLeft()

        def backtrack(visited, cell, dir_index):
            visited.add(cell)
            robot.clean()
            print(cell, dir_index)
            # try each direction
            for i in range(4):
                # to keep track of visited cells
                n_dir_index = (dir_index + i) % 4
                n_cell = (cell[0] + directions[n_dir_index][0], cell[1] + directions[n_dir_index][1])

                if n_cell not in visited and robot.move():
                    backtrack(visited, n_cell, n_dir_index)
                    reset_position() # undo robot.move()
                robot.turnRight()

            return # tried all directions

        # ordered by starting pointing up
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] # the starting dir is always up by problem def

        backtrack(set(), (0, 0), 0)

