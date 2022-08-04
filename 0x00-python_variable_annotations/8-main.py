#!/usr/bin/env python3

make_multiplier = __import__('8-make_multiplier').make_multiplier
print(make_multiplier.__annotations__)
fun = make_multiplier(4.0)
print("{}".format(fun(2.0)))
print("{}".format(fun(5.0)))

