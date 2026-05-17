list_ = set(["My", "Focus", "Never", "Ceases", 2, "Amuse", "Me", 4, "Ever", 2])
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

print(decorator(money_maker)())