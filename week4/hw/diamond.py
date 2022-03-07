#!/usr/bin/env python3

def makeDiamond(height):
    i = 1
    if(height % 2 == 0):
        print('The height of the diamond should be an odd number')
    else:
        while(i <= height):
            print(('*'*i).center(height))
            i += 2

        i = height-2

        while(i >= 0):
            print(('*'*i).center(height))
            i -= 2


def main():
    print('Would you like to get a diamond?')
    height = input('Please give me the height of it: ')
    makeDiamond(int(height))


if __name__ == '__main__':
    main()
