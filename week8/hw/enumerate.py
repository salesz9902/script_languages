#!/usr/bin/env python3
from enum import Enum

DEEP_TONE = 'aáoóuú'
HIGH_TONE = 'eéiíöőüű'

class Tones(Enum):
    DEEP = 1
    HIGH = 2
    MIXED = 3
    NONE = 4

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
            return Tones.MIXED.name
        elif(deep > 0 and high == 0):
            return Tones.DEEP.name
        elif(deep == 0 and high != 0):
            return Tones.HIGH.name
        else:
            return Tones.NONE.name


def main():
    words = ["ablak", "erkély", "kisvasút", "magas", "mély", "pffff"]
    for w in words:
        print("{}: This word is {} toned!".format(w, Tones.deep_or_high(w)))


if __name__ == '__main__':
    main()
