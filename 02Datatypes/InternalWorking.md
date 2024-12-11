# Internal Working of Memory Management in Python

## Memory Management Overview

In Python, memory management is handled through dynamic memory allocation, reference counting, and garbage collection. Python’s approach ensures efficient usage of memory while abstracting the complexities from the developer.

### Memory Allocation
- When a variable is created, Python allocates a memory block to store its value. For example, if you store the number `10`, a memory block is allocated for `10`.
- The datatype is associated with the memory location, not the variable name. This means that variables are merely references to objects in memory.

```python
score = 10
another_score = score  # `another_score` now points to the same memory reference as `score`.
```

### Reference Counting
- Python uses a reference counting mechanism to keep track of how many references exist for a particular object in memory.
- You can use the `sys.getrefcount()` function to check the number of references to an object.

```python
import sys

sys.getrefcount(10)  # Returns the count of references to the integer 10.
sys.getrefcount("hi")  # Returns the count of references to the string "hi".
```

### Garbage Collection
- When an object’s reference count drops to zero, it means no variable is pointing to it, and it is eligible for garbage collection.
- Python’s garbage collector removes such objects to free up memory.

```python
x = 5
x = None  # The reference to the integer 5 is removed. Garbage collection will clean it up eventually.
```

### Late Garbage Collection
- To optimize performance, Python delays the garbage collection of frequently used objects like numbers and strings.

```python
import sys

a = 3
a = 'example'
print(sys.getrefcount(3))  # A high reference count shows frequent reuse of the integer 3.
```

## Mutable and Immutable Objects

### Immutable Objects
- Numbers, strings, and tuples are immutable. When their value changes, a new memory block is created.

```python
a = 5
a = a + 3  # A new memory location is allocated for the value 8.
```

### Mutable Objects
- Lists, dictionaries, and sets are mutable. Their values can be modified in place without changing their memory reference.

```python
myListOne = [1, 2, 3]
myListTwo = myListOne  # Both variables point to the same memory reference.
myListOne[0] = 44
print(myListTwo)  # Output: [44, 2, 3]
```

## Memory Referencing Examples

### Assigning New References
- Assigning a new value to a variable creates a new reference for mutable objects.

```python
p1 = [1, 2, 3]
p2 = p1  # Both point to the same reference.
p2 = [1, 2, 3]  # A new reference is created for `p2`.
```

### Slicing Creates a Copy
- Using slicing creates a new copy of the list, thus avoiding shared references.

```python
h1 = [1, 2, 3]
h2 = h1[:]
h1[0] = 44
print(h1)  # Output: [44, 2, 3]
print(h2)  # Output: [1, 2, 3]
```

### Shallow vs. Deep Copy
- A shallow copy (e.g., `copy.copy`) copies only the outer object, while a deep copy (e.g., `copy.deepcopy`) recursively copies all objects.

```python
import copy

h1 = [1, 2, [3, 4]]
h2 = copy.copy(h1)  # Shallow copy
h3 = copy.deepcopy(h1)  # Deep copy
h1[2][0] = 99
print(h1)  # Output: [1, 2, [99, 4]]
print(h2)  # Output: [1, 2, [99, 4]]
print(h3)  # Output: [1, 2, [3, 4]]
```

## Comparison of References

### Equality (`==`) vs. Identity (`is`)
- `==` checks if the values are equal.
- `is` checks if two variables reference the same memory location.

```python
n = [1, 2, 3]
m = n
print(m == n)  # Output: True
print(m is n)  # Output: True

m = [1, 2, 3]
print(m == n)  # Output: True
print(m is n)  # Output: False
```

### Practical Implications
- Be cautious when working with mutable objects and references to avoid unintended side effects. Slicing or using `copy`/`deepcopy` can help create independent copies when needed.

## Key Takeaways
- Memory management in Python relies on reference counting and garbage collection.
- Immutable objects always create new references when modified, while mutable objects can change in place.
- Use slicing or `copy`/`deepcopy` to create independent copies of mutable objects.
- Use `==` and `is` appropriately to differentiate between value equality and reference identity.













