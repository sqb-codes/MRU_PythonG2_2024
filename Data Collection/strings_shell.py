Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x = 12
text = "Hello World"
type(text)
<class 'str'>
len(text)
11
text[0]
'H'
text[6]
'W'
text[-1]
'd'
text[0:4]
'Hell'
text[0:10]
'Hello Worl'
text[0:20]
'Hello World'
text[0:]
'Hello World'
text[:10]
'Hello Worl'
text[:]
'Hello World'
text[0:11:1]
'Hello World'
text[0:11:2]
'HloWrd'
text[0:11:3]
'HlWl'
text[10:0]
''
text[10:0:-1]
'dlroW olle'
text[::-1]
'dlroW olleH'
dir(text)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
text
'Hello World'
text.lower()
'hello world'
text.upper()
'HELLO WORLD'
text.capitalize()
'Hello world'
text.title()
'Hello World'
text.swapcase()
'hELLO wORLD'
text = "Hello how are you ?"
text.find('o')
4
text.count('o')
3
text.find('o', 5)
7
text.find('o', 8)
15
text.index('o')
4
text.index('o', 5)
7
text.index('o', 8)
15
text.index('z')
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    text.index('z')
ValueError: substring not found
text.find('z')
-1
text.startswith('A')
False
text.startswith('H')
True
text.endswith('?')
True
text.endswith('.')
False
text.isalnum()
False
text.islower()
False
>>> text.upper()
'HELLO HOW ARE YOU ?'
>>> text.isupper()
False
>>> text.isnumeric()
False
>>> text.split()
['Hello', 'how', 'are', 'you', '?']
>>> text = "   Hello    "
>>> text.strip()
'Hello'
>>> text.lstrip()
'Hello    '
>>> text.rstrip()
'   Hello'
>>> text.replace('Hello', 'Bye')
'   Bye    '
