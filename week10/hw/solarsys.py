#!/usr/bin/env python3

def main():
    f = open('DT2.csv')

    for line in f:
        try:
            if line.index('j') < line.index('s') < line.index('u') < line.index('n'):
                print(line)
        except:
            pass


if __name__ == '__main__':
    main()
