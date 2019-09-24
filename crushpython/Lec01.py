# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'crushpython'))
	print(os.getcwd())
except:
	pass
#%%
from IPython import get_ipython

#%% [markdown]
# # Welcome to "CrushPython"
# 
# -------
# So tell them, 'As surely as I live, declares the LORD, I will do to you the very things I heard you say.' Numbers 14:28  
# 
#%% [markdown]
# __NOTE:__ The following materials have been adpated from the numerous sources including Python and Canopy web sites including my own. Please help me to keep this tutorial up-to-date by reporting any issues or questions. Send any comments or criticisms to `idebtor@gmail.com` Your assistances and comments will be appreciated.  
#%% [markdown]
# ------
# 
# # Lesson - Data Types
# 
# 
# ## Tips on IPython magics
# - Magics is a user-definable mini command language in IPython. Magics come in two kinds:
#     - __Line magics:__ prepended by one % character and whose arguments only extend to the end of the current line.
#     한 단어로 명령어를 쓰는 것.
#     - __Cell magics:__ These use two percent characters as a marker (%%), and they receive as argument both the current line where they are declared and the whole body of the cell.
#     
# - You may use pwd, ls and cd to navigate your file systems and find a file since the Notebook dashboard displays only ~.ipynb files and folders. __Line magics__
# ```
#     pwd
#     ls
#     cd ..
#     pwd
#     pushd
#     popd
# ```
# __Note__: Automagic is ON, % prefix IS NOT needed for line magics.  
# __Recall__: `<Cntl+Enter>` executes the command in the current cell and stays there.
# 
# - A text file can be loaded in a notebook cell with the magic command %load. __cell magics__
# ```
#     %load filename.py
# ```    
# - To save the cell content back into a file add the cell-magic `%%writefile filename.py` at the beginning of the cell and run it. Beware that if a file with the same name already exists it will be __silently overwritten__. For example:
# ```
#     %%writefile foo.py
#     print('Hello World')
# ```
# - To run the foo.py script file saved above:
# ```
#     %run foo
# ```
# - To list all available magics available: 
# ```
#     %lsmagic
# ```
# - To see the help any the magic command add a `?`: like `%load?` or `%%writefile?`.
# - For general help on magic functions type "%magic" For a list of the available magic functions, use %lsmagic. For a description of any of them, type %magic_name?, e.g. '%cd?'.
# 
# See also: [Magic functions](http://ipython.org/ipython-doc/dev/interactive/tutorial.html#magic-functions) from the official IPython docs.
# 

#%%
get_ipython().run_cell_magic('writefile', 'foo.py', "import matplotlib.pyplot as plt\nfrom matplotlib.image import imread\n\nimg = imread('https://github.com/idebtor/KMOOC-ML/blob/master/ipynb/images/lenna.png?raw=true')\nplt.imshow(img)")


#%%
get_ipython().run_cell_magic('writefile', 'foo.py # not alert, overwriting ', "print('Hello world')")

#%% [markdown]
# # First things first
# 
# ----------
# 
# ## Hello World
# - `print()` function - prints a textual representation to the console
# - To represent a string, you may use a pair of single, double, or triple of double quations. Use a triple quote to have a multiple lines of comments. 
# 
# - For example
#     - 'Hello World' 
#     - "Hello World"
#     - """Hello World"""
#     - 'Hello "Mr. Kim"'

#%%
print("Hello World")


#%%
print('hello world')


#%%
print("""Hello world""")
print("'hi'Hello")
print("""hihi
hihi
hihi
hihihih
여러 줄로 보이고 싶을때 사용하면 된다.""")

#%% [markdown]
# # Variables and Types
# -----------
# 
# Let's take a look at the common numerical data types within Python.
# 
# - int - integers: ..., -3, -2, -1, 0, 1, 2, 3, ...
# - float - floating point numbers, decimal point fractions: -3.1, 1.5, 1e-8, 3.141592e5
# - str - character strings, text: "WhynotPython", 'python'
# - bool - boolean values: True and False
# 
# Integers
# --------
# 
# The first of these is the integer type.  We can add integers, getting another integer as the result:

#%%
a = 3

#%% [markdown]
# We can also assign an integer to a variable:

#%%
a

#%% [markdown]
# print() vs evaluate

#%%
a = 5
print(a)

#%% [markdown]
# We can ask the variable for its `type`, and see that it is `int`:

#%%



#%%
# 2**8 * 2**8 = 2**16


#%%
# 2**32


#%%
# 2**64


#%%
# 2*132


#%%
# **1000

#%% [markdown]
# __NOTE__: There is no longer a limit to the value of integers. 
#%% [markdown]
# Floating Point Numbers
# ----------------------
# 
# You can represent real numbers in Python as easily as integers.  For example, we could assign 1.4 to the variable `a`:

