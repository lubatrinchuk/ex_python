# Задание 1
import numpy as np
from sklearn import preprocessing

# 1. Создайте вектор с элементами от 12 до 42

a = np.arange(12, 43)

# 2. Создайте вектор из нулей длины 12, но его пятый елемент должен быть равен 1

b = np.zeros(12, dtype = int)
b[4] = 1

# 3. Создайте матрицу (3, 3), заполненую от 0 до 8

v = np.arange(0, 9)
c = v.reshape((3, 3))

# 4. Найдите все положительные числа в np.array([1,2,0,0,4,0])

d = np.array([1,2,0,0,4,0])
d = d[d>0]

# 5. Умножьте матрицу размерности (5, 3) на (3, 2)

e = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]])
f = np.array([[1,2],[2,3],[4,5]])
g = np.dot(e,f)

# 6. Создайте матрицу (10, 10) так, чтобы на границе были 0, а внтури 1

h = np.zeros((10, 10))
h[1:9, 1:9] = 1

# 7. Создайте рандомный вектор и отсортируйте его

j = np.random.randint(0, 100, 10)
k = np.sort(j)

# 8. Каков эквивалент функции enumerate для numpy массивов?

l = np.array([[1,2,3],[4,5,6],[7,8,9]])
for index, values in np.ndenumerate(l):
    print(index, values)

# 9. Создайте рандомный вектор и выполните нормализацию столбцов (из каждого столбца вычесть среднее этого столбца, поделить на sd этого столбца)

m = np.array([2,3,5,6,7,4,8,7,6])
normalized_m = preprocessing.normalize([m])

# 10. Для заданного числа найдите ближайший к нему элемент в векторе

def find(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin() #argmin дает индекс, abs - модуль
    return array[idx]

# 11. Найдите N наибольших значений в векторе

def find_n_max(array, n):
    sorted_index_array = np.argsort(array)
    sorted_array = array[sorted_index_array]
    n_max = sorted_array[-n:]
    return n_max

