def test_example(a: int | float, b: int | float):
    x = a + b
    return f'Сумма целых чисел: {a} + {b} = {x}'


test_example(1, 3)
print(test_example(1, 3))
