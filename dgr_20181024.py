Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> str1 = "Hello"
>>> str2 = "there"
>>> bob = str1 + str2
>>> print(bob)
Hellothere
>>> str3 = '¹23'
>>> str3 = str3 + 1

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    str3 = str3 + 1
TypeError: cannot concatenate 'str' and 'int' objects
>>> x = int(str3) + 1

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    x = int(str3) + 1
ValueError: invalid literal for int() with base 10: '\xc2\xb923'
>>> x=int(str3)+1

Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    x=int(str3)+1
ValueError: invalid literal for int() with base 10: '\xc2\xb923'
>>> x = int(str3)+1

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    x = int(str3)+1
ValueError: invalid literal for int() with base 10: '\xc2\xb923'
>>> x = 
int
(str3) + 1
SyntaxError: invalid syntax
>>> pint(x)

Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    pint(x)
NameError: name 'pint' is not defined
>>> int = (str3) + 1

Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    int = (str3) + 1
TypeError: cannot concatenate 'str' and 'int' objects
>>> name = input('Enter:')
Enter:Chuck

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    name = input('Enter:')
  File "<string>", line 1, in <module>
NameError: name 'Chuck' is not defined
>>> print(name)

Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print(name)
NameError: name 'name' is not defined
>>> name = input('Enter:')
Enter:Chuck

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    name = input('Enter:')
  File "<string>", line 1, in <module>
NameError: name 'Chuck' is not defined
>>> name = raw_input("Enter")
Enter
>>> name = input("Enter")
Enter Chuck

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    name = input("Enter")
  File "<string>", line 1, in <module>
NameError: name 'Chuck' is not defined
>>> var = raw_input("Enter")
Enter
>>> name = input("Enter")
Enter>? Chuck

Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    name = input("Enter")
  File "<string>", line 1
    >? Chuck
    ^
SyntaxError: invalid syntax
>>> input("Enter")
Enter>? Chuck

Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    input("Enter")
  File "<string>", line 1
    >? Chuck
    ^
SyntaxError: invalid syntax
>>> x = int(apple) - 10

Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    x = int(apple) - 10
NameError: name 'apple' is not defined
>>> zot = 'abc'
>>> print(zot[5])

Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    print(zot[5])
IndexError: string index out of range
>>> str = '¹23'
>>> int(str3)

Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    int(str3)
ValueError: invalid literal for int() with base 10: '\xc2\xb923'
>>> int(123)
123
>>> str = '¹23'
>>> str = str3 +1

Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    str = str3 +1
TypeError: cannot concatenate 'str' and 'int' objects
>>> str = 123 + 1
>>> x = int(123) + 1
>>> print(x)
124
>>> 

