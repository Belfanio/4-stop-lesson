import random
print ('введите размерность списков')
razm = int(input())
print ('введите начало диапазона случайных чисел')
start = int(input())
print ('введите конец диапазона случайных чисел')
finish = int(input())
Spis1 = [random.randint(start,finish) for i in range (0, razm)]
print ('Список = {}'.format(Spis1))
minimum = min(Spis1)
print ('минимальный элемент = {}'.format(minimum))
maximum = max(Spis1)
print ('максимальный элемент = {}'.format(maximum))

spis2 = []
for i in range(0, razm):
    a = 0 if i % 2 == 0 else 1
    spis2.append(a)
print ('Список2 = {}'.format(spis2))

spis3 = []
a=1
spis3.append(a)
for i in range(1, razm-1):
    a = 0
    spis3.append(a)
a=1    
spis3.append(a)
print ('Список3 = {}'.format(spis3))

spis4 = [i for i in Spis1 if Spis1.count(i) >= 2]
print ('Список повторяющихся элементов = {}'.format(spis4))