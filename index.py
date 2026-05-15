list_ = set(["My", "Focus", "Never", "Ceases", 2, "Amuse", "Me", 4, "Ever", 2])
def word_evaluator(word):
    for x in list_: 
        if type(x) == int: 
            indx = list_.index(x)
            list_.remove(index)
    return list_

print(word_evaluator(list_))