def f(s, m):
    ns = [i * m for i in s]
    return ns


def f_lambda(s, m):
    return list(map(lambda i: i * m, s))


m = 2
s = [int(x) for x in input("Введите список чисел через пробел: ").split()]
m_str = input("Введите множитель (по умолчанию 2): ")
if m_str:
    m = int(m_str)
print("Результат (функция):", f(s, m))
print("Результат (лямбда-функция):", f_lambda(s, m))
