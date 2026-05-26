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
`\d` Will match any `digit` in the text. (some older regex do not support itm but they all support `\w` and `\s`)  
`\w` will match any `word character`(letters, numbers and underscores.)`[A-za-z0-9_]`     
`\W` matches any `non-word character`.   
`\s` matches any single whitespace character -- `space, newline, return, tab, form [\n\r\t\f]`      
`\S` matches any non-whitespace 
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
## Ignoring Sets of Characters
It involves enclosing the characters in a square bracket and use of caret`(^)`.  
`[^aeiou]`
## Bluff
You could literally match the whole monologue with the simple RegEx: `r'.*'`but where is the fun in that?     
## The 're' Module
In Python, regular expressions require you to use the `re` module from the standard library.  
When we say *standard library*, it means that it was downloaded onto our computer when we installed Python. We still need to import it, but we do not need to include it in our Pipfile.    
**Python's standard library** is a collection of modules that are downloaded when you install any version of Python. 
###  Escape Character
Getting the quotes, backslashes and other operational characters  which have special meaning into one's regex requires that you lead with an escape character, the backslash `(\)`. 
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
`re.compile(pattern, flags=0)`
```py
import re
text = "This is some regular text."
pattern = r"This is some regular text\."
regex = re.compile(pattern)
```
*Note: You can use the `re` module without compiling patterns beforehand. This is **not** recommended because it will require you to include your pattern as an argument to every new `re` method that you run. Gross!* 
```py
str_ = "Wow! What a time to be alive!!"
match = re.search(r"alive!!", str_)
print(match.group())
```
#### dir()
```
dir(regex)
# => ['__class__', '__class_getitem__', '__copy__', '__deepcopy__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'findall', 'finditer', 'flags', 'fullmatch', 'groupindex', 'groups', 'match', 'pattern', 'scanner', 'search', 'split', 'sub', 'subn']
```
#### search(), match()
`re.search(pattern, string, flags=0)`  
`re.match(pattern, string, flags=0)`  
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
##### A note on the Regular Expression Objects
The three functions take the syntax `Pattern.[the-method](string[, pos[, endpos]])` to specify the start and end position of the regex.  
```py
pattern = re.compile("d")
pattern.search("dog")     # Match at index 0

pattern.search("dog", 1)  # No match; search doesn't include the "d"
```
```py
pattern = re.compile("o")  
pattern.match("dog")      # No match as "o" is not at the start of "dog".
pattern.match("dog", 1)   # Match as "o" is the 2nd character of "dog".
```
```py
pattern = re.compile("o[gh]")
pattern.fullmatch("dog")      # No match as "o" is not at the start of "dog".
pattern.fullmatch("ogre")     # No match as not the full string matches.
pattern.fullmatch("doggie", 1, 3)   # Matches within given limits.
```
#### split() and sub()
`re.split(pattern, string, maxsplit, flags=0)`
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
`re.sub(pattern, repl, string, count=0, flags=0)`   
The `sub()` method allows us to further manipulate our search string.  
`sub()` takes a substitution as a parameter.    
If the pattern isn't found, the string is returned unscathed.  
The *repl* can be a function or a string.  
```py
and_pattern.sub(".", story)
```
```py
  str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
  ## re.sub(pat, replacement, str) -- returns new string with all replacements,
  ## \1 is group(1), \2 group(2) in the replacement
  print(re.sub(r'([\w\.-]+)@([\w\.-]+)', r'\1@yo-yo-dyne.com', str))
  ## purple alice@yo-yo-dyne.com, blah monkey bob@yo-yo-dyne.com blah dishwasher
```
As a function example:
```py
re.sub(r'def\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\):',
       r'static PyObject*\npy_\1(void)\n{',
       'def myfunc():')
```
If repl is a function, it is called for every non-overlapping occurrence of pattern. The function takes a single Match argument, and returns the replacement string. For example:   
```py
def dashrepl(matchobj):
    if matchobj.group(0) == '-': return ' '
    else: return '-'

re.sub('-{1,2}', dashrepl, 'pro----gram-files')

re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam', flags=re.IGNORECASE)
```
*When asking for a substitution, the replacement string must be of the same type as both the pattern and the search string.*  
### More methods
#### finditer()
`re.finditer(pattern, string, flags=0)`  
Returns an iterator yielding Match object over all non-overlapping matches for the RE pattern in string.  
#### subn()
`re.subn(pattern, repl, string, count=0, flags=0)`  
Perform the same operation as `sub()`, but return a tuple `(new_string, number_of_subs_made)`  
#### escape()
`re.escape(pattern)`  
Escape special characters in pattern.   
This is useful if you want to match an arbitrary literal string that may have regular expression metacharacters in it. For example:  
```py
print(re.escape('https://www.python.org'))


legal_chars = string.ascii_lowercase + string.digits + "!#$%&'*+-.^_`|~:"
print('[%s]+' % re.escape(legal_chars))


