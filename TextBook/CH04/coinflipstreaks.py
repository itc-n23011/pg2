import random

number_of_streaks = 0

for experiment_number in range(10000):

    results = []
    N = 100
    for i in range(N):
        results.append(random.randint(0, 1))

    S = 6
    for i in range(N - S):
        s = sum(results[i:i+S])
        if s == 0 or s == S:
            number_of_streaks += 1
            break

print(f'同じ面が6連続で出現する確率: {number_of_streaks / 100}%')
