#!/usr/bin/env python3

def recursive(text):
    if len(text) < 1:
        return True
    else:
        if(text[0] == text[-1]):
            return recursive(text[1:-1])
        else:
            return False


def main():
    num = 2002
    text = 'görög'

    print(recursive(str(num)))
    print(recursive(text))


if __name__ == '__main__':
    main()
