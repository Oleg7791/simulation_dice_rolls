from die import Die

# создание кубика
die = Die()

# моделирование серии бросков
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)

print(results)