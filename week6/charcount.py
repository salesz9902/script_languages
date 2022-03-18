#!/usr/bin/env python3

def charcount(text):
    d = {}
    d['whitespace'] = 0
    d['others'] = 0

    for num in range(97, 122+1):
        d[chr(num)] = 0

    for w in text:
        if w == ' ':
            d['whitespace'] += 1
        elif w in d:
            d[w] += 1
        else:
            d['others'] += 1

    return d


def main():
    print(charcount('cat and dog'))


if __name__ == '__main__':
    main()
