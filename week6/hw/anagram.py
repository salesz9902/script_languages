#!/usr/bin/env python3

def normalize(text):
    return text.lower().replace(' ', '')


def isAnagram(text1, text2):
    if(len(normalize(text1)) != len(normalize(text2))):
        return False
    li = li2 = []
    for c in normalize(text1):
        li.append(c)
    for c in normalize(text2):
        li2.append(c)

    return sorted(li) == sorted(li2)


def isAnagramV2(t1, t2):
    if(len(normalize(t1)) != len(normalize(t2))):
        return False
    for i, c in enumerate(sorted(normalize(t1))):
        if(sorted(normalize(t2))[i] != c):
            return False
    return True


def main():
    rt = 'Random Text'
    rt2 = 'Another rAnDomT Ext'
    r = 'listen'
    r2 = 'silent'
    r3 = 'Clint Eastwood'
    r4 = 'Old west action'
    li = []
    li2 = []
    print(f'{r} -> {r2} - {isAnagram(r, r2)}')
    print(f'{rt} -> {rt2} - {isAnagram(rt, rt2)}')
    print(f'{r3} -> {r4} - {isAnagram(r3, r4)}')

    print(f'{r} -> {r2} - {isAnagramV2(r, r2)}')
    print(f'{rt} -> {rt2} - {isAnagramV2(rt, rt2)}')
    print(f'{r3} -> {r4} - {isAnagramV2(r3, r4)}')


if __name__ == '__main__':
    main()