#%%
a = 1.4
type(a)

#%% [markdown]
# Notice that the type of `a` is now `float`:

#%%
a = 0.4
if (a == 0.4):
    print('yes, it is 0.4')
else:
    print('no, it is not 0.4')

#%% [markdown]
# Let's do the same thing as done above but with `a = 1.4 - 1.0` and see what happens.

#%%
a = 1.4 - 1.0
if (a == 0.4):
    print('yes, it is 0.4')
else:
    print('no, it is not 0.4')
a

#%% [markdown]
# Python's `float` data type follows the [IEEE 754 floating point standard](http://en.wikipedia.org/wiki/IEEE_floating_point), the same as C, Fortran, C# and just about every other programming language because that's what modern processors use to do math quickly. 
# 
# Floating-point real numbers can't be represented with exact precision due to hardware limitations. This can lead to cumbersome effects. See the [Python docs](https://docs.python.org/3.6/tutorial/floatingpoint.html) for the details.
# 
# If we add our floating point number to 1.1, we get 1.2 as we expect:

#%%
a = 0.1 + 0.1 + 0.1
a


#%%
a = 0.1 + 0.1 + 0.1
print(a)


#%%
a = 0.3
a

#%% [markdown]
# And if we add 1.2 we get 2.6:

#%%

a += 1.2


#%%


#%% [markdown]
# Well, almost.  It's not quite 2.6.  If you look at the 16th decimal place it's slightly off.
# 
# This can be disconcerting if you are unfamilliar with floating point math.  The reason for this is that to minimize memory usage and maximize performance, floating point numbers take the continuous number line and divide it in little chunks.  If your number doesn't quite line up with the chunks then there will be a small round-off error.
# 
# For example, the value stored in `a` isn't 1.4, it's exactly  
# `1.399999999999999911182158029987476766109466552734375`

#%%
print('{:.52}'.format(a))

#%% [markdown]
# These values are the same as double precision floating point numbers in C, which use 8 bytes, and the values are usually the same on 32 and 64 bit systems.
# 
# There's no way to specify that you want to use a different level of precision with your floating point arithmetic in standard Python, but if you use NumPy you can specify that you want to use single precision floating point numbers if you want to save memory or don't have high precision values.
#%% [markdown]
# ## Dynamically typed vs Strong typed 
# 
# Let's assign a value of a new type to the complex variable `a`. Then see what will happen. 

#%%
a = 1.4
type(a)

#%% [markdown]
# Wow! The assignment works (different from C/C++, java) and the type of the variable `a` is _dynamically_ changed from complex to the new type - string. So, Python is called __a dynamically typed language__. 
# 
# Then will the following code work? 

#%%
a = 'believe'
b = 2
c = 'see'
print(a, b, c)

#%% [markdown]
# It did not work. 
# Many operations in Python depend on their types. So, Python is called __a strongly typed language__
# 
# To fix the problem, we need to convert the type of the variable `b` to string. A built-in function `str()` converts the int type into a str type.

#%%
a = "amen"
b = 2
c = 'see'


#%% [markdown]
# # More Interactive Calculation
# 
# ## Arithmetic Operations
# 
# Let's use an example of a more involved numerical expression to get some familiarity with Python's operation syntax and order of operations.
#%% [markdown]
# * `1 - 2**3 * 4 - 56//7 + 89%98`
#%% [markdown]
# Looking at this, most of the operations should be straightforward, but `**` in Python indicates exponentiation, and `%` is the modulo (or remainder) operation.
# 
# Python's precedence order for operations is fairly standard (from highest to lowest):
# 
# * `( )` (parenthesis grouping)
# * `**`  (exponentiation)
# * `*`   (multiplication), `/`(true division), `//`(integer division), `%`(modulo)
# * `+`, `-` (addition, subtraction)
# 
# So walking through this expression, the exponentiation applys firs in a sub-expression `(2**3*4)`. 

#%%


#%% [markdown]
# So we now have `1 - 8 * 4 - 56//7 + 89%98`.
# 
# The next operations are multiplication, integer division // and modulo. Be caucious when there is a negative number in modulo operation. 

#%%
1 - 8 * 4 - 56//7 +89 % 98

#%% [markdown]
# and the expression simplifies to `1 - 32 + 8 + 89.`

