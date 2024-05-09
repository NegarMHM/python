

"""
definition of three item
type of items
brand items
definition of menu
and finally print the menu
"""

tea = {
    "type": "tea",
    "brand1": "golestan",
    "brand2": "shahrzad",
    "brand3": "tabiat",
}
coffee = {
    "type": "coffee",
    "brand1": "starbucks",
    "brand2": "lavazza",
    "brand3": "nescafe",
    }
beer = {
    "type": "beer",
    "brand1": "albrau",
    "brand2": "tuborg",
    "brand3": "carlton draught",
}
menu = {
    "tea" : tea,
    "coffee" : coffee,
    "beer" : beer,
}
print(menu)







"""
definition of menu
select an item
if item is availabel in the menu
printing is availabel,
if it's not in the menu
print it,it is not availabel
"""

menu = {"tea" , "coffee" , "beer"}
select = ("tea")
if "tea" in menu:
    print("yes, 'tea' is in menu")
elif "tea" not in menu:
    print("no, 'tea' not in menu")







"""
definition of menu
select on item
if item is availabel in the menu
printing is availabel,
if it's not in the menu
print it,it is not availabel
"""

menu = {"tea" , "coffee" , "beer"}
select = ("water")
if "water" in menu:
    print("yes, 'water' in menu")
elif "water" not in menu:
    print("no, 'water' not in menu")








#definition of menu,select two item in the menu,and print or display selected item

menu = {"tea" , "coffee" , "beer"}
select = ("tea" , "coffee")
print(select)









"""
difinition of menu
line two to five ,the number of selected items equal to the menu,
and finally print the number of items
"""

menu = {"tea" , "coffee" , "beer"}
(one , two , three) = menu
(four , five , six) = menu
(seven , eight , nine) = menu
(ten , eleven , twelve) = menu
print(one)
print(five)
print(nine)







#definition of menu,print the number of menu items

menu = {"tea" , "coffee" , "beer"}
print(len(menu))












