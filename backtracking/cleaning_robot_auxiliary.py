import matplotlib.pyplot as plt
import matplotlib.animation as animation

# List of cells visited by the robot
cells = [(0, 0), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, -2), (-1, -3), (0, -3), (1, -3), (0, -2), (2, 0), (3, 0), (3, -1), (3, -2), (3, -3), (3, 1), (3, 2), (3, 3), (3, 4), (1, 2), (1, 3), (1, 4), (0, 4), (-1, 4), (-1, 3), (0, 3)]
# List of directions the robot is facing
directions = [0, 0, 1, 2, 2, 3, 3, 0, 0, 3, 3, 2, 2, 1, 2, 2, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 0, 0, 3, 2]

# List of colors
colors = ['red', 'green', 'blue', 'purple']

# Create a figure and a plot
fig, ax = plt.subplots()

# Set the limits and grid of the plot
ax.set_xlim(-4, 5)
ax.set_ylim(-2, 4)
ax.grid(True)

# Invert the y-axis
ax.invert_yaxis()

# Function to update the plot for each frame
def update(i):
    ax.scatter(cells[i][1], cells[i][0], color='blue')  # Swap x and y
    ax.text(cells[i][1], cells[i][0], str(i), color='black', fontsize=12)  # Add step number
    color = colors[directions[i] % len(colors)]
    if directions[i] == 0:  # up
        ax.arrow(cells[i][1], cells[i][0], 0, -0.5, head_width=0.1, color=color)  # Swap x and y
    elif directions[i] == 1:  # right
        ax.arrow(cells[i][1], cells[i][0], 0.5, 0, head_width=0.1, color=color)  # Swap x and y
    elif directions[i] == 2:  # down
        ax.arrow(cells[i][1], cells[i][0], 0, 0.5, head_width=0.1, color=color)  # Swap x and y
    elif directions[i] == 3:  # left
        ax.arrow(cells[i][1], cells[i][0], -0.5, 0, head_width=0.1, color=color)  # Swap x and y

# Create an animation
ani = animation.FuncAnimation(fig, update, frames=len(cells), interval=1000)

plt.show()