#%%
print(1 - 32 - 8 + 89)
print(1 - 2**3 * 4 - 56//7 + 89%98) 

#%% [markdown]
# ## Simple Math Functions
# 
# There are a number of simple math functions that are available in Python, and we'll show a few here to give you an idea.
# 
# You can get the absolute value with `abs()`:

#%%
max = 100
type(max)
print(max)

#%% [markdown]
# You can round a floating point number to the nearest whole number using `round()`:

#%%
max(2,5,0,4,23,4,1,)
## 이건 max를 value로 사용해서 안됨

#%% [markdown]
# And you can use `max` and `min` to compute minimum and maximum values from a collection of values:
#%% [markdown]
# This example is a little more involved, what's happening is that we have two parts.
# 
# The first is the minimum of 10, -1, 4 and 3:

#%%
del max # 변수 max를 지우고
max(10, 100 ,3,-2) #function max로 사용하기

#%% [markdown]
# The second is the maximum of 0 and the result of the first part:

#%%
max(10, 20)

#%% [markdown]
# which is 0, and that's the result.
# 
# ## Overwriting Functions (!)
# 
# One thing that may be surprising if you have worked with other languages is that these functions can be overridden.  

#%%
max = 100


#%%
max(2, 5, 0, 4)                   #max(), min() are built-in functions

#%% [markdown]
# The name `max`, for example, has nothing special about it---it's not a keyword---and the name can be bound to an integer or any other value:

#%%


#%% [markdown]
# So now we've done this `max` is an integer:

#%%
max(10, 20)

#%% [markdown]
# and if we try to call `max(4, 5)` we'll get a type error:

#%%


#%% [markdown]
# because `max` is an integer now, not a function, and you can't call an integer.
# 
# In this case we can remove the local definition of `max` that is masking the built-in function by using the `del` statement:

#%%


#%% [markdown]
# If we check now, we'll see that `max` is back to being a function:

#%%


#%% [markdown]
# ## Type Conversion
# 
# Use the functions int(), float(), str(), chr() and ord() to convert between types (we will talk about functions next time). Note that `ord` stands for ordinal(서수) which is the number representing the position of c in the sequence of Unicode codepoints. 
# 
# For example, if you have a floating point number and want to cast it to an integer, use the `int()` function:

#%%
a = int(-1.92345)
type(a)
print(a)

#%% [markdown]
# which always __rounds towards 0.__
# 
# If you have an integer and you want to create a float, you can cast it up using the `float()` function:

#%%


#%% [markdown]
# If you add an integer to a floating point number, or a floating point number to a complex number, Python always gives you the result as the widest type, so int plus float gives you float:

#%%


#%% [markdown]
# ord('a') vs chr(97) 

#%%



#%%


#%% [markdown]
# 
#%% [markdown]
# #### Example:
# 
# Write a code that accepts an age from user and display the result as shown below. You may need to use `int()` and `input()`. 
# 
# ```
# What is your age?
# 7
# Your age becomes 8 tomorrow. 
# ```

#%%


#%% [markdown]
# ## In-Place Operations
# 
# In place versions of the standard arithmetic operations are possible using `+=`, `-=`, and so forth.  So for example:

#%%
b = 5
b += 0.5            # b = b + 0.5
b = b + 0.5
print(b)
b *= 2
b

#%% [markdown]
# ## Boolean Data Type
# 
# Python has a boolean data type, which has two values, `True` and `False`.  So we could set:

#%%
a = 3 > 4
type(a)

#%% [markdown]
# and see that the type of `q` is now `bool`:

#%%
q = True
p = False

if (q == True):
    print('q is true')
    
if (q):
    print('q is true')


#%%
a = 1 > 2
b = 3 > 2

#%% [markdown]
# Boolean values are most often created using expressions.  For example `1 < 0` is false, so if we do:

#%%


#%% [markdown]
# we see that `q` gets the value `False` as you might hope.
# 
# ## Comparison Operators
# Python's comparison operators are quite standard: `<`, `>`, `<=`, `>=`, `==` and `!=`.  So for example:

#%%
s = 1 > 2
type(s)


#%%
import numpy as np
np.arange(0, 5, 2)


#%%


#%% [markdown]
# One really slick feature of Python's comparisons are chained comparisons:

#%%


#%% [markdown]
# Effectively Python treats this expression as if it were:

#%%


#%% [markdown]
# ## Logical Operations
# 
# Comparisons can be combined using the logical operators `and`, `or` and `not`.  So for example:
# 
# 

#%%
5 < 10 and 10 < 20


#%%
5 < 10 or xxxxxx < 20


#%%
5 < 10 or 10 < 20


#%%
5 < 10 or 10 > 20

#%% [markdown]
# Python uses ["short-circuit" evaluation](http://en.wikipedia.org/wiki/Short-circuit_evaluation) of logical expressions if the value of subsequent terms can't affect the result.  So for example, in the expression:
#%% [markdown]
# #### Example:
# 
# What you expect from the following logical expression?
# 
# 1 > 4 and 5 < xx
# 
# 1. Name error
# 2. Type error
# - True 
# - False

#%%



#%%
1 > 4 or 5 < xx

#%% [markdown]
# since the first operand is `False`:

#%%


#%% [markdown]
# there is no way that the full expression could ever evalute to `True` and so Python skips the evaluation of the second operand, and returns `False` straight away.
# 
# Python's `or` operator works in a similar way:

#%%


#%% [markdown]
# and it will short-circuit evaluation if the first operand is `True`:

#%%


#%% [markdown]
# And finally, the `not` operation inverts the value of the argument:

#%%


#%% [markdown]
# ### Quiz
# Write a logical expression which evaluates an age to be true if the age is a teenage. The teenage means between 13 and 19 inclusively.

#%%
age = 10
# write a logical expression below to determine whether or not age is teen.

# age > 12 and age < 20

12 < age < 20

#%% [markdown]
# ### is_teen(age) function
# Replace `None` in `is_teen()` function with the logic expression you developed above.

#%%
def is_teen(age):
    return None


#%%
# test is_teen() 
for age in [9, 10, 11, 12, 15, 19, 20, 21]:
    None


#%%
for age in range(21):
    if (is_teen(age)): 
        print('The age', age, 'is a teen age')

#%% [markdown]
# ## Example: Leap year
# 
# A leap year is exactly divisible by 4 except for century years (years ending with 00). The century year is a leap year only if it is perfectly divisible by 400. For example,
# 
# ```
# 2017 is not a leap year
# 1900 is a not leap year
# 2012 is a leap year
# 2000 is a leap year
# ```

#%%
# Python program to check if the input year is a leap year or not

year = 2000

# To get year (integer input) from the user
# year = int(input("Enter a year: "))

if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))

