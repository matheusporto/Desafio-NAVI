# Questão 2

import math as m
import statistics as stat

array = []

for i in range(10):
    if i % 2 == 0:
        array.append(pow(i, 3) + 7 * (m.factorial(i)))
    else:
        array.append(pow(2, i) + 4 * (m.log(i)))

mean = round(stat.mean(array), 2)
position = array.index(max(array))

print('A posição do maior elemento é', position, 'e a média dos elementos do vetor é', mean)