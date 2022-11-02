# Home Work Solutions 3

"""
Write a function some_sum with the following behavior:

# def some_sum

some_summ(1) #-> 1
some_summ(1) + some_summ(1) #-> 2

some_summ(1, 2, 3) #-> 6

some_summ(1)(2) #-> 3

some_summ(1)(2)(1, 2, 3) #-> 9

some_summ(1)(2)(1, 2, 3) + some_summ(1)(2) #-> 12

some_summ(1)(2)(1, 2, 3)(1) #-> 10

some_summ(1)()() #-> 1
some_summ(1)()(1) * some_summ(1)(2)() #-> 4
"""


class MyClass(int):
    def __call__(self, *argv):
        return some_sum(self, *argv)


def some_sum(*args):
    res = sum(args)
    return MyClass(res)


if __name__ == '__main__':
    assert some_sum(1) == 1
    assert some_sum(1) + some_sum(1) == 2
    assert some_sum(1, 2, 3) == 6
    assert some_sum(1)(2) == 3
    assert some_sum(1)(2)(1, 2, 3) == 9
    assert some_sum(1)(2)(1, 2, 3) + some_sum(1)(2) == 12
    assert some_sum(1)(2)(1, 2, 3)(1) == 10
    assert some_sum(1)()() == 1
    assert some_sum(1)()(1) * some_sum(1)(2)() == 4  # Ошибка в условии. Результат должен быть 2 + 3 == 6, а не 4.
