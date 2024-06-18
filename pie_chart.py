import matplotlib.pyplot as plt

# Define the budget categories and their corresponding spending amounts
categories = ['Housing', 'Transportation', 'Food', 'Entertainment', 'Utilities']
spending = [1500, 800, 600, 200, 300]

# Calculate the total spending
total_spending = sum(spending)

# Calculate the percentage of spending for each category
percentages = [(x / total_spending) * 100 for x in spending]

# Create a pie chart
plt.figure(figsize=(6, 6))  # Adjust the figure size if needed
plt.pie(percentages, labels=categories, autopct='%1.1f%%', startangle=140, colors=['royalblue', 'lightcoral', 'gold', 'lightgreen'])
plt.title('Budget Allocation by Category', y=1.04)  # Adjust the 'y' parameter to raise the title
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Display the pie chart
plt.show()
