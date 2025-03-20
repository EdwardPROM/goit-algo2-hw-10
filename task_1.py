import random
import time
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return randomized_quick_sort(less) + equal + randomized_quick_sort(greater)

def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]  # останній елемент
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return deterministic_quick_sort(less) + equal + deterministic_quick_sort(greater)

# Генеруємо випадковиий масив
sizes = [10_000, 50_000, 100_000, 500_000]
test_arrays = {size: np.random.randint(0, 1_000_000, size).tolist() for size in sizes}

# Вимірювання часу виконання
def measure_execution_time(sort_function, arr, repetitions=5):
    times = []
    for _ in range(repetitions):
        copied_array = arr.copy()
        start_time = time.perf_counter()
        sort_function(copied_array)
        end_time = time.perf_counter()
        times.append(end_time - start_time)
    return sum(times) / repetitions

results = []

for size, arr in test_arrays.items():
    random_time = measure_execution_time(randomized_quick_sort, arr)
    deterministic_time = measure_execution_time(deterministic_quick_sort, arr)
    results.append({
        'Розмір масиву': size,
        'Рандомізований QuickSort': random_time,
        'Детермінований QuickSort': deterministic_time
    })

# Графік виведення   
df_results = pd.DataFrame(results)
print(df_results)

plt.figure(figsize=(8, 6))

plt.plot(df_results['Розмір масиву'], df_results['Рандомізований QuickSort'], label='Рандомізований QuickSort')
plt.plot(df_results['Розмір масиву'], df_results['Детермінований QuickSort'], label='Детермінований QuickSort')

plt.xlabel('Розмір масиву')
plt.ylabel('Середній час виконання (секунди)')
plt.title('Порівняння рандомізованого та детермінованого QuickSort')
plt.legend()
plt.grid(True)
plt.show()

# Результати
for index, row in df_results.iterrows():
    print(f"Розмір масиву: {row['Розмір масиву']}")
    print(f"   Рандомізований QuickSort: {row['Рандомізований QuickSort']:.4f} секунд")
    print(f"   Детермінований QuickSort: {row['Детермінований QuickSort']:.4f} секунд\n")
