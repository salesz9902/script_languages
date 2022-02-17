#!/usr/bin/env python3

def isPalindrom(word):
    if(word == word[::-1]):
        return True
    else:
        return False


def main():
    print(isPalindrom('görög'))
    print(isPalindrom('kacsa'))
    print(isPalindrom('kék'))


if __name__ == '__main__':
    main()
