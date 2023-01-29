
number = int(input('введите число: '))
total = 0
while number > 0:
    x = number % 10
    total = total + x
    number = number // 10
print(total)
