# In python all the things are compared as a numbers only 
# Internally all the things are compared as number only 
# In python under the hood in all things C is used so the precision of c is carry forwarded to pyton also 
# >>> x=2
# >>> y=3
# >>> z=4
# >>> x+y
# 5
# >>> x+y*z   #Never use this sort of things in production as it puts burden in real world 
# 14
# x + (y  * z)   Will depend on precision so use parenthesis 
# >>> 40+2.23    Python supports high precsiion dono values ka data type same hona chahiye , dono mismatch data type nai hona chahiye dono same precision hona chahiye
# 42.23
# >>> float(40)+2.23 
# 42.23
# # >>> 'chai'+'code'  all operators supports overoading
# 'chaicode'
# >>> x,y,z   this is tuple data type helpfull in asigning more than one value etc
# (2, 3, 4)
# >>> x,y,z
# (2, 3, 4)
# >>> x+1
# 3
# >>> y*2
# 6
# >>> x+3
# 5
# now we want to know agar mai y ko divide karu two se to one remainder bachta hai 
# >>> y % 2 gives us remander
# >>> y ** 2 gives us power 
# >>> result = 1/3.0 //gives us the result in points and we can decide how much accuracy we need 0.333333333333333 
# if we want to format it 
# explain below concept in detail
# # >>> repr('chai')
# "'chai'"
# >>> print('chai')
# >>>chai/


# Comparison Operator 
# >>> 1<2
# True
# >>> 5.0==5.0
# True
# >>> 5.0==5
# True
# >>> 4.0!=5.0
# True
# >>> x=2
# >>> y=3
# >>> z=4
# >>> x,y,z
# (2, 3, 4)
# >>> x<y<z
# True
# >>> 1 == 2 < 3     changed internaly as 1==2 and 2 < 3 
# False
# >>> 



# third party library for mathematics fucntion 
# >>> import math 
# >>> math.floor(3.14) //gives us closest number down to the nearest integer 
# 3
# >>> math.ceil(3.14) //gives us the closest value up the nearesst inteeger 
# 4
# >>> math.trunc(2.8) //goes towars zero
# 2
# >>> math.trunc(-2.8)
# -2
# >>> 9999999999999999999999999999+1.23    this can be resolved using some lobrary 
# 1e+28
# >>> 9999999999999999999999999999+2     this can be resollved easily using the normal addition and subs and python can handle it easily 
# 10000000000000000000000000001

# >>> 0o20   these are normal octal numbers 
# 16
# >>>0xff these are octall as well 
# >>>oct(64) //convert decimal to octal
# >>>bin(64) //convert to binary
# >>>hexa(64) //conver to hexa
# >>>int('64',8) //convert 64 to base 8,first parameter is string



# bitwise operator 
# x=1
# x<<2  //left shift by 2 bits
# x>>2 //right shift by 2 bits




# ramndom
# >>> import random 
# >>> random.random()   random number between 0 and 1
# 0.9383063118701768
# >>> random.randint(1,100)  random number between 1 to 99 excluding 100
# 76
# >>> can use the above concept with the list as well 
# >>> l1=['lemon','masala','ginger','mint']
# >>> random.choice(l1)
# 'masala'
# >>> random.choice(l1)
# 'lemon'
# >>> random.choice(l1)
# 'masala'
# >>> random.choice(l1)
# can shuffle the things as well 
#>>> l1=['lemon','masala','ginder','mint']
# >>> random.shuffle(l1)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'random' is not defined. Did you forget to import 'random'?
# >>> import random
# >>> random.shuffle(l1)
# >>> l1
# ['masala', 'ginder', 'lemon', 'mint']
# >>> 



# below is the case of decimal precision so import 
# # >>> 0.1+0.1+0.4
# 0.6000000000000001
# >>> 0.1+0.1+0.1
# 0.30000000000000004
# >>> 0.1+0.1+0.1 - 0.3
# 5.551115123125783e-17
# >>> (0.1+0.1+0.1) - 0.3
# 5.551115123125783e-17   //these are known problems and belowe is the knowns soltons for these known problems


# from decimal import Decimal 
# Decimal('0.1')
# >>> Decimal('0.1')+Decimal('0.1')+Decimal('0.1')-Decimal('0.3')  
# Decimal('0.0') 
# >>> myFra=Fraction(2,7)    2/7
# >>> myFra
# Fraction(2, 7)



# perform set operation 
# >>> setone={1,2,3}
# >>> setone
# {1, 2, 3}
# >>> settwo= {2,3,4}
# >>> setone and settwo
# {2, 3, 4}
# >>> setone or settwo
# {1, 2, 3}
# >>> setone & settwo
# {2, 3}
# >>> setone | settwo
# {1, 2, 3, 4}
# >>> >>> setone-{1,2,3}   
# set()         //we get result as empty set and not empty parethesis as empty parenthesis are dictionary



# >>> type({})
# <class 'dict'>




# ṭype(True)   #It is treated as boolean
# >>> type(True)
# <class 'bool'>



# >>> True is 1       both have same value but difference reference in the memory 
# <stdin>:1: SyntaxWarning: "is" with 'int' literal. Did you mean "=="?
# False



# >>> True is 1
# <stdin>:1: SyntaxWarning: "is" with 'int' literal. Did you mean "=="?
# False
# >>> True+4
# 5


