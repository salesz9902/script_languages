#!/usr/bin/env python3

def valid(text, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
    """Compare the two args and output the common characters."""
    same = ''
    for c in text:
        if(chars.find(c) != -1):
            same += chars[chars.find(c)]
    print(f'"{text}" \t-> "{same}"')


def main():
    valid("Barking!")
    valid("KL754", "0123456789")
    valid("BEAN", "abcdefghijklmnopqrstuvwxyz")


if __name__ == '__main__':
    main()
