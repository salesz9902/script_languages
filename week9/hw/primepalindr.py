#!/usr/bin/env python3

def isPalindrom(word: int) -> bool:
    w: str = str(word)
    if(w == w[::-1]):
        return True
    else:
        return False


def isPrime(n: int) -> bool:
    """
    Decide whether a number is prime or not.
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    i = 3
    maxi: float = n**0.5 + 1
    while i <= maxi:
        if n % i == 0:
            return False
        i += 2

    return True


def test(number: int) -> int:
    while(True):
        if(isPalindrom(number) and isPrime(number)):
            return number
        number += 1


def main():
    print('test(31) == 101 ', test(31) == 101)
    print('test(130) == 131 ', test(130) == 131)
    print('test(131) == 131 ', test(131) == 131)
    print('test(1977) == 10301 ', test(1977) == 10301)


if __name__ == '__main__':
    main()
