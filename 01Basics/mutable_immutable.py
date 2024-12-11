# Mutable Data types are those that can be changed.
# Immutable data types are those that cannot be changed.
# In python everything are called as object and most of the data types are immutable 

# Open shell 
# now in memory supose you want a space variable where you need to store the 
# username, creates a space in memory we store siddhant in it "siddhant"
# >>> username = "siddhant"   
# >>> username
# 'siddhant'
# >>> username = "rohan"
# >>> username
# 'rohan'
# >>> 


# the above behavior is odd as we considered the variable as immutable //this string is immutable according to what we have studied
# so we came across a problem, now lets explore it a little bit 
# >>> x =  10
# >>> y = x
# >>> x
# 10
# >>> y
# 10
# >>>  x = 15
#   File "<stdin>", line 1
#     x = 15
# IndentationError: unexpected indent
# >>>  x = 15
#   File "<stdin>", line 1
#     x = 15
# IndentationError: unexpected indent
# >>> x = 15
# >>> y
# 10
# >>> x
# 15
# >>> 



