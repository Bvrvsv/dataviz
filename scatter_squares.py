import matplotlib.pyplot as plt

# Generate data
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

# Create scatter plot
plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
scatter = ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
ax.set_title('Square Numbers Scatter Plot', fontsize=16)    
ax.axis([0, 1_000, 0, 1_100_000])
ax.ticklabel_format(axis='y', style='plain')
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of Value', fontsize=14)

plt.show()
