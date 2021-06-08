from math import sqrt
from timeit import default_timer

def prime_number_generator(number):
    for num in range(3, number):
        is_prime = True
        for i in range(2, int(sqrt(num) + 1)):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            yield num


if __name__ == "__main__":
    number = input('Please input the number:')
    start = default_timer()
    if number.isnumeric():
        num = int(number)
        if num <= 2:
            print('Number must be greater than 2')
        else:
            for prime in prime_number_generator(num):
                print(prime, end=', ')
    else:
        print('Must be a positive integer')
    end = default_timer()
    print()
    print("total time: ",  end - start, "seconds")