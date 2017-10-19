# Unsorted tips that I've picked up while learning!

input() always returns a string.
using input to receive a number will require explicit coercion.

### Type Coercion
string()
int()
float()

eg: string(29) outputs '29'
or
myAge = 29
print('I am no longer ' + string(myAge) + ' years old' )

An integer can be equal to a float:
3.00 == 3
true

### Boolean order of operation
1. not
2. and
3. or

## for and while loops
check the fiveTimes.py file for examples of each

## Range function
range(x y z)
range can be given between 1 and 3 arguments
range(x) will count from 0 up to but not including x
range(x y) will count from x up to but not including y
range(x y z) will count from x, up to but not including y in steps of z
eg
range(0 11 2) will output
0 2 4 6 8 10