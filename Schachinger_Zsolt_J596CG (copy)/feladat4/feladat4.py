#!/usr/bin/env python3
import sys


def main():
    if(len(sys.argv) < 2):
        pass
    if(len(sys.argv) > 1):
        word = list(sys.argv[1])
        print(''.join(word))
        for i, d in enumerate(sys.argv):
            if(d.isdigit() and sys.argv[i-1] in word):
                times = int(d)
                where = word.index(sys.argv[i-1])
                if times != 0:
                    for index in range(times):
                        word.insert(where, sys.argv[i-1])
                    word = list(word)
                print(''.join(word))


if __name__ == '__main__':
    main()
