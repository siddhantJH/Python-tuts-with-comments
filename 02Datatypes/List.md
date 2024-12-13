<!-- we use square bracket to make a list  -->

>>> tea_varieties=["Black","Green","White"]
>>> tea_varieties
['Black', 'Green', 'White']
>>> print(tea_varieties)       # use print syntax as normal printing is not okay 
['Black', 'Green', 'White']

<!-- to access individual element we use the indexing rule -->
>>> print(tea_varieties[2])
White
>>> 


<!-- slicing and dicing and negative indesng also works here  -->
>>> print(tea_varieties[-1])
White
>>> tea_varieties[1:2]
['Green']
>>> tea_varieties[0:2]
['Black', 'Green']
>>> 
>>> 


<!-- List is mutable as well so we can change indivivual element without changeing the reference  -->
>>> tea_varieties[1]='purple'
>>> tea_varieties
['Black', 'purple', 'White']
>>> 

<!-- but if we try to use slicing syntax to assign the element that there are few cases that might arise-->
tea_variaties[1:2]='lemon'
>>> tea_varieties[1:2]='lemon'   //here lemon got treated as array issliye aik aikvalue individually mili hai 
>>> tea_varieties
['Black', 'l', 'e', 'm', 'o', 'n', 'White']
>>> 



<!-- to resolve this we do this-->
>>> tea_varieties[1:2]=["Lemon"]
>>> tea_varieties
['Black', 'Lemon', 'White']
>>> 



<!-- replacing two or mode element in the list usign slicing techniques  -->
>>> tea_varieties[1:3]=["Siddhant","Jha"]
>>> tea_varieties
['Black', 'Siddhant', 'Jha']
>>> 


>>> tea_varieties[1:1]   //we get empty as we have excluded the last index 1
[]


<!-- what if we try to assign something to 1:1 -->
>>> tea_varieties[1:1]=["pagla","boi"]
>>> tea_varieties
['Black', 'pagla', 'boi', 'Siddhant', 'Jha']     //aap zero se aage aae ho aur kuch nai kaha hai mujhe to i will insert it directly after 0th index 
>>> 



<!-- removing a part of the array -->
>>> tea_varieties[1:3]=[]   //insert nothing result into removing of the elmeent from that part 
>>> tea_varieties
['Black', 'Siddhant', 'Jha']



<!-- conditional loop iteratingf through the list in python-->
>>> for tea in tea_varieties:
...     print(tea,end="-")   //here we can gives second argument as well on how to move to next elemet 
... 
Black
Green
White
>>> 

<!-- using if else -->
>>> if "Black" in tea_var:
...     print("present")
... 
present
>>> 


<!-- adding element in the last-->
>>> tea_var.append("king")
>>> tea_var
['Black', 'Siddhant', 'Jha', 'king']       
<!-- we have .pop() method so it removes the last element and return it to you -->
<!-- we have .remove("king") only remove te king but it does not return it  -->
<!-- we have .insert(1,"elementname") insert the elmenetname at 1st index-->

if we assign the a new variable lets say tea_varieties_copy the tea_varieties then in that case 
the referece is copied,but if we want to create a entire new copy of the array then in that case we 
need to use the copy method 

tea_varieties_copy=tea_varieties.copy() //make new entry of the arrat and different referece is copied 



<!-- list comprehension-->
squared_nums=[x**2 for x in range(10)]  //1 se 10 tak excluding 10 har element uthao aur uspar 2 ka power lagao aur list me daldo
<!-- x ki value pe x**2 aaega  -->




### Detailed Notes on Python Lists

#### Basics of Python Lists
1. **Creating a List**:
   - Syntax: Use square brackets `[]` to create a list.
   ```python
   tea_varieties = ["Black", "Green", "White"]
   print(tea_varieties)  # Output: ['Black', 'Green', 'White']
   ```

