import math
import numpy


def is_prime_number(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return n > 1


def prime_numbers_generator(n):
    array = []
    amount = 0
    x = 0
    while amount < n:
        if is_prime_number(x):
            array.append(x)
            amount += 1
            print(x)
        x += 1
    return array


# Testing if the prime number generator is working correct
def test1():
    array = [2, 3]
    numpy.testing.assert_array_equal(prime_numbers_generator(2), array)


def test2():
    array = [2, 3, 5, 7, 11, 13, 18]
    numpy.testing.assert_array_equal(prime_numbers_generator(7), array)


if __name__ == "__main__":
    test1()
    test2()
