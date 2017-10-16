input() always returns a string.
using input to receive a number will require explicit coercion.

### Type Coercion
string()
int()
float()

eg: string(29) outputs '29'
or
myAge = 29
print('I am no longer ' + string(myAge) + ' years old' )#

An integer can be equal to a float:
3.00 == 3
true