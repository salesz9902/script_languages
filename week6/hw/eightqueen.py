#!/usr/bin/env python3

def maketable(queens):
    li = []
    d = {}

    print('+' + '-'*17 + '+')

    for i in range(8):
        li.append('.')

    for i in range(8):
        d[str(i)] = li

    for i, v in enumerate(d.values()):
        print('|', end=' ')
        for index, e in enumerate(v):
            if(index == queens[i]):
                print('Q', end=' ')
            else:
                print(e, end=' ')
        print('|')

    print('+' + '-'*17 + '+')


def main():
    rli = [7, 3, 0, 2, 5, 1, 6, 4]
    rli2 = [0, 4, 7, 5, 2, 6, 1, 3]
    maketable(rli)
    maketable(rli2)


if __name__ == '__main__':
    main()
