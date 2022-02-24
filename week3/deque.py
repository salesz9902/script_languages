#!/usr/bin/env python3

from collections import deque


def main():
    q = deque([3, 4, 5])
    print(q)
    q.append(6)
    q.append(7)
    print(q)

    q.popleft()

    print(q)


if __name__ == '__main__':
    main()
