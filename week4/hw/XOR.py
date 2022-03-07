#!/usr/bin/env python3


def main():
    str1 = 'python'
    str2 = None

    if(bool(str1) and not bool(str2)):
        print(True)
    elif(not bool(str1) and bool(str2)):
        print(True)
    else:
        print(False)


if __name__ == '__main__':
    main()
