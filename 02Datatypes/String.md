""""""
''
""


# extracting first char 
# >>> chai="masala chai"
# >>> chai
# 'masala chai'
# >>> first_char = chai
# >>> first_char=chai[0]
# >>> firstchar
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'firstchar' is not defined. Did you mean: 'first_char'?
# >>> first_char
# 'm'
# >>> 



# extracting a word from a string 
# >>> slice_chai=chai[0:6]
# >>> slice_chai
# ''masala'


# >>> num_list="012345678"
# >>> num_list[:]
# '012345678'
# >>> num_list[3:]
# '345678'
# >>> num_list[:7]
# '0123456'
# >>> num_list[:20]
# '012345678'
# >>> num_list[:20:2]   //last parameter is number of hops 
# '02468'


# most of the string which we use are unicode string means and other string function 
# >>> chai="masala chai"
# >>> chai
# 'masala chai'
# >>> print(chai)
# masala chai
# >>> print(chai.lower)
# <built-in method lower of str object at 0x7c5f086e9770>
# >>> chai = 'masala chai'
# >>> chai
# 'masala chai'
# >>> print(chai.lower())
# masala chai
# >>> print(chai.upper())
# MASALA CHAI
# >>> chai = "    masala chai"
# >>> chai
# '    masala chai'
# >>> print(chai.strip())
# masala chai
# >>> 


# replace the word in the string 
# chai="Lemon chai
#print(chai)
# >>> chai = "Lemon Chai"
# >>> print(chai.replace("Lemon","Ginger"))
# Ginger Chai   //original chai did not change vo hamesha se same hi rahega as string is immutable 
# >>>  chai
# 'Lemon Chai'
# >>> 


# split using the , operator 
# >>> chai = "Lemon , Ginger, Masala, Mint"
# >>> chai
# 'Lemon , Ginger, Masala, Mint'
# >>> l1=chai.split(',')
# >>> l1
# ['Lemon ', ' Ginger', ' Masala', ' Mint']
# >>> l1=chai.split(', ')
# >>> l1
# ['Lemon ', 'Ginger', 'Masala', 'Mint']
# >>> 



# find at which location a word has came 
# >>> cup = "ginger tea"
# >>> print(cup.find("tea"))
# 7
# >>> 



# count the number of occurences of teh chai word in a string 
# chai = "Masala chai chai chai"
# print(chai.count("Chai"))


# PLace Holders these are called placeholder and we can add variables in it 
# >>> chai_type="Masala"
# >>> chai_type
# 'Masala'
# >>> quantity=2
# >>> Order= "I ordered {} cups of {} chai"
# >>> Order
# 'I ordered {} cups of {} chai'
# >>> 


# replacing placeholders using the word 
# >>> chai_type="Masala"
# >>> chai_type
# 'Masala'
# >>> quantity=2
# >>> Order= "I ordered {} cups of {} chai"
# >>> Order
# 'I ordered {} cups of {} chai'
# >>> print(Order.format(quantity,chai_type))
# I ordered 2 cups of Masala chai
# >>> 


# List to string 
# >>> chai_variety = ["Lemon","Masala","Ginger"]
# >>> chai_variety
# ['Lemon', 'Masala', 'Ginger']
# >>> print("".join(chai_variety)) with no spaces
# LemonMasalaGinger
#>>> print(" ".join(chai_variety))
# Lemon Masala Ginger
# >>> print(", ".join(chai_variety))
# Lemon, Masala, Ginger




# finding the length of the string 
# >>> chai="Masala chai"
# >>> print(len(chai))
# 11



# iterate through the letters int the stirng 


# ignoring specific character in the string , helps when we want to pass the windows path to some function or anything 
# >>> chai="He said,\"Masala chai is awesome\" "
# >>> chai
# 'He said,"Masala chai is awesome" '
# >>> 


# how to not ignore \n
# >>> chai = r"Masala\nchai"
# >>> chai
# 'Masala\\nchai'
# >>> print(chai)
# Masala\nchai
# >>> print(chai)
# Masala\nchai
# >>> chai=r"c:\user\pwd\"
#   File "<stdin>", line 1
#     chai=r"c:\user\pwd\"     //when we use slash in the string just remve the last slash and then we font need to put // // in between 
#          ^
# SyntaxError: unterminated string literal (detected at line 1)
# >>> chai
# 'Masala\\nchai'
# >>> chai=r"c:\\user\\pwd\\"
# >>> chai
# 'c:\\\\user\\\\pwd\\\\'
# >>> print(chai)
# c:\\user\\pwd\\
# >>> 



# containment string true/fasle 
# >>> chai="Masala chai"
# >>> print(chai in chai)
# True
# >>> 








### Detailed Notes on String Manipulations in Python

# Python strings are an essential part of programming. This document outlines key string operations and manipulations with practical examples.

# ---