2. **Accessing Elements**:
   - Lists allow access to individual elements using indexing.
   ```python
   print(tea_varieties[2])  # Output: White
   ```
   - Negative indexing is also supported:
   ```python
   print(tea_varieties[-1])  # Output: White
   ```

3. **Slicing**:
   - You can slice a list using the syntax `start:end`, where `start` is inclusive and `end` is exclusive.
   ```python
   print(tea_varieties[1:2])  # Output: ['Green']
   print(tea_varieties[0:2])  # Output: ['Black', 'Green']
   ```

---

#### Mutability of Lists

1. **Changing Elements**:
   - Lists are mutable, meaning individual elements can be updated.
   ```python
   tea_varieties[1] = 'purple'
   print(tea_varieties)  # Output: ['Black', 'purple', 'White']
   ```

2. **Using Slicing to Assign Elements**:
   - Direct assignment with slicing can behave differently based on the input.
   - Example where a string is assigned:
     ```python
     tea_varieties[1:2] = 'lemon'
     print(tea_varieties)  # Output: ['Black', 'l', 'e', 'm', 'o', 'n', 'White']
     ```
     *Each character in the string was treated as an individual element.*
   - To avoid this, use a list:
     ```python
     tea_varieties[1:2] = ["Lemon"]
     print(tea_varieties)  # Output: ['Black', 'Lemon', 'White']
     ```

3. **Replacing Multiple Elements**:
   - You can replace multiple elements using slicing.
   ```python
   tea_varieties[1:3] = ["Siddhant", "Jha"]
   print(tea_varieties)  # Output: ['Black', 'Siddhant', 'Jha']
   ```

4. **Inserting Elements Using Slicing**:
   - If you assign to a zero-length slice, elements are inserted without replacing existing ones.
   ```python
   tea_varieties[1:1] = ["pagla", "boi"]
   print(tea_varieties)  # Output: ['Black', 'pagla', 'boi', 'Siddhant', 'Jha']
   ```

5. **Removing Elements Using Slicing**:
   - Assigning an empty list to a slice removes those elements.
   ```python
   tea_varieties[1:3] = []
   print(tea_varieties)  # Output: ['Black', 'Siddhant', 'Jha']
   ```

---

#### Iterating Through Lists

1. **Simple Loop**:
   - Iterate through the list using a `for` loop.
   ```python
   for tea in tea_varieties:
       print(tea, end="-")  # Output: Black-Green-White-
   ```

2. **Conditional Check**:
   - Check if an element exists in the list.
   ```python
   if "Black" in tea_varieties:
       print("present")  # Output: present
   ```

---

#### Adding and Removing Elements

1. **Appending Elements**:
   - Use `.append()` to add an element to the end of the list.
   ```python
   tea_varieties.append("king")
   print(tea_varieties)  # Output: ['Black', 'Siddhant', 'Jha', 'king']
   ```

2. **Removing Elements**:
   - Use `.pop()` to remove and return the last element.
   ```python
   tea_varieties.pop()  # Removes 'king' and returns it.
   ```
   - Use `.remove()` to delete a specific element without returning it.
   ```python
   tea_varieties.remove("Jha")
   ```

3. **Inserting Elements**:
   - Use `.insert(index, element)` to insert an element at a specific position.
   ```python
   tea_varieties.insert(1, "elementname")
   ```

---

#### Copying Lists

1. **Reference Copy**:
   - Assigning a list to another variable copies the reference, not the data.
   ```python
   tea_varieties_copy = tea_varieties
   ```
   *Changes to one list will affect the other.*

2. **Creating a Separate Copy**:
   - Use `.copy()` to create a new list with a different reference.
   ```python
   tea_varieties_copy = tea_varieties.copy()
   ```

---

#### List Comprehension

1. **Generating Lists**:
   - List comprehensions allow concise creation of lists.
   ```python
   squared_nums = [x**2 for x in range(10)]
   print(squared_nums)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
   ```
   *Each element `x` from `range(10)` is squared and added to the list.*

---

This detailed note captures all the key concepts and examples you have provided about Python lists.

