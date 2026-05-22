
list_ = ["Collins", "Collins", 'Luka', "Rakim", "Rakim", "Lulu"]
dict_ = {}
for name in list_:
    dict_[name] = dict_.get(name, 0) + 1

print(dict_)
