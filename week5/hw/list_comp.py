#!/usr/bin/env python3

def main():
    """15 tasks solved with list comprehensions."""
    # task1
    print('task1')
    task1 = ['auto', 'villamos', 'metro']
    task1sol = [elem.upper()+'!' for elem in task1]
    print(task1sol)

    # task2
    print('task2')
    task2 = ['aladar', 'bela', 'cecil']
    task2sol = [name.capitalize() for name in task2]
    print(task2sol)

    # task3
    print('task3')
    task3sol = [0 for task3sol in range(10)]
    print(task3sol)

    # task4
    print('task4')
    task4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    task4sol = [elem*2 for elem in task4]
    print(task4sol)

    # task5
    print('task5')
    task5 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    task5sol = [int(elem) for elem in task5]
    print(task5sol)

    # task6
    print('task6')
    task6 = '1234567'
    task6sol = [int(c) for c in task6]
    print(task6sol)

    # task7
    print('task7')
    task7 = 'The quick brown fox jumps over the lazy dog'
    words = task7.split()
    task7sol = [len(word) for word in words]
    print(task7sol)

    # task8
    print('task8')
    task8 = 'python is an awesome language'
    words = task8.split()
    task8sol = [word[0] for word in words]
    print(task8sol)

    # task9
    print('task9')
    task9 = 'The quick brown fox jumps over the lazy dog'
    words = task9.split()
    task9sol = [(word, len(word)) for word in words]
    print(task9sol)

    # task10
    print('task10')
    task10 = range(10)
    task10sol = [elem for elem in task10 if(elem % 2 == 0)]
    print(task10sol)

    # task11
    print('task11')
    task11 = range(0, 20)
    task11sol = [num*num for num in task11 if(num % 2 == 0)]
    print(task11sol)

    # task12
    print('task12')
    task12 = range(0, 20)
    task12sol = [num*num for num in task12 if(str(num*num)[-1] == '4')]
    print(task12sol)

    # task13
    print('task13')
    task13 = range(65, 90+1)
    task13sol = ''.join([chr(num) for num in task13])
    print(task13sol)

    # task14
    print('task14')
    task14 = [' apple ', ' banana ', ' kiwi ']
    task14sol = [w.strip() for w in task14]
    print(task14sol)

    # task15
    print('task15')
    task15 = [1, 0, 1, 1, 0, 1, 0, 0]
    task15sol = ''.join([str(n) for n in task15])
    print(task15sol)


if __name__ == '__main__':
    main()
