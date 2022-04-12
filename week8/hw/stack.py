#!/usr/bin/env python3

class Stack:
    def __init__(self):
        self.data = []

    def append(self, val):
        self.data.append(val)

    def size(self):
        return len(self.data)

    def empty(self):
        # return not bool(self.data.size()))
        return self.size() == 0

    def remove(self):
        if self.empty():
            return None
        else:
            return(self.data.pop())


class MyQueue:
    s1 = Stack()
    s2 = Stack()

    def append(self, val):
        self.s1.append(val)

    def popleft(self):
        i = len(self.s1.data)-1
        while i >= 0:
            self.s2.append(self.s1.data[i])
            i -= 1

        self.s1.data = []
        self.s2.data.pop()

        i = len(self.s1.data)-1
        while i > 0:
            self.s1.append(self.s2.data[i])
            i -= 1

        for n in self.s2.data:
            self.s1.append(n)

        return self.s1.data

    def is_empty(self):
        return self.s1.empty()

    def size(self):
        return self.s1.size()

    def __str__(self):
        return f'q[{self.s1.data}]'


def main():
    queue = MyQueue()
    queue.append(5)
    queue.append(8)
    queue.append(13)
    print('queue output: ', queue)
    print('queue size: ', queue.size())
    print('after popleft: ', queue.popleft())
    print('is empty: ', queue.is_empty())


if __name__ == '__main__':
    main()
