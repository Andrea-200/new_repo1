import matplotlib.pyplot as plt

# Data for plotting
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Create a new figure
plt.figure()

# Plot data
plt.plot(x, y, label='y = x^2')

# Add title and labels
plt.title('Simple Plot')
plt.xlabel('x-axis')
plt.ylabel('y-axis')

# Add a legend
plt.legend()

# Show the plot
plt.show()
