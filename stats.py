def count_words(book_contents):
    words = book_contents.split()
    return len(words)

def char_count(book_contents):
    book_contents = book_contents.lower()
    my_dict = {}
    for char in book_contents:
        if char in my_dict:
            # +1 the character count
            my_dict[char] += 1
        else:
            # define key and put the count of that key to 1
            my_dict[char] = 1
    
    return my_dict

def sort_on(items):
    return items["num"]

def sort_my_dict(my_dict):
    list_of_dicts = []
    for dictt in my_dict:
        list_of_dicts.append({"char": dictt, "num": my_dict[dictt]})
    
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts



