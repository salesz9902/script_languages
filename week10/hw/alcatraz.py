#!/usr/bin/env python3

def changeState(dict, steps):
    for i in dict.keys():
        if i % steps == 0:
            if(dict[i] == 0):
                dict[i] = 1
            else:
                dict[i] = 0


def main():
    cells = {}

    # step 0: all closed
    for i in range(1, 601):
        cells[i] = 0

    for i in range(1, 601):
        changeState(cells, i)

    print('A nyitva maradt cellák listája:')
    for i in cells.keys():
        if cells[i] == 1:
            print(i, end=' ')


if __name__ == '__main__':
    main()
