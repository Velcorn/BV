# -*- coding: utf-8 -*-


def rotate(index):
    l1 = list(range(1, 10))
    l2 = l1[:index]
    l3 = l1[index + 1:]
    return l2[::-1] + [l1[index]] + l3[::-1]


def scrabble(string):
    werte = {"a": 1, "b": 3, "c": 4, "d": 1, "e": 1, "f": 4, "g": 2, "h": 2, "i": 1, "j": 6, "k": 4, "l": 2, "m": 3,
             "n": 1, "o": 2, "p": 4, "q": 10, "r": 1, "s": 1, "t": 1, "u": 1, "v": 6, "w": 3, "x": 8, "y": 10, "z": 3,
             "ä": 6, "ö": 8, "ü": 6}

    val = 0
    for c in string:
        if c in werte:
            val += werte[c]
        else:
            return "Only lowercase chars!"
    return val


def list_info():
    l1 = []
    while len(l1) < 5:
        user_input = input('Enter a number: ')
        try:
            float(user_input)
            l1.append(user_input)
        except ValueError:
            print("Not a number!")

    print(l1)
    print("Min: " + min(l1))
    print("Max: " + max(l1))
    print("Median: " + sorted(l1)[int(len(l1) / 2)])
    print("Different: " + str(len(set(l1))))

    z = 0
    for i in l1:
        if float(i).is_integer():
            z += 1
    print("Z: " + str(z))
    return "R w/o Z: " + str(len(l1) - z)


# print(rotate(2))
# print(scrabble("informatikum"))
print(list_info())
