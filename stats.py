from typing import Any


def number_words(inputx):

    with open (inputx) as f:
        text = f.read()
        counter = 0
        new_list = text.split()
        for word in new_list:
            counter += 1
        return counter

def count_characters(inputx):
    with open(inputx) as f:
        text = f.read()
        text = text.lower()
        new_list =  []
        new_list.append(text)
        new_string = " ".join(new_list)
        letters_symbols = {
            "a" : 0, "b" : 0,"c" : 0,"d" : 0,"e" : 0,"f" : 0,"g" : 0,"h" : 0, "i" : 0,"j": 0,"k" : 0,"l" : 0,
            "m" : 0,"n" : 0,"o" : 0,"p" : 0,"q" : 0,"r" : 0,"s" : 0,"t" : 0,"u" : 0,"v" : 0,"w" : 0,"x" : 0,"y" : 0,
            "z" : 0,"!" : 0,"?" : 0,"-": 0 ,"%" : 0,"&" : 0,"*": 0,"#" : 0,"%" : 0,"&" : 0,"*" : 0,"/" : 0,"." : 0,
            "'" : 0,":" : 0,";" : 0
        }

        for i in range(0, len(new_string)):
            if new_string[i] in letters_symbols:
                letters_symbols[new_string[i]] += 1

    return letters_symbols

def sort_on(items):
    return items["num"]

def sort_func(dict_to_sort):
    list_of_dicts = [{"char": k, "num": v} for k, v in dict_to_sort.items()]
    output = list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts










