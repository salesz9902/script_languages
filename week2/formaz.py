#!/usr/bin/env python3

def hello(name, color, obj):
    # geza, kek az eg!
    # v0, C:
    # printf("%s, %s az %s!\n", name, color, obj);
    # v1
    #print('{0}, {1} az {2}! Ki? {0}'.format(name, color, obj))
    # v2
    #print('{}, {} az {}!'.format(name, color, obj))
    # v3
    #print('{n}, {c} az {o}!'.format(n=name, c=color, o=obj))
    # v4
    #print(f'1 + 1 = {1+1}')
    print(f'{name.capitalize()}, {color} az {obj}!')


def main():
    hello('géza', 'kék', 'ég')
    print('-' * 20)
    hello('julcsi', 'piros', 'autó')


if __name__ == '__main__':
    main()
