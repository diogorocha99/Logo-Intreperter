# main.py

from Parser import Parser


with open("ex2.logo", mode="r") as fh:
    contents = fh.read()

parser= Parser()

parser.Parser(contents)
