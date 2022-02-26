#!/usr/bin/env python3

def iterativ(text):
    i = len(text)-1
    new = ''
    while(i != -1):
        new += text[i]
        i -= 1
    return new


def main():
    num = 2002
    text = 'görög'

    print(iterativ(str(num)))
    print(iterativ(text))


if __name__ == '__main__':
    main()
