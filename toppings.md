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
# A ploy on manipulating lists(histogram) 
```py
list_ = ["Collins", "Collins", 'Luka', "Rakim", "Rakim", "Lulu"]
dict_ = {}
for name in list_:
    dict_[name] = dict_.get(name, 0) + 1

print(dict_)
```
# A note on inheritance(super())
Python allows inheritance from multipe classes which may result to the `"Don't blink problem"` resulting from hardcoding parent class names which completely breaks down the class.    
`super()` helps avoid the problem.   
Case: Imagine a student who is also an employee.  
```py
class User:
    def __init__(self, name):
        print("User init")
        self.name = name

class Employee(User):
    def __init__(self, name, salary):
        super().__init__(name)
        print("Employee init")
        self.salary = salary

class Student(User):
    def __init__(self, name, grade):
        super().__init__(name)
        print("Student init")
        self.grade = grade

# A class inheriting from BOTH Student and Employee
class TeachingAssistant(Student, Employee):
    def __init__(self, name, grade, salary):
        # This magically initializes BOTH Student AND Employee, and ensures 
        # User.__init__ is only called ONCE!
        super().__init__(name, grade, salary)
```
Python uses `MRO(Method Resolution Order)`. It creates a linear pipeline of one's classes.  
When `TeachingAssistant` calls `super()`, Python looks at the pipeline steps through it sequentially.  
Because every subclass uses `super()`, the initialization flows predictably through `Student`, then jumps over to `Employee`, and finally hits `User`. If you hardcoded the parent names instead of using `super()`, `User.__init__` would end up getting called twice, accidentally overwriting data and wasting processing power.  
# Regex
**Regular expression:** a sequence of characters used to search for a pattern inside of a string.   
**Pattern:** a description of sequences of characters that share certain traits with one another.  
Sequences do not need to be the same length or share any common characters to pattern match.  
Also called a `filter`.
## History
RegEx came about in the 1950's and 1960's in various forms. Among the first appearances of regular expressions in program form was when `Ken Thompson` built `Stephen Cole Kleene's` notation into the editor `QED` as a means to match patterns in text files. Since then, there have been various implementations of regular expressions developed.    
We use Python regular expression, an implementation based off mostly of the PERL language.  
A key difference btwn the two is that regex in Python requires us to import the re module whereas it is natively supported in PERL and many languages.  

