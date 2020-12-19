# Questão 1

count = 0
for i in range(1, 5000000):
    if (i % 2 == 0) and (i % 37 == 0) and (i % 49 == 0):
        count += 1

print(count, 'é a quantidade de números que atende às restrições')