#!/usr/bin/env python3

DEEP_TONE = 'aáoóuú'
HIGH_TONE = 'eéiíöőüű'


def deep_or_high(word):
    w = list(word)
    deep = 0
    high = 0
    for c in w:
        if(DEEP_TONE.find(c) != -1):
            deep += 1
        if(HIGH_TONE.find(c) != -1):
            high += 1
    if(deep > 0 and high > 0):
        print(f'{word} -> vegyes')
    elif(deep > 0 and high == 0):
        print(f'{word} -> mély')
    elif(deep == 0 and high != 0):
        print(f'{word} -> magas')
    else:
        print(f'{word} -> semmilyen')


def main():
    words = ['ablak', 'erkély', 'kisvasút', 'magas', 'mély', 'pffff']
    for word in words:
        deep_or_high(word)


if __name__ == '__main__':
    main()
