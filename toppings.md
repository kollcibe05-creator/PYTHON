#### Print() can Accept an `end`ing
```py
print("Hello world!", end=" ")
print("Hello sun!", end="!! ")
print("Hello sky!", end="!!!\n")
```
`end` is used when for instance, you may be working on a paragraph and you don't need a newline character as print defaults.  
`end` can be a string of any character including the newline `\n`.  
# .nf
Is a special formatter used to display a floating-point number rounded to the specified decimal places.  
```py
price_1 = 3
print(f"Item 1 costs ${price_1:.3f}")

# => Item 1 costs $3.000
```
# dir
Using the dir() function on any Python object will display a list of all the methods that object responds to  
```py
dir("hello")
# => ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', ... ]
```
# Falsy Values
Like JS, Python has many falsy values though they do not map perfectly to one another though.  
Back in JS:  
```js
!!null;
// => false
!!undefined;
// => false
!!false;
// => false
!!0;
// => false
!!NaN;
// => false
!!"";
// => false
```
In Python, use of the `not` operator reverses the truth value of a value, variable or statement.  
`!` still plays a role in Python, but it is only used in the `!=` operator that asserts that two values are not equal.  
# Implicit line joining
PEP 8  guidelineds state that lines should be composed of 79 characters or fewer for function arguments.   
```py     
def take_twenty_arguments(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18, arg19, arg20):
    pass
```
To improve readability, python supports `implicit line joining` inside of parentheses and brackets, which mean that we can add a new line anywhere in the list of arguments as long as it does not interrupt the name of the argument.  
```py
def take_twenty_arguments(arg1, arg2, arg3, arg4, arg5, arg6, arg7, 
arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, 
arg16, arg17, arg18, arg19, arg20):
    pass

# Hanging four-space indents with an added level
def take_twenty_arguments(arg1, arg2, arg3, arg4, arg5, arg6, arg7, 
    arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, 
    arg16, arg17, arg18, arg19, arg20):
    pass
```
# Comparison Operators - JS vs Python
Unlike JS, the `==` function in python `will not coerce strings to numbers before comparing them` or perform some other types coercions.   
For example, using the `==` operator can lead to strange behavior
```js
"1" == 1
// => true
0 == []
// => true
[] == ![]
// => true
```
In Python, the `==` function checks if the objects on both sides are considered the equivalent values.   
```py
"1" == 1
# False
1 == 1
# True
```
There are some differences between Python's `==` and JavaScript's `===` though.   
In JavaScript, the `===` operator checks if both objects have the same identity, i.e. refer to the same space in memory.  
For example, in JavaScript, this example returns `false` because the two arrays are unique objects in memory:
```js
[1, 2, 3] === [1, 2, 3];
// => false
```
In Python, this example returns `True` because Python considers these to have equivalent values  
```py
[1, 2, 3] == [1, 2, 3]
# True
```
Python will also check if an integer has the equivalent value to a Float, even though they're technically different data types.  
```py
1.0 == 1
# True
```
*Note: While Python does have an operator, `is`, that is similar to JavaScript's `===`, it is `not used the same way as it is in JavaScript`. There are very few scenarios when you want to use the is operator in Python; in general, for comparing data, you want to use the `==`*  
