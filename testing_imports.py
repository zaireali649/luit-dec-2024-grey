# Import local hello_world scripts
import hello_world

# Import random for generating random numbers
import random  

# Generate a random number between 1 and 100
print("Random number between 1 and 100:", random.randint(1, 100))


# Import math for mathematical operations
import math  

# Calculate the square root of 16
print("Square root of 16:", math.sqrt(16))


# Import os to interact with the operating system
import os  

# Print the current working directory
print("Current working directory:", os.getcwd())


# Import matplotlib for creating plots
import matplotlib.pyplot as plt  

# Create a simple line plot
x = [1, 2, 3, 4, 5]  # X-axis values
y = [1, 4, 9, 16, 25]  # Y-axis values (squares)

plt.plot(x, y, marker='o')  # Plot x vs y with circular markers
plt.title("Simple Line Plot")  # Add a title
plt.xlabel("X Values")  # Label the X-axis
plt.ylabel("Y Values (Squared)")  # Label the Y-axis
plt.show()  # Display the plot
