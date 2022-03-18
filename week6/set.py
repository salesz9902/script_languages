#!/usr/bin/env python3


def main():
    kosar = ['alma', 'ananasz', 'banan', 'alma', 'narancs', 'banan']
    gyumolcs = set(kosar)
    print(gyumolcs)
    print(type(gyumolcs))
    vissza = list(gyumolcs)
    print(vissza)


if __name__ == '__main__':
    main()
