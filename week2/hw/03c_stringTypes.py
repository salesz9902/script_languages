#!/usr/bin/env python3

def main():
    html = '''
<html>
<body>
<h1>hello</h1>
</body>
</html>
'''.strip()

    s = 'py\nthon'
    length = len(s)

    raw = r'C:\Windows\valami'

    print("'" + html + "'")
    print(s, length)
    print(raw)


if __name__ == '__main__':
    main()
