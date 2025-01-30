Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = [23,45,67,78,89,90]
name = ('john','sam','raj','rez','gam','lala')
a+name
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a+name
TypeError: can only concatenate list (not "tuple") to list
a
[23, 45, 67, 78, 89, 90]
d = [a,name]
d
[[23, 45, 67, 78, 89, 90], ('john', 'sam', 'raj', 'rez', 'gam', 'lala')]
a = id
class = [id , name]
SyntaxError: invalid syntax
d = class
SyntaxError: invalid syntax
d = Class
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    d = Class
NameError: name 'Class' is not defined
Class = d
Class = [id,name]
class
SyntaxError: invalid syntax
Class
[<built-in function id>, ('john', 'sam', 'raj', 'rez', 'gam', 'lala')]
N.id = id
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    N.id = id
NameError: name 'N' is not defined
N id = id
SyntaxError: invalid syntax
Nid = id
nid
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    nid
NameError: name 'nid' is not defined. Did you mean: 'Nid'?
Nid
<built-in function id>
Num = Nid
Num
<built-in function id>
Num = [12,23,34,45,56,67,78,89,90]
Class = [Num,name]
Class
[[12, 23, 34, 45, 56, 67, 78, 89, 90], ('john', 'sam', 'raj', 'rez', 'gam', 'lala')]
Num.sort
<built-in method sort of list object at 0x0000011EA2A45580>
max(Num)
90
a = [23,45,67,78,89,90]
//list concept
SyntaxError: invalid syntax
/list concept
SyntaxError: invalid syntax
#list concept
# Tuple
tup = (14,14,67,98,09,1.5)
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
tup = (9,9,1,3,1.4,6)
tup.count
<built-in method count of tuple object at 0x0000011EA0250D60>
tup.count(tup)
0
tup.count(9)
2
tup.index
<built-in method index of tuple object at 0x0000011EA0250D60>
tup.index(4)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    tup.index(4)
ValueError: tuple.index(x): x not in tuple
>>> set1 = {1, 2, 3, 4}
... set2 = {3, 4, 5, 6}
... 
... print(set1.union(set2))  # {1, 2, 3, 4, 5, 6}
... print(set1.intersection(set2))  # {3, 4}
... print(set1.difference(set2))
SyntaxError: multiple statements found while compiling a single statement
>>> set1 = {1,2,3}
>>> set2 = {5,6,7}
>>> set1.union(set2)
{1, 2, 3, 5, 6, 7}
>>> set2.isdisjoint
<built-in method isdisjoint of set object at 0x0000011EA2A08AC0>
>>> set2
{5, 6, 7}
>>> Set2.union(set1)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    Set2.union(set1)
NameError: name 'Set2' is not defined. Did you mean: 'set2'?
>>> set2.union(set1)
{1, 2, 3, 5, 6, 7}
>>> set1.pop()
1
>>> set1
{2, 3}
>>> #dictonaries
>>> Colors = {'red' : ['apple','peach','cherry'],'yellow' : ['mango','banana'],'green':['grapes','kiwi"],'orange' : ['orange','papaya']}
...                                                                                     
SyntaxError: unterminated string literal (detected at line 1)
>>> Colors = {'red' : ['apple','peach','cherry'],'yellow' : ['mango','banana'],'green':['grapes','kiwi'],'orange' : ['orange','papaya']}
...                                                                                     
>>> Colors.items()
...                                                                                     
dict_items([('red', ['apple', 'peach', 'cherry']), ('yellow', ['mango', 'banana']), ('green', ['grapes', 'kiwi']), ('orange', ['orange', 'papaya'])])
>>> Colors.keys()
...                                                                                     
dict_keys(['red', 'yellow', 'green', 'orange'])
