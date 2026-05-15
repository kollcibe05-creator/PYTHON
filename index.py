# import ipdb
list_ = set(["My", "Focus", "Never", "Ceases", 2, "Amuse", "Me", 4, "Ever", 2])
#  words = for x in list_: 
#     if type(x) == int: 
#         indx = list_.index(x)
#         list_.remove(index)
#     return list_

dict_ = dict(name="Collo", age=20, kilos=56, State="Focused")
# print(dict_)
def tracing_value(x):
    print("We are about to start")
    while x < 5:
        print(x, "Not yet 5")
        # ipdb.set_trace()
        x+=1
    print("Done!")

# print(tracing_value(0))

outside_the_function = "Hey, I'm outside."
print(outside_the_function)
def change_inside_to_outside():
        outside_the_function = "Change to inside"
        return outside_the_function

print(change_inside_to_outside())
print(outside_the_function)