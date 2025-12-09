import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.set_facecolor('#f0f0f0')
ax.grid(True, linestyle='--', color='gray', alpha=0.7)  
ax.scatter(input_values, squares, s=100, c='r', marker='^', label='Data Points')
ax.plot(input_values, squares, marker='o', linestyle='--', color='b', label='Squares')
ax.set_title('Square Numbers', fontsize=14)
ax.set_xlabel('Value', fontsize=12)
ax.set_ylabel('Square of Value', fontsize=12)
ax.tick_params(axis='both', labelsize=10)
ax.legend()

plt.show()