<!-- Internal working of the python -->
<!-- 
In python we can manage memory as well , apart from grabage colletion 
In memory block we added the text [10] now it is created when someone ased for this reference 
score=10, a_score=score //since python optimises it gives the same reference to it 
,suppose we take another variable id=5 , now suppose the use of id is not anymore 
so we remove it , so no one is now pointing to 5 so garbage colletion comes in the picture 
and removes the unpointed 5 in the memory, how to count the number of references in the memory 
ref_count //this keeps the count of number of refernces in the memory, memory reference count


<!-- datatype is given to memory location and not the variable -->
<!-- datatype is given to the memory type -->


<!-- >>> sys.getrefcount(24601)
3
>>> sys.getrefcount('hi')
 -->


<!-- Late garbage collection to save time in future 
>>> a=3
>>> a
3
>>> a = 'chaiaurcode'
>>> a
'chaiaurcode'
>>> import sys
>>> sys.getrefcount(3)
4294967295
>>> 

//python does not immediatly collects the number or string as these are used frquently
 -->


<!-- 
>>> a
5
>>> b
2
>>> a=a+3
>>> a
8
>>> 


<-- the reference where a points to gets incremented by 3 -->
<!-- a=a+2 first refernce is resolve a=5+2 goes to calculation 
then new memory location is relocated for 7 and then a points to 7 and old 5 gets delete(not immediately) -->



<!-- myListOne=[1,2,3] -->
<!-- >>> myListOne=[1,2,3]
>>> myListTwo=myListOne
>>>  
first list reference is created then myListOne points to it and then we have MyListTwo,
it points to same reference , now if we try to change value of myListOne
will it affect myListTwo?? no new referece for myListone is created with modified value, but if we try to change a particular value using the 
index notation then myListTwo will get affected again same result as list as myListTwo is assigned the same reference 

-->

<!-- variant one  -->
<!-- 
>>> l1=[1,2,3]
>>> l2=l1
>>> l1
[1, 2, 3]
>>> l2
[1, 2, 3]
>>> l1[0]=44
>>> l1
[44, 2, 3]
>>> l2
[44, 2, 3]
>>> 
 -->



 <!-- variant two -->
 <!-- 
 
 >>> p1= [1,2,3]
>>> p2=[1,2,3]
>>> p1[0]=44
>>> p1
[44, 2, 3]
>>> p2
[1, 2, 3]
>>> 

  -->



  <!-- p1=[1,2,3]
  p2=p1
  p2=[1,2,3] -->
  <!-- now here we might think that p2 will get assigned the same reference 
  but as we know that list is mutable so if we change p1 now then p1 and p2 is different , change ho sakta hai to different reference do -->


  <!-- h1 = [1,2,3] -->
  <!-- h2=h1[0:]
  //in this case we create entirely new copy for h2 not referencing it , slicing creates the copy-->



  <!-- 
  >>> h2=h1[0:]
>>> h1
[1, 2, 3]
>>> h2
[1, 2, 3]
>>> h1[0]=44
>>> h1
[44, 2, 3]
>>> h2
[1, 2, 3]
>>> 
   -->



   <!-- 
   >>> import copy
>>> h1=[1,2,3]
>>> h2= copy.copy(h1)
>>> j1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'j1' is not defined. Did you mean: 'h1'?
>>> h1
[1, 2, 3]
>>> h2
[1, 2, 3]
>>> 
   <!-- this will not copy the list present inside the list, so we use deepcopy  -->




<!-- 
>>> n=[1,2,3]
>>> m=n
>>> m
[1, 2, 3]
>>> n
[1, 2, 3]
>>> m==n
True
>>> 
 -->



 <!-- 
 >>> n=[1,2,3]
>>> m=n
>>> m
[1, 2, 3]
>>> n
[1, 2, 3]
>>> m is n  //checkes memory refernce 
True
>>>  -->




<!-- 
>>> n=[1,2,3]
>>> m=n
>>> m
[1, 2, 3]
>>> n
[1, 2, 3]
>>> m==n
True
>>> m=[1,2,3]
>>> m==n
True
>>> m is n
False
>>> 
 -->