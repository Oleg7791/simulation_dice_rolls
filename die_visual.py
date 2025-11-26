from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# создание кубика
die = Die()

# моделирование серии бросков
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)
# анализ результатов
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# визуализация результатов
x_values = list(range(1, die.num_sides + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': "Frequency of Result"}
my_laylout = Layout(title='Results of rolling one D6 1000 times',
                    xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_laylout}, filename='d6.html')
print(frequencies)