## Writing Regular Expressions
```py
pattern = r'abc'
```
`r` stands for `raw`, which means that the escape characters such as backslashes`(\)` are read and not ignored.  
This expands the number of characters that can go into a pattern and allows you to search for patterns with greater flexibility.  
## Metacharacters
Allow one to use pre-defined shorthand to match specific characters.   
`\d` Will match any `digit` in the text.  
`\w` will match any `word character`(letters, numbers and underscores.)   
`\W` matches any `non-word character`.   
`\s` matches any whitespaces.    
## Only specific characters
`r"aeiou"` won't work for vowels.  
`r[aeiou]` will work - looks for **one single character** in our text which matches any of the characters inside the square brackets.     
## Ranges
We can, for instance write a regex to match the first ten characters like `r"[abcdefghij]"`.  
We can shorten this by using a RegEx range: `r'[a-j]'`.  
`r'[0123456789]'` becomes `r'[0-9]'`  
`r'[A-z]'` represents all letters, both in upper and lower case.  
## Double Vowels
For the longest way, we wil have to do something like:  
`r'aa|ae|ai|ao|au|ea|ee|ei|eo|eu|ia|ie'`   
An improvement is to use two sets of square brackets with vowels, each one representing a single character:     
`r'[aeiou][aeiou]'`  
Our most efficient, however, is to use repetitions:  
`r'[aeiou]{2}'`  
The curly braces sorrounding mean that the pattern or character directly preceding it must repeat that number of times.  
## Bluff
You could literally match the whole monologue with the simple RegEx: `r'.*'`but where is the fun in that?     
## The 're' Module
In Python, regular expressions require you to use the `re` module from the standard library.  
When we say *standard library*, it means that it was downloaded onto our computer when we installed Python. We still need to import it, but we do not need to include it in our Pipfile.    
**Python's standard library** is a collection of modules that are downloaded when you install any version of Python.  
```py
import re

text = "This is a regular text."
```
The `.` character matches anything.  
If we want to match the period specifically we should end our pattern with `\.`  
```py
import re
text = "This is some regular text."
pattern = r'This is some regular text\.'
```
### `re` Methods
#### compile()
```py
import re
text = "This is some regular text."
pattern = r"This is some regular text\."
regex = re.compile(pattern)
```
*Note: You can use the `re` module without compiling patterns beforehand. This is **not** recommended because it will require you to include your pattern as an argument to every new `re` method that you run. Gross!*  
#### dir()
```
dir(regex)
# => ['__class__', '__class_getitem__', '__copy__', '__deepcopy__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'findall', 'finditer', 'flags', 'fullmatch', 'groupindex', 'groups', 'match', 'pattern', 'scanner', 'search', 'split', 'sub', 'subn']
```
#### search(), match()
It searches to see if there is a match for your regular expression in the text.  
```py
import re
text = 'A regular text.'
pattern = r"text"
regex = re.compile(pattern)
match = regex.search(text)
print(match)
# => <re.Match object; span=(7, 11), match='text'>
```
The `search()` method returns an `re.Match` object.  
```py
dir(match)
# => [(ignoring magic methods...), 'end', 'endpos', 'expand', 'group', 'groupdict', 'groups', 'lastgroup', 'lastindex', 'pos', 're', 'regs', 'span', 'start', 'string']
```
An `re.Match` object contains an index for its start and end locations in the string that your RegEx is being checked against. It also contains the string itself.  
```py
match.start()
# => 7
match.end()
# => 11
match.span()
# => (7, 11)
match.string
# => 'I love text. Text text text text text.'
```
There is also a  `match()` that belongs to the `re`objects.   
The match searches if there is a match for your regular expression that starts from the *beginning* of the text, returning an `re.Match` object if one is found.  
If you're feeling very particular, the `fullmatch()` method checks the text from the beginning to the end, returning an `re.Match` object if the whole thing is a match.   
The `search()`, `match()` and `fullmatch()` methods are useful if you're just checking to see if a match exists; if you're looking for the strings that match your pattern, `findall()` is a better option.  
*`match()` returns a match object if there is a match that starts at `0` index of your search string.(The start only and the succedent don't matter.)*   
*`fullmatch()` returns a match object if your pattern `fully matches` your string - from 0 all the way to the end.*   
#### findall()
Very straightforward(and therefore very useful).    
Like `search()`, it searches to see if there are matches for the regex within the text.  
It returns a `list` of matching strings instead of `re.Match`  
```py
import re
text = 'The big red cat ate the fat rat.'
pattern = r'[A-z]{3}'
regex = re.compile(pattern)
regex.findall(text)
# => ['The', 'big', 'red', 'cat', 'ate', 'the', 'fat', 'rat']
```
#### split() and sub()
Regular expressions are helpful in finding strings that match certain patterns, but also gives us the ability to manipulate strings.  
The `re` module provides us many methods to do this - split() and sub() are the most useful.    
`split()` returns a list of strings that surround a pattern that you choose to split around
```py
story = "I went to the park and I saw my friend and my friend's dog was there and we ran around and there was another dog and the other dog didn't like my friend's dog but then they got used to each other and they ran to the creek and we ran to the creek too to keep them out of the water and they went in the water and then we went in the water and the water was cold and we got out of the water and Mrs. Smith got mad at us and we went back to the classroom and got hot chocolate and then we watched a movie and now we're going home."
and_pattern = re.compile(r'\sand')
and_pattern.split(story)
# => ['I went to the park', ' I saw my friend', " my friend's dog was there", ' we ran around', ' there was another dog', " the other dog didn't like my friend's dog but then they got used to each other", ' they ran to the creek', ' we ran to the creek too to keep them out of the water', ' they went in the water', ' then we went in the water', ' the water was cold', ' we got out of the water', ' Mrs. Smith got mad at us', ' we went back to the classroom', ' got hot chocolate', ' then we watched a movie', " now we're going home."]
```
`\s` replaces a single whitespace character.      
The `sub()` method allows us to further manipulate our search string.  
`sub()` takes a substitution as a parameter.  
```py
and_pattern.sub(".", story)
```


