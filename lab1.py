from math import sqrt


def sum_primes(array):
    if len(array) == 0:
        return "None"
    x = sum(list(filter(lambda num: is_prime(num), array)))
    if x > 0:
        return x
    else:
        return "None"


def is_prime(num):
    if num <= 0 or num == 1:
        return False
    if num % 2 == 0 and num > 2:
        return False
    return all(num % i for i in range(3, int(sqrt(num)) + 1, 2))


if __name__ == "__main__":
    print("Enter a list of numbers: ", end=" ")
    num_array = list(map(int, input().split()))
    print("Sum of all prime numbers in array is {}".format(sum_primes(num_array)))

