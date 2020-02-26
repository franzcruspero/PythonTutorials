# from random import random

# def coin_flip():
#     if random(

#     ) > 0.5:
#         return "heads"
#     else:
#         return "tails"

# print(coin_flip())



def list_manipulation(list, command, location, val):
    if command == "remove":
        if location == "end":
            return list.pop()
        else:
            return list.pop(0)
    else:
        if location == "end":
            return list.append(val)
        else:
            return list.insert(0, val)

print(list_manipulation(["1", "2", "3"], "add", "beginning", 20))