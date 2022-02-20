#!/usr/bin/env python3

def main():
    print('{0:<12} {1:^16} {2:16}'.format('Name', 'Age', 'City'))
    print('-'*40)
    print('{0:12} {1:^16} {2:16}'.format('Kiss Janos', '40', 'Budapest'))
    print('{0:12} {1:^16} {2:16}'.format('Kiss Erno', '36', 'Debrecen'))
    print('{0:12} {1:^16} {2:16}'.format('Kiss Attila', '28', 'Szeged'))
    print('{0:12} {1:^16} {2:16}'.format('Pelda Pista', '20', 'Miskolc'))


if __name__ == '__main__':
    main()
