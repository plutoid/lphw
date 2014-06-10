#!/usr/bin/python
# coding:utf8

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()

print "So, you're %s old, %r tall and %r heavy." % ( # %r means raw
    age, height, weight)

