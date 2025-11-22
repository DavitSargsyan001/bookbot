import sys
from stats import count_words
from stats import char_count
from stats import sort_my_dict

def get_book_text(pathToFile):
    with open(pathToFile) as f:
        file_contents = f.read()
    
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    #path = 'books/frankenstein.txt'
    fileRead = get_book_text(path)
    word_count = count_words(fileRead)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    chars_count = char_count(fileRead)
    list_of_dicts = sort_my_dict(chars_count)
    
    for i in list_of_dicts:
        if i["char"].isalpha():
            v1 = i["char"]
            v2 = i["num"]
            print(f"{v1}: {v2}")

    print("============= END ===============")

main()