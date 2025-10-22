def test_example(a: int, b: int) -> str:
    x = a + b
    return f'Сумма {a} + {b} = {x}'


test_example(1, 3)
print(test_example(1, 3))
