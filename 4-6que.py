my_list = [42,43]
my_dict = {
    'foo': {
        'a':12,
        'b': (1, 2, 3, 4, my_list)
    },
    'bar': {
        'c':12,
        'd': {5, 6, 7, 8}
    },
    'moo': {
        'e' :12,
        'f' : {'lol': ['l', 'o', 'l'] }
    },
}


print(my_dict['foo']['b'])
my_set = set(my_list)
my_list.append(9)
print(my_list)





