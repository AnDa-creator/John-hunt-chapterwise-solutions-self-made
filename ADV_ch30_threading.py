from threading import Thread
from time import sleep
from random import randint


def printer(msg=None, max_period=0):
    for i in range(10):
        sleep_period = randint(0, max_period)
        sleep(sleep_period)
        print(msg, "-- slept for --", sleep_period)


if __name__ == '__main__':
    t1 = Thread(target=printer, args=('A', 10))
    t2 = Thread(target=printer, args=('B', 5))
    t3 = Thread(target=printer, args=('C', 15))
    t4 = Thread(target=printer, args=('D', 7))
    t5 = Thread(target=printer, args=('E', 2))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