operators = ['+', '-', '*', '/', '**']
print('|'.join(map(re.escape, sorted(operators, reverse=True))))
```
This function must not be used for the replacement string in `sub()` and `subn()`, only backslashes should be escaped. For example: 
```py
digits_re = r'\d+'
sample = '/usr/sbin/sendmail - 0 errors, 12 warnings'
print(re.sub(digits_re, digits_re.replace('\\', r'\\'), sample))
```
*Changed in version 3.3: The `'_'` character is no longer escaped.*   
*Changed in version 3.7: Only characters that can have special meaning in a regular expression are escaped. As a result, `'!', '"', '%', "'", ',', '/', ':', ';', '<', '=', '>', '@'`, and '`'are no longer escaped.*  
#### purge()
Clear the regular expression cache.  

## More Tips
### Basic Patterns
- `a, X, 9`: ordinary characters match themselves exactly. The meta-characters which do not match themselves because they have special meanings are: `. ^ + ? { [] \ | ()`  
- `.`: Matches any single character except newline `\n`  
- `\b` Boundary between word and a non-word(matches the empty string only at the end or beginning or end of a word. A word is defined as a sequence of word characters. Note that formally, `\b` is defined as the boundary between a `\w` and a `\W` character (or vice versa), or between `\w` and the beginning or end of the string. This means that `r'\bat\b'` matches `'at'`, `'at.'`, `'(at)'`, and `'as at ay'` but not `'attempt'` or `'atlas'`) * Inside a character range(eg. `[\b]`), `\b` represents the backspace character, for compatibility with Python’s string literals.*    
- `^ = start`, `$=end`: match the start and end of the string. (^ has no special meaning if it’s not the first character in the set.)  
- `*` Causes the resulting RE to match 0 or more repetitions of the preceding RE, as many repetitions as possible.   
`ab*` will match `a`, `ab`, or `a` followed by any number of `b`s.  