#%% [markdown]
# ### Quiz
# Complete the following leap_year() function that returns `True` if `year` is a leap year, `False` otherwise. 

#%%
def leap_year(year):
    return None


#%%
# test leap_year()
for year in [100, 200, 1990, 2000, 2002, 2004, 2010, 2100]:
    None

#%% [markdown]
# ------------------
# 
# # Excercise 
# 
# ## 1. Given an integer number, print its last digit.

#%%
# Read an integer:
a = int(input("Enter an integer number: "))

# print the last digit of a which is an integer.
# for example, print 5 if 35, 6 if 6, 9 if 5679. 
x = a % 10
x


#%%
# Read an integer as a str:
a = input("Enter an integer number: ")

# print the last digit of a which is an integer.
# for example, print 5 if 35, 6 if 6, 9 if 5679. 

a[-1]

#%% [markdown]
# ## 2. Given a three-digit number. Find the sum of its digits.

#%%
# Read an integer:
a = int(input())
print(a)
# print the last digit of a which is an integer.
# for example, print 5 if 35, 6 if 6, 9 if 5679. 

#%% [markdown]
# ## 2. Given a three-digit number. Find the sum of its digits.

#%%
# Read an integer:
a = int(input())
print(a)
# for example, print 6 if a is 123, 18 if a is 369. 

sum = 0
while n:
    None
    
print(sum)

#%% [markdown]
# ## 3. Clock displays military time
# 
# The integer N given is the number of minutes that is passed since midnight. Display the hour and minute in military time. The program should print two numbers: the number of hours (between 0 and 23) and the number of minutes (between 0 and 59). For example, if N = 150, then 150 minutes have passed since midnight - i.e. now is 2:30 am. So the program should print 2:30.

#%%
# Read an integer:
a = int(input())
print(int(a/60),":",int(a%60))
# print 3:0 for 180, 7:24 for 444, 18:31 for 1111, 23:59 for 1439 

#%% [markdown]
# ## 4. Minimum of two numbers
# Given two integers, print the smaller value. Don't use min() function.
# 

#%%
##### Read an integer:
a = int(input('a:'))
b = int(input('b:'))

print("a:", a) if a > b else print("b:", b)

#%% [markdown]
# ## 5. Sign function
# 
# For the given integer x, print 1 if it's positive, -1 if it's negative, or 0 if it's equal to zero.
# Try to use the cascade `if-elif-else` for it.

#%%
# Read an integer:
x = int(input())

print("positive") if x >0 else print("negative") if(x < 0) else print("zero")

#%% [markdown]
# ## 6. Equal numbers
# 
# Given three integers, determine how many of them are equal to each other. The program must print one of these numbers: 3 (if all are the same), 2 (if two of them are equal to each other and the third is different) or 0 (if all numbers are different).

#%%
# Read an integer:
x = int(input("x:"))
y = int(input("y:"))
z = int(input("z:"))
result = 0
if x == y:
    result += 1
if x == z:
    result += 1
if y == z:
    result += 1
print(result)
    

#%% [markdown]
# --------
# __The LORD bless you and keep you.__ Numbers 6:24

