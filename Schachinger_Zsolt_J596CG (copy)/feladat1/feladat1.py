#!/usr/bin/env python3
import json


def main():
    f = open('data.json')
    js = json.load(f)
    f.close()
    print('-> data.json beolvasva')

    li = []
    for key in js['data']:
        li = []
        for i in range(len(js['data'][key])):
            for d in js['data'][key][i]:
                li.append(d)
        js['data'][key] = li

    out = open('out.json', 'w')
    json.dump(js, out)
    out.close()
    print('-> out.json létrehozva')


if __name__ == '__main__':
    main()
