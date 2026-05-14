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
