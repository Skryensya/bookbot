from stats import get_num_words
from stats import get_num_letters
from stats import sort_dict_into_list
from sys import argv, exit

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if(len(argv) < 2 ):
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    filepath= argv[1]
    book = get_book_text(filepath)
    num_words = get_num_words(book)
    letter_count = get_num_letters(book)
    sorted_letter_count = sort_dict_into_list(letter_count)
 
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for c in sorted_letter_count:
        print(f"{c["char"]}: {c["num"]}")

    print("============= END ===============")


if __name__ == "__main__":
    main()