### Basic Regex Rules
- The search proceeds through the start to the end, stopping at the first match found.  
- All of the pattern must be matched, but not all of the string.  
- If `match = re.search(pattern, str_)` is successful, match is not None and in particular `match.group()` is the matching text.  
```py
  ## Search for pattern 'iii' in string 'piiig'.
  ## All of the pattern must match, but it may appear anywhere.
  ## On success, match.group() is matched text.
  match = re.search(r'iii', 'piiig') # found, match.group() == "iii"
  match = re.search(r'igs', 'piiig') # not found, match == None

  ## . = any char but \n
  match = re.search(r'..g', 'piiig') # found, match.group() == "iig"

  ## \d = digit char, \w = word char
  match = re.search(r'\d\d\d', 'p123g') # found, match.group() == "123"
  match = re.search(r'\w\w\w', '@@abcd!!') # found, match.group() == "abc"
```
### Repetition
- `+` 1 or more of the pattern to its left. (eg. `i+` => 1 or more i's)  
- `*` 0 or more occurrences of the pattern to its left.  
- `?` match 0 or 1 occurrences of the pattern to its left.  
### Leftmost and Largest
First the search finds the most leftmost match for the pattern, and the second it tries to use up as much of the string as possible. i.e `+` and `*` can go as far as possible(`+` and `*` are said to be `"greedy"`.)  
```py
  ## i+ = one or more i's, as many as possible.
  match = re.search(r'pi+', 'piiig') # found, match.group() == "piii"

  ## Finds the first/leftmost solution, and within it drives the +
  ## as far as possible (aka 'leftmost and largest').
  ## In this example, note that it does not get to the second set of i's.
  match = re.search(r'i+', 'piigiiii') # found, match.group() == "ii"

  ## \s* = zero or more whitespace chars
  ## Here look for 3 digits, possibly separated by whitespace.
  match = re.search(r'\d\s*\d\s*\d', 'xx1 2   3xx') # found, match.group() == "1 2   3"
  match = re.search(r'\d\s*\d\s*\d', 'xx12  3xx') # found, match.group() == "12  3"
  match = re.search(r'\d\s*\d\s*\d', 'xx123xx') # found, match.group() == "123"

  ## ^ = matches the start of string, so this fails:
  match = re.search(r'^b\w+', 'foobar') # not found, match == None
  ## but without the ^ it succeeds:
  match = re.search(r'b\w+', 'foobar') # found, match.group() == "bar"
```
### Email Example
```py
  str = 'purple alice-b@google.com monkey dishwasher'
  match = re.search(r'\w+@\w+', str)
  if match:
    print(match.group())  ## 'b@google'
```
The search does not get the whole email address in this case because *\w* does not match the "-" or "." in the address.   
The fix is down below.   
### Square brackets
Will absolutely solve our email parsing issue above:
```py
  match = re.search(r'[\w.-]+@[\w.-]+', str)
  if match:
    print(match.group())  ## 'alice-b@google.com'
```
### Group extraction
The "group" feature of a regex allows one to pick out the parts of the matching text.  
Suppose for the emails problem that we want to extract the username and host separately. To do this, add parentheses `( )` around the username and host in the pattern, like this: `r'([\w.-]+)@([\w.-]+)'`.  
In this case, the parentheses do not change what the pattern will match, instead they establish logical "groups" inside of the match text.  
On a successful search, match.group(1) is the match text corresponding to the 1st left parentheses, and match.group(2) is the text corresponding to the 2nd left parentheses.    
The plain match.group() is still the whole match text as usual.  
```py
  str = 'purple alice-b@google.com monkey dishwasher'
  match = re.search(r'([\w.-]+)@([\w.-]+)', str)
  if match:
    print(match.group())   ## 'alice-b@google.com' (the whole match)
    print(match.group(1))  ## 'alice-b' (the username, group 1)
    print(match.group(2))  ## 'google.com' (the host, group 2)
```
A common workflow with regular expressions is that you write a pattern for the thing you are looking for, adding parentheses groups to extract the parts you want.  
### findall With Files
For files, one may be in the habit of writing a loop to iterate over the lines of the file, you could then call `findall()` on each line.   
Instead, let `findall()` do the iteration for you.  
Just feed the whole file text into `findall()`and let it return a list of all the matches in a single step.  
Recall that `f.read()` returns the whole text of a file in a single string.   
```py
  # Open file
  f = open('test.txt', encoding='utf-8')
  # Feed the file text into findall(); it returns a list of all the found strings
  strings = re.findall(r'some pattern', f.read())
```
### findall and Groups
The parentheses `()` group mechanism can be combined with `findall()`.  
If the pattern includes 2 or more parentheses groups, then instead of returning a list of strings, `findall()` returns a list of `tuples`.  
Each tuple represents one match of the pattern, and inside it is the group(1), group(2).... data.  
So if two parentheses groups are added to the email pattern, then findall() returns a list of tuples, each length containing the username and host. (e.g ("alice", "google.com"))  
```py
  str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
  tuples = re.findall(r'([\w\.-]+)@([\w\.-]+)', str)
  print(tuples)  ## [('alice', 'google.com'), ('bob', 'abc.com')]
  for tuple in tuples:
    print(tuple[0])  ## username
    print(tuple[1])  ## host
```
Once you have the list of tuples, you can loop over it to do some computation for each tuple.   
If the pattern includes no parentheses, then `findall()` returns a list of found strings as in earlier examples.  
If the pattern includes a single set of parentheses, then findall() returns a list of strings corresponding to that single group.  
(Obscure optional feature: Sometimes you have `paren ( )` groupings in the pattern, but which you do not want to extract. In that case, write the parens with a `?:` at the start, e.g. `(?: )` and that `left paren` will not count as a group result.)
### OPTIONS
The `re` functions take options to modify the behavior of the pattern match.  
The option flag is added as an extra argument to the `search()` or `findall()` etc.  
```py
re.search(pattern, str_, re.IGNORECASE)
```
To pass multiple, you'll have to use the bitwise **OR operator**, which is the pipe `|`symbol:  
re.compile() example:   
```py
import re

text = """ERROR: Server is down
warning: low disk space
Error: database disconnected"""

# Combine IGNORECASE (I) and MULTILINE (M)
# This matches 'Error' or 'error' at the start of any line
pattern = re.compile(r"^error:.*", re.IGNORECASE | re.MULTILINE)

matches = pattern.findall(text)
print(matches)
# => ['ERROR: Server is down', 'Error: database disconnected']
```
RE methods directly:
```py
import re

text = "Deep Learning\nMachine Learning"

# Correct way involves using keyword argument 'flags='
result = re.findall(r"learning$", text, flags=re.IGNORECASE | re.MULTILINE)
print(result) # Output: ['Learning', 'Learning']
# Faulty: (Do not do this for direct methods):
# re.findall(r"learning$", text, re.IGNORECASE | re.MULTILINE)
``` 
You may use Inline flags inside the regex string.    
They take the syntax: `(?flags)`   
**i** IGNORECASE  
**m** MULTILINE  
**s** DOTAL   
**x** VERBOSE
```py
import re

text = "Alpha\nbeta"

# (?im) turns on IGNORECASE and MULTILINE automatically
pattern = r"(?im)^beta"

match = re.search(pattern, text)
print(match.group()) 
# => beta
```
- **IGNORECASE** ignore upper/lowercase differences for matching.  
- **DOTALL** allow dot(.) to match newline -- normally it matches anything but newline.  
This can trip you up -- you think `.*` matches everthing, but by default it does not go past the end of a line.  
Note that `*\s*`(whitespaces) includes newlines, so if you want to match a run of whitespace that may include a newline, you can just use `\s`  
- **MULTILINE** Within a string made of many lines, allow `^` and `$` to match the start and end of each line.  
Normally, `^/$`would just match the start and end of the whole string.  
re.A (ASCII-only matching)

- `re.I` (ignore case) (re.IGNORECASE)
- `re.L` (locale dependent)
- `re.M` (multi-line)  (re.MULTILINE)
- `re.S` (dot matches all)  (re.DOTALL) (corresponds with the inline flag `(?s)`)   
- `re.U` (Unicode matching)  (re.UNICODE) 
- `re.A` (ASCII-only matching) (re.ASCII)
- `re.DEBUG`
- `re.L` (re.LOCALE)
- `re.X` (verbose) (re.VERBOSE) (inline flag -- `(?x)`) (This flag allows you to write regular expressions that look nicer and are more readable by allowing you to visually separate logical sections of the pattern and add comments. Whitespace within the pattern is ignored, except when in a character class, or when preceded by an unescaped backslash, or within tokens like `*?`, `(?:` or `(?P<...>`. For example, `(? :` and `* ?` are not allowed.)  
This means that the two following regular expression objects that match a decimal number are functionally equal:  
```py
a = re.compile(r"""\d +  # the integral part
                   \.    # the decimal point
                   \d *  # some fractional digits""", re.X)
b = re.compile(r"\d+\.\d*")
```
- `re.NOFLAG`
Indicates no flag being applied, the value is `0`.  
This flag may be used as a default value for a function keyword argument or as a base value that will be conditionally ORed with other flags. Example of use as a default value:  
```py
def myfunc(text, flag=re.NOFLAG):
    return re.match(text, flag)
```
### Greedy vs Non-Greedy
Suppose you have text with tags in it: `<b>foo</b> and <i>so on</i>`.  
Suppose you are trying to match each tag with the pattern `(<.*>)`  
The result is a little surprising, but the `greedy` aspect of the `.*` causes it to match the whole `'<b>foo</b> and <i>so on</i>'` as one big match.  
There is an extension to regular expression where you add a `?` at the end, such as `.*?` or `.+?`, changing them to be *non-greedy*.  
Now they stop as soon as they can. So the pattern `'(<.*?>)'` will now get `'<b>'` as the first match and `'</b>'` as the second match......     
The `.*?` extension originated in Perl, and regular expressions that include Perl's extensions are known as Perl Compatible Regular Extensions -- `pcre`.  
Python includes the pcre support.  
Many command line utils etc. have a flag where they accept pcre patterns.  
An older but widely used technique to code this idea of "all of these chars except stopping at X" uses the `square-bracket style`. For the above you could write the pattern, but instead of `.*` to get all the chars, use `[^>]*` which skips over all characters which are not `>` (the leading `^` "inverts" the square bracket set, so it matches any char not in the brackets).
### More Tips    
#### possessive quantifiers
`*+`,`++`,`?+` quantifiers, those where `+` is appended also match as many other as possible.  
However unlike the true greedy quantifiers, these do not allow back-tracking when the expression following it fails to match. These are known as possessive quantifiers.  
For example, `a*a` will match `'aaaa'` because the `a*` will match all 4 `'a'`s, but, when the final `'a'` is encountered, the expression is backtracked so that in the end the `a*` ends up matching 3 `'a'`s total, and the fourth `'a'` is matched by the final `'a'`. However, when `a*+a` is used to match `'aaaa'`, the `a*+` will match all 4 `'a'`, but when the final `'a'` fails to find any more characters to match, the expression cannot be backtracked and will thus fail to match. `x*+`, `x++` and `x?+` are equivalent to `(?>x*)`, `(?>x+)` and `(?>x?)` correspondingly.  
#### A note on sets and special characters
Special characters lose their meaning inside sets.  
`[(+*)]` will match any of the literal character `('`, `'+'`, `'*'`, or `')'`.  
#### More on the Backslash `\`
Backslash either escapes characters which have special meaning in a set such as `'-'`, `']'`, `'^'` and `'\\'` itself or signals a special sequence which represents a single character such as `\xa0` or `\n` or a character class such as `\w` or `\S`. Note that **\b** represents a **single “backspace”** character, **not a word boundary** as outside a set, and numeric escapes such as `\1` are always **octal escapes**, not **group references**. Special sequences which do not match a single character such as `\A` and `\z` are not allowed.   
#### `?:...`
A non-capturing version of a regular parentheses.  
Matches whatever regular expression is inside the parenthese, but the substring matched by the group *cannot* be retrieved after performing a match or referenced later in the pattern.  
#### `?#...`
A comment; the contents of the parenthese are simply ignored.  
#### `(?!...`
Matches if `...` doesn’t match next. This is a negative lookahead assertion. For example, `Isaac (?!Asimov)` will match `'Isaac '` only if it’s not followed by `'Asimov'`.  
#### `(?(id/name)yes-pattern|no-pattern)`
Will try to match with `yes-pattern` if the group with given id or name exists, and with `no-pattern` if it doesn’t. no-pattern is optional and can be omitted. 
#### `\A`
Matches only at the start of the string.  
#### `\number`
Matches the contents of the group of the same number.   
Groups are numbered starting from 1. For example, `(.+) \1` matches `'the the'` or `'55 55'`, but not `'thethe'` (note the space after the group). This special sequence can only be used to match one of the first 99 groups.      

#### `\B`
Matches the empty string, but only when it is not at the beginning or end of a word.  
This means that `r'at\B'` matches `'athens'`, `'atoms'`, `'attorney'`, but not `'at'`, `'at. '`or `'at!'`.  
`\B` is the opposite of `\b`, so word characters in Unicode (str) patterns are Unicode alphanumerics or the underscore, although this can be changed by using the ASCII flag.  
#### `\z`
Matches only at the end of the string.
#### `\Z`
same as `\z`. For compatibility with old Python versions.  
#### Others
- \a      \b      \f      \n
- \N      \r      \t      \u
- \U      \v      \x      `\\`
#### To ensure that a specific string is used only once.  
```py
r'^(?!.*_.*_)[a-zA-Z0-9]+_[a-zA-Z0-9]+$'
```
The `(?!.*_.*_)` is the magic guard(a negative lookahead). Right at the start of the string, it looks ahead and tells the regex to fail immediately if it finds and underscore followed by anything, followed by a second underscore.   
Once the guard approves that there are no duplicate underscores, this part handles the actual match. It expects alphanumeric characters, a single literal `_`, and more alphanumeric characters.  
You can induce a shortcut by:
```
^[^_]*_[^_]*$
```
- `^[^_]*`: From the start of the string, match any number of characters that are not an underscore.   
- `_`: Match the single allowed underscore.   
- `[^_]*$`: Match any number of characters that are not an underscore until the end of the string.  
When dealing with a list-like approach:
```py
r'^\[(?!.*_.*_)\w*_\w*\]$'
```
We escape the brackets as `\[` and `\]` to indicate we want literal bracket characters, not a character class.   
To find unique character:
```
(.)(?!.*\1)
```
- The `(.)` is a capturing group that matches any single character(except a newline). It stores this character as a group number`(\1)` 
- `(?! ...)` Is a negative lookahead. It tells the regex engine to look ahead from the current position and fail to match if the stuff inside these parentheses happens next.  
- `.*\1`: inside the lookahead, this means any characters(`.*`) followed by a repetition of our first captured character.   
"Match a character, but only if that exact same character cannot be found anywhere else ahead of it in the string."  

To find a unique character:
```
\b(?!\w*(\w)\w*\1)\w\b
```
##### Tip on uniqueness
```py
email_address = r"(?!(^\d.))(?!.*\.{2})(?!.*\d)[a-z0-9\.]+@[a-z]+.[a-z]+"
```
- `(?!(^\d.))` It ensures that the email does not start with a digit. The caret`^` in this case means the literal start of the email.
- `(?!.*\.{2})` asserts that there should not be two concurrent `.`s.  
- `(?!.*\d)`(obviously contrived) asserts that there should not be any digit used.  
#### ^ vs \A & $ vs \Z
The difference between them come down to how they handle multi-line strings and trailing newlines(`\`).  
##### \A & ^
`\A` matches the absolute beginning of the entire string, ignoring the line breaks on multiline(`re.MULTILINE`).    
`^` matches the beginning of a line or string. By default, it matches the start of the string. If `re.MULTILINE` is turned on, it matches the start of every single line(right after the `\n`).  
```py
import re

text = "Hello\nWorld"

# ^ with MULTILINE matches both 'Hello' and 'World'
print(re.findall(r"^.+$", text, re.MULTILINE))  # Output: ['Hello', 'World']

# \A ignores MULTILINE and only matches 'Hello'
print(re.findall(r"\A.+", text, re.MULTILINE))   # Output: ['Hello']
```
##### $ vs \Z vs \z
Python treats them differently based on whether there is a trailing newline at the very end of your string.  
- `$` (The Line End): Matches the end of a line or the string. If your string has a trailing newline (e.g., `"text\n"`), `$` matches right before that newline. If `re.MULTILINE` is active, it matches before every newline character in the string.   
- `\Z` (The Soft String End): Matches the end of the entire string, but with a quirk: if the string ends with a newline, `\Z` matches right before that final newline. It completely ignores `re.MULTILINE`.  
- `\z` (The Absolute Hard String End): Matches the absolute end of the string, period. It does not make an exception for a trailing newline. (Note: In Python's native `re` module, `\z` is actually not supported; Python uses `\Z` for string ends. However, `\z` is standard in other engines like PCRE, Ruby, and Python's alternative `regex` module).  
```py
import re

text = "Python\n"

# '$' matches because it allows a trailing newline
print(bool(re.match(r"Python$", text)))  # True

# '\Z' matches because it also allows a final trailing newline
print(bool(re.match(r"Python\Z", text))) # True

# If you use the strict third-party 'regex' module with '\z':
# re.match(r"Python\z", text) -> False (because of the hidden '\n' at the very end)
```
#### Match Objects and Regular Expressions Objects expounded on.  
