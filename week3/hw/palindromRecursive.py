#!/usr/bin/env python3

def recursive(text):
    if len(text) < 1:
        return True
    else:
        if(text[0] == text[-1]):
            return recursive(text[1:-1])
        else:
            return False


def main():
    num = 2002
    text = 'görög'

    print(f'{num} is palindrom' if recursive(
        str(num)) else f'{num} is not palindrom')
    print(f'{text} is palindrom' if recursive(
        text) else f'{num} is not palindrom')


if __name__ == '__main__':
    main()
