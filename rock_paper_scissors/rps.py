#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    options = [['rock'], ['paper'], ['scissors']]

    def inner(n, arr=[[]], cache={}):
        newArr = []
        if n == 0:
            return arr
        else:
            for opt in options:
                for item in arr:
                    newArr += [opt + item]
        plays = inner(n-1, newArr)
        cache[n] = plays
        return plays

    return inner(n)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
