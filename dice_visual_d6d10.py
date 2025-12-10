import plotly.express as px

from die import Die
import die

# Create a D6 and a D10 die instances
d6 = Die()
d10 = Die(10)

# Make some rolls and store the results in lists
results = []
for roll_num in range(50_000):
    result = d6.roll()+ d10.roll()
    results.append(result)  


# Analyze the results

frequencies = []
poss_results = range(2, d6.num_sides + d10.num_sides + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

Title = 'Results of rolling one D6 and one D10 50,000 times'

fig = px.bar(x=poss_results, y=frequencies, labels={'x': 'Result', 'y': 'Frequency'},
             title=Title)  
fig.show()