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
# `Pie Syntax`
```py
def check_working_hours(func):
    def wrapper(time):
        if 1100 < time < 2100:
            func(time)
        else:
            print("I'm off duty!")
    return wrapper

@check_working_hours
def sweep_floors(time):
    print("Sweeping the floors...")

@check_working_hours
def wash_dishes(time):
    print("Washing the dishes...")

@check_working_hours
def chop_vegetables(time):
    print("Chopping the vegetables...")

sweep_floors(800)
# I'm off duty!
wash_dishes(1000)
# I'm off duty!
chop_vegetables(1200)
# Chopping the vegetables...
```
The `@check_working_hours` is a syntactic sugar for re-assigning a function.  
When Python reads:
```py
@check_working_hours
def sweep_floors(time):
    print("Sweeping the floors...")
```
It immediately translates it behind the scenes to:
```py
def sweep_floors(time):
    print("Sweeping the floors...")

# Python reassigns the variable name 'sweep_floors'
sweep_floors = check_working_hours(sweep_floors)
```
When Python executes `sweep_floors = check_working_hours(sweep_floors)`:   
- **The Outer Function Runs**: check_working_hours is called, and the original `sweep_floors` function is passed in as the argument `func`  
- **The Inner Function is Defined**: Inside, Python defines a new function called `wrapper`. Crucially, it doesn't run `wrapper` yet; it just creates it.  
- **The Closure is Created**: Because `wrapper` sits inside `check_working_hours`, it memorizes the environment it was born in. It "remembers" what `func` is (the original floor-sweeping function). This memory is called a **closure**
- **The Swap Happens**: `check_working_hours` returns the `wrapper` function object.
- **The New Identity**: The variable name sweep_floors is now officially pointing directly to `wrapper`  
The original `sweep_floors` is gone. Whenever you type `sweep_floors` later in your code, you are actually calling `wrapper`.    

Because `sweep_floors` is now actually the `wrapper` function, what you are really executing is:
```py
wrapper(800)
```
*`wrapper` doesn't capture and pass back the result. If `func(time)` returns something, it just vanishes inside the `wrapper`.To make a decorator robust so it handles functions with return values, you would write it like:*
```py
def check_working_hours(func):
    def wrapper(time):
        if 1100 <time < 2100:
            # Capture the return value of the original function
            result = func(time)
            return result
        else:
            return "I'm off duty!"
    return wrapper
```
# A note on strings
In addition to strings being indexed and iterable, they are `immutable`, meaning, with every manipulation of it produces a new object; the original is not replaced.   
# A note on sets & dicts
`set` instantiation must be done using the `set()` class constructor. Closed curly braces `{}` will instanteate an empty dictionary.   
```py
{1, 2, 3, 4, 5, 6} # Yeah, a dictionary just like that....
```
# Glitch 
```
collinskibet@DESKTOP-EQ3N800:~/Development/code/phase-5/PYTHON$ git status
error: object file .git/objects/c2/c6dd9457875339e7ebcfa2a79bbb96643cae8d is empty
error: object file .git/objects/c2/c6dd9457875339e7ebcfa2a79bbb96643cae8d is empty
error: object file .git/objects/c2/c6dd9457875339e7ebcfa2a79bbb96643cae8d is empty
fatal: bad object HEAD
```
The "bad object HEAD" error is Git's indication that its internal db has been corrupted usually due to sudden power outage, a system crash, or a hard drive hiccup that interrupted a write operation.   
Basically, the file Git uses to track your current position (the HEAD) is pointing to a "blob" (a file snapshot) that is now empty or unreadable.  
The actual code is likely to be not affected.  
## Back up the broken state
```
cp -R .git .git_backup
```
## Identify the corruption
Confirm if its just the HEAD or something deeper
```
find .git/objects -type f -empty
```
If it lists files like the one in our error, those objects are toasted.  
Since they are empty, Git can't recover the data from them directly.  
## Soft Fix
Usually, the `index` file is the one that's corrupted. We can try removing it and letting Git rebuilt it.  
### Remove the corrupted index
```
tail -n 20 .git/logs/HEAD
```
The logs will include something like `rm .git/index`. This doesn't delete one's code but just tells git to forget what was "staged".   
### Reset the index.
```
git reset
```
Git will try rebuilding the index based on the last successful commit.  
### Check Status
```
git status
```
## "Deep Fix"(if step 3 failed)
If the error still impedes, the last commit itself might be corrupted.  
We need to point Git to the previous valid commit.   
### Find the last good commit
To actually read the file and see the commit history, one needs to use a text viewer command like `cat` or `tail`.  
#### View the Log File: 
```
tail -n 10 .git/logs/refs/heads/main
```
#### Decode the Log Output:
The second to last line usually contains the hash of the last 'good' commit. (That is the second hash(right before one's name/email)).  
#### Manually override HEAD
```
echo "THE_HASH" > .git/refs/heads/main
```
If it works but still complains about a broken index next, fix it by running:
```
rm .git/index
```
Followed by:
```
git reset
```
If it works, definitely ignore the `.git_backup/` or delete it.  
```
echo ".git_backup/" >> .gitignore
```
```
rm -rf .git_backup/
```
When Git is entirely blotted, after creating a new folder, you can run:
```
cp -r ../MESSED_FOLDER/* .
```
In Linux and MacOS terminals, any file or folder that starts with a dot(like `.git` or `.gitignore`) is considered a hidden file.  
With the use of the wildcard symbol `*`, they will be completely ignored.   
To copy hidden files like `.git`, one would have to name the folder directly without the wildcard.  
```
cp -r ../PYTHON_mess .
```
# A ploy on manipulating lists 
```py
list_ = ["Collins", "Collins", 'Luka', "Rakim", "Rakim", "Lulu"]
dict_ = {}
for name in list_:
    dict_[name] = dict_.get(name, 0) + 1

print(dict_)
```
