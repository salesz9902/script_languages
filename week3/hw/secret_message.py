#!/usr/bin/env python3

TEXT = """
Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb
"""


def main():
    newTEXT = ''

    for char in TEXT:
        if(char.isupper()):
            if(ord(char) > 88):
                char = chr(ord(char)-26)
            char = chr(ord(char)+2)
        elif(char.islower()):
            if(ord(char) > 120):
                char = chr(ord(char)-26)
            char = chr(ord(char)+2)
        else:
            char = chr(ord(char))

        newTEXT += char

    print(newTEXT)


if __name__ == '__main__':
    main()
