# def word_evaluator(word):
#     for x in list_: 
#         if type(x) == int: 
#             indx = list_.index(x)
#             list_.remove(index)
#     return list_

# print(word_evaluator(list_))

# def try_except(value): 
#     try: 
#         return value * 6
#     except: 
#         print("TypeError: The value provided is not a number")
#     finally: 
#         print("Coding is Fun")

# print(try_except(45))

dog = "Lulu"

match(dog): 
    case("Bosco"): 
        owner = "Cooked"
    case("Scooby"): 
        owner = "Slightly Cooked."
    case("Rex"):
        owner = "Safe"
    case _: 
        owner = "Non-existent"


dict_map = {
    "Bosco": "Cooked", 
    "Scooby": "Slightly Cooked", 
    "Rex": "Safe", 
    "Cuddly": "Snuggling", 
}

owner = dict_map.get(dog, "Still a devastation anyway!")


def decorator(func):
    def wrapper(): 
        "I am the wrapper function. I just return stuff"
        return func()
    return wrapper

def money_maker(): 
    return "How much can you really make if you are pragmatic enough!"

# print(decorator(money_maker)())
# set_ = set(["Nintendo", "Collo", "Luka", 2, 4, 5])
# print(set_["Collo"])

list_ = ["My", "Focus", "Never", "Ceases", "Amuse", "Me", "Ever"]
# numbers = [print(i) for i in list_ if "e" in i]
# print(numbers)

list_2 = [("Howard", 5), ("Collins", 1), ("Mercy", 3), ("Luka", 2), ("Flynn", 4), ("Tracy", 7), ("Mercury", 9),]
def sort_value(tuple_value):
    return tuple_value[1]
list_2.sort(key=sort_value)
# print(list_2)
word_1 = "Where's the love?"
word_2 = "Where is the love, huh"

print(set(word_1) - set(word_2))