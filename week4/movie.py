#!/usr/bin/env python3

def get_movie_info():
    # connect to a db
    # return a record/tuple
    return('Total Recall', 1990, 7.5)


def main():
    t = get_movie_info()
    print(t)

    title = t[0]
    year = t[1]
    point = t[2]

    print(title, year, point)

    ti, ye, po = get_movie_info()
    print(ti, ye, po)


if __name__ == '__main__':
    main()
