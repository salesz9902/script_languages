#!/usr/bin/env python3

def loop(num, debug=False):
    """A function which creates a list of number until the first arg. In debug mode it prints out the start and the end of the for loop."""
    if(debug == False):
        for num in range(1, num+1):
            print(num, end=' ')
    else:
        print('\n# ciklus kezdete:')
        for num in range(1, num+1):
            print(num, end=' ')
        print('\n# ciklus vége')


def main():
    loop(5)
    loop(5, debug=True)


if __name__ == '__main__':
    main()
