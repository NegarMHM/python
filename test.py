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




menu = {"tea" , "coffee" , "beer"}
select = ("tea")
if "tea" in menu:
    print("yes, 'tea' is in menu")
elif "tea" not in menu:
    print("no, 'tea' not in menu")







menu = {"tea" , "coffee" , "beer"}
select = ("water")
if "water" in menu:
    print("yes, 'water' in menu")
elif "water" not in menu:
    print("no, 'water' not in menu")





menu = {"tea" , "coffee" , "beer"}
select = ("tea" , "coffee")
print(select)




menu = {"tea" , "coffee" , "beer"}
(one , two , three) = menu
(four , five , six) = menu
(seven , eight , nine) = menu
(ten , eleven , twelve) = menu
print(one)
print(five)
print(nine)






menu = {"tea" , "coffee" , "beer"}
print(len(menu))












