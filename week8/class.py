#!/usr/bin/env python3

class MyClass:
    def hello(self):
        return "Hello World!"


def main():
    is_ok = True
    obj = MyClass()
    print(obj.hello())


if __name__ == '__main__':
    main()
