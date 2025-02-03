Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = 4.5
type(a)
<class 'float'>
a = b
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a = b
NameError: name 'b' is not defined
b = a
id(b)
1219409737648
id(a)
1219409737648
ch = "name"
id(ch)
140704017401184
type(ch)
<class 'str'>
#data types
#numeric
#int float complex bool
q = 1
type(q)
<class 'int'>
h=2.89
type(h)
<class 'float'>
complex(q,h)
(1+2.89j)
bool(h)
True
tyoe(true)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    tyoe(true)
NameError: name 'tyoe' is not defined. Did you mean: 'type'?
type(true)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    type(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
type(h)
<class 'float'>
float(q)
1.0
float(false)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    float(false)
NameError: name 'false' is not defined. Did you mean: 'False'?
int(false)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    int(false)
NameError: name 'false' is not defined. Did you mean: 'False'?
int(true)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    int(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
int(True)
1
float(False)
0.0
comples(True,False)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    comples(True,False)
NameError: name 'comples' is not defined. Did you mean: 'complex'?
complex(True,False)
(1+0j)
h>q
True

bool(h<q)
False
bool(h>q)
True


#sequence
#list set tuple string range
lst = [12,23,34,45]
type(lst)
<class 'list'>
num = {23,34,45,56}
type(num)
<class 'set'>
hi = (12,23,34,45)
type(hi)
<class 'tuple'>
kim = "gym"
type(kim)
<class 'str'>
range(h)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    range(h)
TypeError: 'float' object cannot be interpreted as an integer
range('h')
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    range('h')
TypeError: 'str' object cannot be interpreted as an integer
range(100)
range(0, 100)
set{range(100)}
SyntaxError: invalid syntax
list[range(100)]
list[range(0, 100)]
list(range(100))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
list(range(5,100,3))
[5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50, 53, 56, 59, 62, 65, 68, 71, 74, 77, 80, 83, 86, 89, 92, 95, 98]
list(range(0,100,5))
[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
w=list(range(0,50,2))
w
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
type(w)
<class 'list'>
u = {'music':'drums','piano'}
SyntaxError: ':' expected after dictionary key
u = {'music':['drums','piano'],'party':['balloons',['cake']}
     
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
u = {'music':['drums','piano'],'party':['balloons'],['cake']}
     
SyntaxError: ':' expected after dictionary key
u = {'music':['drums','piano'],'party':['balloons','cake']}
     
d_values(u)
     
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    d_values(u)
NameError: name 'd_values' is not defined
u_values()
...      
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    u_values()
NameError: name 'u_values' is not defined
>>> u
...      
{'music': ['drums', 'piano'], 'party': ['balloons', 'cake']}
>>> u.vales()
...      
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    u.vales()
AttributeError: 'dict' object has no attribute 'vales'. Did you mean: 'values'?
>>> d.vales()
...      
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    d.vales()
NameError: name 'd' is not defined
>>> d.values()
...      
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    d.values()
NameError: name 'd' is not defined
>>> u.values()
...      
dict_values([['drums', 'piano'], ['balloons', 'cake']])
>>> u.keys()
...      
dict_keys(['music', 'party'])
>>> d.get('music')
...      
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    d.get('music')
NameError: name 'd' is not defined
>>> u.get('music')
...      
['drums', 'piano']
