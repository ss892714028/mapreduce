import random

data = []
for _ in range(2000000):
    data.append('https://github.com/ss892714028' + str(random.randint(1, 500)))

with open("data.txt", 'w') as f:
    f.write("\n".join(data))
