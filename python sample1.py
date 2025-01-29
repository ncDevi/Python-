Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
2*3
6
6
6
>>> 'devi' *3
'devidevidevi'
>>> # Step 1: Define variables
... a = 10
... b = 5
... 
... # Step 2: Perform operations
... sum_result = a + b
... difference = a - b
... product = a * b
... quotient = a / b
... 
... # Step 3: Display results
... print(f"The sum of {a} and {b} is {sum_result}.")
... print(f"The difference between {a} and {b} is {difference}.")
... print(f"The product of {a} and {b} is {product}.")
... print(f"The quotient of {a} divided by {b} is {quotient}.")
SyntaxError: multiple statements found while compiling a single statement
>>> print(f"The sum of {a} and {b} is {sum_result}.")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(f"The sum of {a} and {b} is {sum_result}.")
NameError: name 'a' is not defined
>>> a=2
>>> b=76
>>> print("sum of a and b is {sum_result})
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> print ("sum of a and b is {sum_result}")
...       
sum of a and b is {sum_result}
>>> a = 3
...       
>>> b = 4
...       
>>> print ("sum of a and b is {a+b})
...        
SyntaxError: unterminated string literal (detected at line 1)
>>> print ("sum of a and b is {a+b}")
...        
sum of a and b is {a+b}
