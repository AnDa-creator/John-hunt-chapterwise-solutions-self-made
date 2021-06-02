from math import ceil


def check_choice(string):
    if string == 'double':
        return lambda y: y * 2
    elif string == 'triple':
        return lambda y: y * 3
    elif string == 'square_root':
        return lambda y: y ** 0.5
    elif string == 'is_prime':
        return lambda y: y % 2 == 0
    elif string == 'is_integer':
        return lambda y: isinstance(y, int)
    elif string == 'is_letter':
        return lambda y: isinstance(y, string)


def my_higher_order_function(i, func):
    func_now = check_choice(func)
    return func_now(i)


if __name__ == '__main__':
    print(my_higher_order_function(2, 'double'))
    print(my_higher_order_function(2, 'triple'))
    print(my_higher_order_function(16, 'square_root'))
    print(my_higher_order_function(2, 'is_prime'))
    print(my_higher_order_function(4, 'is_prime'))
    print(my_higher_order_function('2', 'is_integer'))
    print(my_higher_order_function('A', 'is_integer'))
    print(my_higher_order_function('A', 'is_letter'))
    print(my_higher_order_function('1', 'is_letter'))
