import re

text = 'This is a regular text. And this text too.'
pattern = r'text'
regex = re.compile(pattern)
match = regex.search(text)
print(match)