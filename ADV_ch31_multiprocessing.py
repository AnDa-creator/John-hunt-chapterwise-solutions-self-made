from multiprocessing import Pool
from timeit import default_timer


def factorial(num):
    if num == 1:
        return num
    else:
        return num * factorial(num - 1)


if __name__ == '__main__':
    start1 = default_timer()
    with Pool(processes = 8) as pool:
        results = pool.map(factorial, [i for i in range(700, 900)])
    # print(results)
    end1 = default_timer()
    print("time taken: ", end1 - start1, "seconds")
    start2 = default_timer()
    for i in range(700, 900):
        results.append(factorial(i))
    # print(results)
    end2 = default_timer()
    print("time taken: ", end2 - start2, "seconds")
    print('5:', factorial(5), ', 7:', factorial(7) )