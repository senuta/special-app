print('Задача 6. Сумма факториалов')

# Напишите программу,
# которая запрашивает у пользователя число N
# и находит сумму факториалов 1! + 2! + 3! +... + N! 

N = int(input('Введите число: '))
fact = 1
summ = 0

for num in range(1, N + 1):
  fact *= num
  print('Факториал числа ', num, '= ', fact)
  summ += fact
print('Сумма факториалов числа', N, '= ', summ)