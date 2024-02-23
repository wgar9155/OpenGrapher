import mplcursors
import matplotlib.pyplot as plt
# Sample data
x = ['A', 'B', 'C']
y = [10, 20, 15]

# Create bar plot
plt.bar(x, y)

# Add labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Plot')
