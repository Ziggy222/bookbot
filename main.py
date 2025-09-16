from stats import get_word_count
from stats import get_character_count
from stats import create_sorted_list

import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def print_report(book_path, word_count, sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for character in sorted_list:
        print(f"{character["char"]}: {character["num"]}")
    print("============= END ===============")

def main():
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)

    char_count = get_character_count(book_text)
    
    sorted_list = create_sorted_list(char_count)
    
    print_report(book_path, word_count, sorted_list)

if not len(sys.argv) == 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main()