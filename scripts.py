while True:
  lowerBorder = int(input('Нижняя граница: '))
  upperBorder = int(input('Верхняя граница: '))
  if lowerBorder > upperBorder:
    print('Нижняя граница не может быть больше верхней границы. \nУкажите корректные данные.')
  else:
    break

if lowerBorder == upperBorder:
  print('C', '\t', 'F')
  c = lowerBorder
  f = round(c * 1.8 + 32)
  print(c, '\t', f)
else:
  step = int(input('Шаг: '))
  print('C', '\t', 'F')
  for c in range(lowerBorder, upperBorder, step):
    f = round(c * 1.8 + 32)
    print(c, '\t', f)
  if c < upperBorder:
    print(upperBorder, '\t', round(upperBorder * 1.8 + 32))