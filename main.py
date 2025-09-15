from stats import number_words, count_characters, sort_func
import sys
print("Give us any book from books/nameofbook.txt")
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
inputx = sys.argv[1]
def get_book_text(inputx):
    with open (inputx) as f:
        text = f.read()
    return text


def main():
    sorted_chars = sort_func(count_characters(inputx))
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    for i in sorted_chars:
        print(f"{i["char"]}: {i['num']}")
    print("============= END ===============")
main()