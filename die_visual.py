import plotly.express as px
from die import Die

# Create a Die instance with 6 sides

die = Die()

# Make some rolls and store the results in a list

results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

#Analyze the results
frequencies = []
poss_results = range(1, die.num_sides + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)


#print(frequencies)

#Visualize the results
fig = px.line(x=poss_results, y=frequencies, labels={'x': 'Result', 'y': 'Frequency'},
             title='Results of rolling one D6 1000 times')  
fig.show()