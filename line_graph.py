import matplotlib.pyplot as plt

# Data for the revenue for each month in the quarter
months = ['January', 'February', 'March']
revenue = [5000, 6000, 5500]  # Replace with your actual revenue data

# Create a bar graph
plt.bar(months, revenue, color='royalblue')

# Add labels and title
plt.xlabel('Month')
plt.ylabel('Revenue ($)')
plt.title('Quarterly Revenue')

# Display the graph
plt.tight_layout()
plt.show()