# ### **1. Extracting First Character**
# To access the first character of a string:
# ```python
# chai = "masala chai"
# first_char = chai[0]  # 'm'
# ```

# #### **Error Example**
# If you mistype a variable name, Python will raise a `NameError`:
# ```python
# firstchar  # NameError: name 'firstchar' is not defined. Did you mean: 'first_char'?
# ```

# ---

# ### **2. Extracting a Substring (Slicing)**
# Slicing extracts portions of strings using `[start:stop]` or `[start:stop:step]` syntax:
# ```python
# chai = "masala chai"
# slice_chai = chai[0:6]  # 'masala'
# ```

# #### **Slicing Examples**
# - **Full String:** `num_list[:]` → `'012345678'`
# - **From Index:** `num_list[3:]` → `'345678'`
# - **Up to Index:** `num_list[:7]` → `'0123456'`
# - **Out-of-Bounds Index:** `num_list[:20]` → `'012345678'` (No error; stops at the string’s length)
# - **Stepped Slicing:** `num_list[:20:2]` → `'02468'` (Every second character)

# ---

# ### **3. Unicode Strings**
# Strings in Python are Unicode by default, allowing them to handle a vast range of characters.

# #### **Examples**
# ```python
# chai = "masala chai"
# print(chai.lower())  # 'masala chai' (lowercased)
# print(chai.upper())  # 'MASALA CHAI' (uppercased)

# # Removing whitespace:
# chai = "    masala chai"
# print(chai.strip())  # 'masala chai'
# ```

# ---

# ### **4. Replace Words in Strings**
# String replacement uses `.replace()`:
# ```python
# chai = "Lemon Chai"
# print(chai.replace("Lemon", "Ginger"))  # 'Ginger Chai'
# # Note: Strings are immutable; the original remains unchanged.
# chai  # 'Lemon Chai'
# ```

# ---

# ### **5. Splitting Strings**
# Split a string into a list using `.split(separator)`:
# ```python
# chai = "Lemon, Ginger, Masala, Mint"
# l1 = chai.split(", ")  # ['Lemon', 'Ginger', 'Masala', 'Mint']
# ```

# ---

# ### **6. Finding Substring Index**
# The `.find()` method returns the index of the first occurrence of a substring, or `-1` if not found:
# ```python
# cup = "ginger tea"
# print(cup.find("tea"))  # 7
# ```

# ---

# ### **7. Counting Substring Occurrences**
# The `.count()` method counts how many times a substring appears:
# ```python
# chai = "Masala chai chai chai"
# print(chai.count("chai"))  # 3
# ```

# ---

# ### **8. Placeholders (String Formatting)**
# Placeholders allow inserting variables into strings:
# ```python
# chai_type = "Masala"
# quantity = 2
# order = "I ordered {} cups of {} chai"
# print(order.format(quantity, chai_type))  # 'I ordered 2 cups of Masala chai'
# ```

# ---

# ### **9. Joining Lists into Strings**
# The `.join()` method concatenates list elements into a single string:
# ```python
# chai_variety = ["Lemon", "Masala", "Ginger"]
# print("".join(chai_variety))  # 'LemonMasalaGinger' (no spaces)
# print(" ".join(chai_variety))  # 'Lemon Masala Ginger' (with spaces)
# print(", ".join(chai_variety))  # 'Lemon, Masala, Ginger'
# ```

# ---

# ### **10. String Length**
# The `len()` function returns the total number of characters:
# ```python
# chai = "Masala chai"
# print(len(chai))  # 11
# ```

# ---

# ### **11. Iterating Through a String**
# Strings are iterable:
# ```python
# for letter in "Masala chai":
#     print(letter)
# ```

# ---

# ### **12. Escaping Characters**
# Escape characters allow including special characters in strings:
# ```python
# chai = 'He said, "Masala chai is awesome"'
# print(chai)  # 'He said, "Masala chai is awesome"'
# ```

# ---

# ### **13. Raw Strings**
# Raw strings (`r"string"`) treat backslashes as literals:
# ```python
# chai = r"Masala\nchai"
# print(chai)  # 'Masala\nchai'

# # Windows paths:
# chai = r"c:\\user\\pwd\\"  # Avoids errors caused by single backslashes
# print(chai)  # 'c:\\user\\pwd\\'
# ```

# ---

# ### **14. String Containment**
# The `in` keyword checks if a substring exists:
# ```python
# chai = "Masala chai"
# print("chai" in chai)  # True
# ```

# ---

# ### **Key Notes**
# - **Immutability:** Strings are immutable. Any modification creates a new string.
# - **Error Handling:** Typing errors in variable names can lead to runtime errors.
# - **Unicode Strings:** Python strings can handle diverse characters globally.
# - **Efficiency:** Use slicing, `.join()`, and `.format()` for efficient operations.

# These examples highlight Python’s flexibility and powerful string handling capabilities.