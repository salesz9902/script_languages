#!/usr/bin/env python3

def iterativ(text):
    i = len(text)-1
    new = ''
    while(i != -1):
        new += text[i]
        i -= 1
    if(new == text):
        return True
    else:
        return False


def main():
    num = 2002
    text = 'görög'

    print(f'{num} is palindrom' if iterativ(
        str(num)) else f'{num} is not palindrom')
    print(f'{text} is palindrom' if iterativ(
        text) else f'{num} is not palindrom')


if __name__ == '__main__':
    main()
