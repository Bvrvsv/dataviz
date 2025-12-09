import matplotlib.pyplot as plt

from random_walk import RandomWalk  
while True:
    # Create a random walk instance and fill it with points
    rw = RandomWalk(num_points=5000)
    rw.fill_walk()

    # Plot the random walk
    plt.style.use('classic')
    fig, ax = plt.subplots()
    points_number = list(range(rw.num_points))
    ax.scatter(rw.x_values, rw.y_values, c=points_number, cmap=plt.cm.Blues,
        edgecolors='none',s=15)
    ax.plot(rw.x_values, rw.y_values, linewidth=1)
    ax.set_title("Random Walk", fontsize=16)
    ax.set_xlabel("X Values", fontsize=14)
    ax.set_ylabel("Y Values", fontsize=14)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running.lower() == 'n':
        break