# Detailed notes of ebove 

# Here's a detailed note covering all the concepts mentioned in the above prompt:

# ---

# ## **Python Concepts in Detail**

# ### **Basic Arithmetic Operations**
# 1. **Addition and Multiplication**:
#    - Example:  
#      ```python
#      x = 2
#      y = 3
#      z = 4
#      x + y  # Output: 5
#      x + y * z  # Output: 14 (evaluates as x + (y * z) due to operator precedence)
#      ```

#    - **Production Advice**: Avoid expressions like `x + y * z` without parentheses in production to maintain clarity and precision. Use explicit parentheses: `x + (y * z)`.

# 2. **Floating-Point Arithmetic**:
#    - Python supports high precision for calculations:
#      ```python
#      40 + 2.23  # Output: 42.23
#      float(40) + 2.23  # Output: 42.23
#      ```

# 3. **String Concatenation**:
#    - Strings can be concatenated using the `+` operator:
#      ```python
#      'chai' + 'code'  # Output: 'chaicode'
#      ```

# 4. **Tuple Assignment**:
#    - Tuples are used for assigning multiple values:
#      ```python
#      x, y, z = 2, 3, 4
#      x, y, z  # Output: (2, 3, 4)
#      ```

# ### **Modulus and Exponentiation**
# 1. Modulus (`%`): Returns the remainder.
#    ```python
#    y % 2  # Output: 1
#    ```
# 2. Exponentiation (`**`): Raises a number to a power.
#    ```python
#    y ** 2  # Output: 9
#    ```

# ### **Formatting and Representations**
# 1. **Formatting Numbers**:
#    - Floating-point precision:
#      ```python
#      result = 1 / 3.0  # Output: 0.3333333333333333
#      ```
#    - Use string formatting for better control:
#      ```python
#      formatted = f"{result:.2f}"  # Output: '0.33'
#      ```

# 2. **Representation**:
#    - `repr()`: Provides a string representation of an object suitable for debugging.
#      ```python
#      repr('chai')  # Output: "'chai'"
#      ```

# ### **Comparison Operators**
# 1. Python supports common comparison operators:
#    ```python
#    1 < 2  # True
#    5.0 == 5.0  # True
#    5.0 == 5  # True
#    4.0 != 5.0  # True
#    ```

# 2. Chained Comparisons:
#    ```python
#    x = 2
#    y = 3
#    z = 4
#    x < y < z  # True
#    1 == 2 < 3  # False (evaluates as (1 == 2) and (2 < 3))
#    ```

# ### **Math Library**
# - **Math Functions**:
#   ```python
#   import math
#   math.floor(3.14)  # Output: 3
#   math.ceil(3.14)   # Output: 4
#   math.trunc(2.8)   # Output: 2
#   math.trunc(-2.8)  # Output: -2
#   ```

# - Handling Large Numbers:
#   ```python
#   9999999999999999999999999999 + 2  # Python handles large integers
#   ```

# ### **Number Systems**
# - Octal, Binary, Hexadecimal Conversions:
#   ```python
#   oct(64)  # Output: '0o100'
#   bin(64)  # Output: '0b1000000'
#   hex(64)  # Output: '0x40'
#   int('64', 8)  # Converts '64' in base 8 to decimal
#   ```

# ### **Bitwise Operators**
# - Bitwise shifts:
#   ```python
#   x = 1
#   x << 2  # Left shift by 2 bits: Output: 4
#   x >> 2  # Right shift by 2 bits: Output: 0
#   ```

# ### **Random Module**
# - Random Number Generation:
#   ```python
#   import random
#   random.random()  # Output: Random float between 0 and 1
#   random.randint(1, 100)  # Random integer between 1 and 99
#   ```

# - Random List Operations:
#   ```python
#   l1 = ['lemon', 'masala', 'ginger', 'mint']
#   random.choice(l1)  # Randomly picks an element from the list
#   random.shuffle(l1)  # Shuffles the list
#   ```

# ### **Decimal and Fraction Precision**
# - **Decimal Module**:
#   ```python
#   from decimal import Decimal
#   Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')  # Output: Decimal('0.0')
#   ```

# - **Fractions Module**:
#   ```python
#   from fractions import Fraction
#   myFra = Fraction(2, 7)
#   ```

# ### **Set Operations**
# - Basic Operations:
#   ```python
#   setone = {1, 2, 3}
#   settwo = {2, 3, 4}
#   setone & settwo  # Intersection: {2, 3}
#   setone | settwo  # Union: {1, 2, 3, 4}
#   setone - settwo  # Difference: {1}
#   ```

# ### **Data Types**
# 1. **Boolean**:
#    ```python
#    type(True)  # <class 'bool'>
#    True + 4  # Output: 5
#    ```

# 2. **Empty Set vs Dictionary**:
#    ```python
#    type({})  # Output: <class 'dict'>
#    ```

# ### **Known Floating-Point Issues**
# - Precision errors in floating-point arithmetic:
#   ```python
#   0.1 + 0.1 + 0.1 - 0.3  # Output: 5.551115123125783e-17
#   ```

# - Solutions using `Decimal`:
#   ```python
#   from decimal import Decimal
#   Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')  # Output: Decimal('0.0')
#   ```

# ---

# This note provides a comprehensive breakdown of all the key concepts mentioned in the prompt.