#!/usr/bin/env python3
from typing import List


def listPages(pagesToPrint: str) -> List[int]:
    pages: List[str] = pagesToPrint.split(',')
    newPages: List[int] = []
    for page in pages:
        if (page.find('-') != -1):
            fr: int = page.find('-')
            for i in range(int(page[:fr]), int(page[fr+1:])+1):
                newPages.append(i)
        else:
            newPages.append(int(page))

    return newPages


def main():
    print('Pages to print (e.g. 1-5,7,9):')
    pages: str = input()
    print('Printing: ', listPages(pages))


if __name__ == '__main__':
    main()
