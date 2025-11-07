def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_letters(text):
    dictionary = {}
    for c in text:
        c= c.lower()
        if(c.isalpha() == False):
            continue
        if(c not in dictionary):
            dictionary[c] = 1
        else:
            dictionary[c]+=1
    return dictionary


def sort_on(items):
    return items["num"]
        

def sort_dict_into_list(dictionary):
    sorted_list = []
    for k, v in dictionary.items():
        item = {"char": k, "num": v}
        sorted_list.append(item)

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list