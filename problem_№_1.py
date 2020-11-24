def sum_chisel(x):
    s = 0
    for i in range(1, x):
        if i % 3 == 0 or i % 5 == 0:
            s += i
    return s


print(sum_chisel(1000))
