#!/usr/bin/env python3

def checkhamming(w1, w2):
    hvalue = 0
    for c1, c2 in zip(w1, w2):
        if(not c1 == c2):
            hvalue += 1
    return hvalue
    # return sum([1 for c1, c2 in zip(s1,s2) if c1 != c2])


def main():
    print(checkhamming('toned', 'roses'))


if __name__ == '__main__':
    main()
