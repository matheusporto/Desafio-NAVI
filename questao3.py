# Questão 3

import math

dict = {}
n_students = 5

for i in range(n_students):
    print('Nome do aluno', i+1, ':')
    name = input()

    print('Nota do aluno', i+1, ':')
    grade = float(input())

    dict[name] = grade

for student, grade in dict.items():
    if grade == max(dict.values()):
        print('O aluno com maior nota é', student, 'cuja nota é', grade)