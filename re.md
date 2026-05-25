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
