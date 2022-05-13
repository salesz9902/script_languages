#!/usr/bin/env python3

def main():
    f = open('employees.txt')
    lines = f.readlines()

    l = ''
    sum = 0
    for line in lines:
        l = line.split(';')
        sum += int(l[2])

    f.close()
    print(sum/len(lines))


if __name__ == '__main__':
    main()
