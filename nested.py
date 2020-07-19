#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = "Nikal Morgan"

import sys


def is_nested(line,
              symbols={"(": ")", "[": "]", "{": "}", "<": ">", "(*": "*)"}):
    """Validate a single input line for correct nesting"""
    # print(line, len(line))
    keys = symbols.keys()
    values = symbols.values()
    stack = []
    index = 0
    symbol = ''
    while index != len(line):
        symbol = line[index]
        if index + 1 != len(line):
            if symbol == "(" and line[index+1] == "*":
                index = index + 1
                symbol = "(*"
                if "(*" in stack and index + 1 == len(line)-1:
                    return "No, position error at {}".format(index)
                if "(*" not in stack and index + 1 == len(line)-1:
                    return "No, position error at {}".format(index-1)
            if symbol == "*" and line[index+1] == ")":
                index = index + 1
                symbol = "*)"
                if "(*" not in stack and index + 1 == len(line)-1:
                    return "No, position error at {}".format(index)
        if symbol in keys:
            stack.insert(0, symbol)
            if index+1 == len(line) and len(stack) != 0:
                return "No, position error at {}".format(index+1)
        elif symbol in values:
            if len(stack) == 0:
                return "No, position error at {}".format(index)
            if stack[0] == keys[values.index(symbol)]:
                stack.pop(0)
            else:
                for s in stack:
                    if s == keys[values.index(symbol)]:
                        stack.remove(s)
                if index + 1 == len(line):
                    return "No, position error at {}".format(index)
        index = index + 1
    if len(stack) != 0:
        return "No, position error at {}".format(index+1)
    else:
        return "Yes"


def main(args):
    """Open the input file and call `is_nested()` for each line"""
    # Results: print to console and also write to output file
    with open(args[0], 'r') as in_put:
        lines = in_put.read().splitlines()
    for line in lines:
        print(is_nested(line))
        with open('output.txt', 'a') as out_put:
            out_put.write(is_nested(line)+'\n')


if __name__ == '__main__':
    main(sys.argv[1:])

