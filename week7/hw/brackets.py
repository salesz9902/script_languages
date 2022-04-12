#!/usr/bin/env python3

OPEN = ["[", "{", "("]
CLOSE = ["]", "}", ")"]


def test(text):
    stack = []
    for i in text:
        if i in OPEN:
            stack.append(i)
        elif i in CLOSE:
            pos = CLOSE.index(i)
            if ((len(stack) > 0) and
                    (OPEN[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False


def main():
    print('test("((5+3)*2+1)") == True ->', test("((5+3)*2+1)") == True)
    print('test("{[(3+1)+2]+}") == True ->', test("{[(3+1)+2]+}") == True)
    print('test("(3+{1-1)}") == False ->', test("(3+{1-1)}") == False)
    print('test("[1+1]+(2*2)-{3/3}") == True ->',
          test("[1+1]+(2*2)-{3/3}") == True)
    print('test("(({[(((1)-2)+3)-3]/3}-3)") == False ->',
          test("(({[(((1)-2)+3)-3]/3}-3)") == False)


if __name__ == '__main__':
    main()
