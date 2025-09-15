from generate import generate_random_points
from time import time
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt
from convex_hull import compute_hull

points_v_time = defaultdict(list)

for n in [10, 100, 1000, 10000, 100000, 500000, 1000000]:
    for _ in range(5):
        points = generate_random_points('normal', n)
        # plot_points(points)
        start = time()
        hull_points = compute_hull(points)
        end = time()
        points_v_time[n].append(round(end - start, 4))
        # draw_hull(hull_points)
        # title(f'{n} Normal Distribution points: {round(end - start, 4)} seconds')
        # show_plot()

print(f'raw: {points_v_time}')
print()

mean_time = defaultdict(int)
for key, value in points_v_time.items():
    mean_time[key] = np.mean(value)

print(f'mean: {mean_time}')

x = list(mean_time.keys())

bar_width = 0.2
n = np.arange(len(x))
plt.figure(figsize=(10, 6))
plt.scatter(n, list(mean_time.values()), color='blue', s=100)
k = 1/2
c = 1
y = k * n * np.log(n + c)
plt.plot(n, y, label=r'$n \log n$', color='red')

t = .15 * n ** 2
plt.plot(n, t, label=r'$n \log n$', color='green')

plt.title('n v time', fontsize = 20)
plt.xlabel('n', fontsize = 15)
plt.ylabel('mean time (seconds)', fontsize = 15)
plt.xticks([r for r in range(len(x))], x, fontsize=8)
plt.show()

"""
5. The relation of the empirical plot to the O(nlogn) theoretical complexity, is about 1/2 (constant 
of proportionality). However, the line formed by n^2 with a constant of proportionality 0.15 may fit 
the empirical data better. 
"""
