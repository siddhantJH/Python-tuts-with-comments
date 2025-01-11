>>> chai_types={"Masala":"Spicy"}    //this is one field 
>>> 



<!-- to access a particular value -->
>>> chai_types["Masala"]   //use square bracket and key along with it 
'Spicy'


<!-- we could also use get function to get the value of spice -->
>>> chai_types.get("Masala")
'Spicy'
>>> chai_types.get("pagla")
>>> 


<!-- how to add a value in the dictionary-->
chai_types["Green"]="Fresh"


<!-- Iteration in the dictionary and how to do it efficiently -->
{'spiderman': 'AAA', 'valoratn': 'FPS'}   // we get only the keys 
>>> for game in game_types:
...     print(game)
... 
spiderman
valoratn
>>> 


<!-- printing the key and value both -->
>>> for game in game_types:
...     print(game,game_types[game])
... 
spiderman AAA
valoratn FPS


<!-- another way to get key and value -->
>>> for key,values in game_types.items():   //har aik item tha kar lana padega aur fir print karna padega, each item is a single key and value pair
...     print(key,values)
... 
spiderman AAA
valoratn FPS


<!-- check the availability of the key and value in the backend , but we can do that only using the key-->
>>> if "spiderman" in game_types:
...     print("Yes we have it")
... 
Yes we have it


<!-- we could also get the length of the dictionary  -->
print(len(game_types))    //each key value pair is counted as a new value so  it wil counted as 1 


<!-- in order to add the value in the dictionary-->
>>> game_types["metro"]="AAA"
>>> game_types
{'spiderman': 'AAA', 'valoratn': 'FPS', 'metro': 'AAA'}


<!-- what if we want to pop the item  form the dictionary -->
>>>game_types.pop("Metro")  when we try to pop the item usign the key, the whole item get popped and in return we get the value
>>> game_types.pop("metro")   //has to be case sensitive 
'AAA'
>>> game_types
{'spiderman': 'AAA', 'valoratn': 'FPS'}



<!-- another popping technique is pop item in which you do not need to pass any item , it directly pops the last element -->
>>> game_types.popitem()        //we get the key and value as a tuple in return, will have only 1 item 
('valoratn', 'FPS')


<!-- here also we can make a copy of the dictionary without using the same reference by using .copy() method
entirely new space is allocated in the memeory and then we assign the new reference to the variable-->



<!-- actually in dictionary also we can have a dictionary inside the dictionary but to use it we need key as well -->
game_types={
    "rockstar":{
        "gta":"AAA","mafia":"AAA"
    },
    "EA":{
        "fifa":"sports","battlefield":"AAA"
    }
}
>>> print(game_types)
{'rockstar': {'gta': 'AAA', 'mafia': 'AAA'}, 'EA': {'fifa': 'sports', 'battlefield': 'AAA'}}
>>> game_types["rockstar"]
{'gta': 'AAA', 'mafia': 'AAA'}
>>> game_types["rockstar"]["gta"]
'AAA'




<!-- squared numbers exmaple in dictionary as well -->
>>> squared_num={x:x**2 for x in range(6)}
>>> squared_num
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
>>> squared_num.clear()
>>> print(squared_num)
{}



<!-- first make key set than make value set -->
>>> keys=["Masala","Ginger","Lemon"]
>>> print(keys)
['Masala', 'Ginger', 'Lemon']
>>> default_value="delicious"
>>> new_dict=dict.fromkeys(keys,default_value)     //mention kis keys se nai values bannai hai 
>>> new_dict=dict.fromkeys(keys,default_value)  
>>> print(new_dict)
{'Masala': 'delicious', 'Ginger': 'delicious', 'Lemon': 'delicious'}

