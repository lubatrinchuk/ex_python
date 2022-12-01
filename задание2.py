#Задание 2
#Напишите полностью векторизованный вариант
#Дан трёхмерный массив, содержащий изображение, размера (height, width, numChannels), а также вектор длины numChannels.
#Сложить каналы изображения с указанными весами, и вернуть результат в виде матрицы размера (height, width).
#Считать реальное изображение можно при помощи функции scipy.misc.imread (если изображение не в формате png,
#установите пакет pillow: conda install pillow). Преобразуйте цветное изображение в оттенки серого,
#использовав коэффициенты np.array([0.299, 0.587, 0.114]).
from PIL import Image
import numpy as np

gray = np.array([0.299, 0.587, 0.114])

img = Image.open('z.jpg')

numpydata = np.asarray(img)
gray_img = numpydata.dot(gray)

print(gray_img)

pilImage = Image.fromarray(gray_img)
pilImage.show()



