import string
from time import time


class Timer(object):
    def __init__(self, name):
        self.start = time() * 1000
        self.name = name

    def stop(self):
        td = int(time() * 1000  - self.start)
        print("{} took {}ms".format(self.name, td))


def bruteforce_generator(chars, min_length=3, max_length=20):
    n = min_length
    l = len(chars)
    while n <= max_length:
        indices = [0] * n
        for i in range(0, pow(l, n)):
            current = 0
            while True:
                if current >= n:
                    break
                indices[current] += 1
                if indices[current] == l:
                    indices[current] = 0
                    current += 1
                else:
                    break
            yield "".join([chars[idx] for idx in indices])
        n += 1


def load_passwordlist(path):
    with open(path, "r") as f:
        raw = f.readlines()

    return [l.strip() for l in raw if not l.startswith("#") and l.strip() != ""]


def find_passw1(passw, chars=string.printable):
    t = Timer("Finding n={}".format(len(passw)))
    found = False
    for i in bruteforce_generator(chars, min_length=3, max_length=len(passw)):
        if i == passw:
            print("Found: {}".format(i))
            found = True
            break

    t.stop()
    if not found:
        print("NOT FOUND")


def find_passw2(passw):
    t = Timer("Finding n={}".format(len(passw)))
    lst = list(load_passwordlist("password-list.txt"))
    found = False
    for i in lst:
        if i == passw:
            print("Found: {}".format(i))
            found = True
            break
    t.stop()
    if not found:
        print("NOT FOUND")


def mutate_passw(lst):
    popular_numbers = list(range(1, 99)) + list(range(1900, 2021))
    for l in lst:
        yield l
        yield l.lower()
        yield l[0].upper() + l[1:].lower()
        for n in popular_numbers:
            yield l + str(n)


def find_passw3(passw):
    t = Timer("Finding n={}".format(len(passw)))
    lst = list(load_passwordlist("password-list.txt"))
    found = False
    for i in mutate_passw(lst):
        if i == passw:
            print("Found: {}".format(i))
            found = True
            break

    t.stop()
    if not found:
        print("NOT FOUND")


