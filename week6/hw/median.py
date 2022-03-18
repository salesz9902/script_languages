#!/usr/bin/env python3
import math


def median(nums):
    """Returns the median of a list."""
    half = len(nums)/2-1
    nums.sort()
    if(len(nums) % 2 == 0):
        half = math.ceil(half)
        return (nums[half]+nums[half+1])/2
    return nums[math.ceil(half)]


def main():
    print(median([1, 2, 3, 4, 5]))
    print(median([3, 1, 2, 5, 3]))
    print(median([1, 300, 2, 200, 1]))
    print(median([3, 6, 20, 99, 10, 15]))


if __name__ == '__main__':
    main()
