#!/usr/bin/env python3

def main():
    naturalNums = list(range(1, 101))

    sumSquare = 0
    squareSum = 0
    for num in naturalNums:
        sumSquare += num
        squareSum += num**2

    print(f'osszeg negyzete: {sumSquare**2} \n negyzet osszege: {squareSum} ')
    print(f'ketto kozotti kulonbseg: {sumSquare**2 - squareSum}')


if __name__ == '__main__':
    main()
