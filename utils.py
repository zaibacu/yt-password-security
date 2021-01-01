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


def find_passw(passw, chars=string.printable):
    t = Timer("Finding n={}".format(len(passw)))
    for i in bruteforce_generator(chars, min_length=3, max_length=len(passw)):
        if i == passw:
            print("Found: {}".format(i))
            break

    t.stop()
