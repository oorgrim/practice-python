def multiplication(a, b=None):
    res = a * b
    return res
a = map(multiplication, [1, 2, 3], [3, 4, 5])
print(list(a))