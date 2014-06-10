#!/usr/bin/python 

# w3m http://learnpythonthehardway.org/book/ex15.html

from sys import argv

script, filename = argv

txt = open(filename)

print "here'syour file %r: " % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)
print txt_again.read()

