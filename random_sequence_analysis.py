import math
import numpy as np

#Реализуем функцию генератора псевдослучайных чисел с использованием указанной #формулы:
def middle_square_generator(seed, n, k): 
    sequence = [seed] 
    for i in range(n - 1): 
        val = sequence[-1] ** 2 
        fractional, _ = math.modf(val * 10 ** (k // 2)) 
        next_val = int(fractional * 10 ** k) * 10 ** (-k) 
        sequence.append(next_val) 
    return sequence
    
#Вычисляем период и отрезок апериодичности последовательности:
def compute_period(sequence): 
    n = len(sequence) 
    for period in range(1, n): 
        if sequence[-1] == sequence[-1 - period]: 
            return period 
    return n 
 
def compute_aperiodicity(sequence, period): 
    n = len(sequence) 
    for aperiodic in range(n - 2 * period): 
        if sequence[aperiodic:aperiodic + period] == sequence[aperiodic + period:aperiodic + 2 * period]: 
            return aperiodic + period - 1
    return n

#Проверяем гипотезу о равномерности распределения случайной последовательности с #помощью критерия хи-квадрат:
def chi_square_test(sequence, num_bins): 
    n = len(sequence) 
    bin_counts, _ = np.histogram(sequence, bins=np.linspace(0, 1, num_bins + 1)) 
    expected_count = n / num_bins 
    chi_square_stat = np.sum((bin_counts - expected_count) ** 2 / expected_count) 
    return chi_square_stat

seed = 0.15
n = 5000 
k = 2
num_bins = 13 
 
sequence = middle_square_generator(seed, n, k) 
period = compute_period(sequence) 
aperiodicity = compute_aperiodicity(sequence, period) 
chi_square_stat = chi_square_test(sequence, num_bins) 

if period == n: period = 1

print(sequence) 
print(period) 
print(aperiodicity) 
print(chi_square_stat)