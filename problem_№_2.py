def fibonacci():
    x1 = 1
    x2 = 2
    s = 0
    while x1 < 4000000:
        x = x1 + x2
        x1 = x2
        x2 = x
        if x1 % 2 == 0:
            s += x1
    return f'Сумма всех чётных чисел Фибоначчи по задаче №2 = {s}'


print(fibonacci())
