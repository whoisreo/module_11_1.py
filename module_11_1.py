import numpy as np


a = np.random.randint(0, 100, size=(9, 9))

a_sum = np.sum(a)
a_mean = np.mean(a)
a_f = np.array(a[a > 50])


print(f'Массив:\n{a}')
print(f'Сумма элементов: {a_sum}')
print(f'Среднее значение: {a_mean}')
print(f"Фильтрация. Числа больше 50:\n{a_f}")
