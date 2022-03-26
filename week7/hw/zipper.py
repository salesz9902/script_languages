#!/usr/bin/env python3

def main():
    # chars = "abcdefghijklmnopqrstuvwxyz"
    codes = list(range(ord('a'), ord('z')+1))

    for t in codes:
        print(f"('{chr(t)}', {t})")


if __name__ == '__main__':
    main()
