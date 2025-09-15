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
    #print(get_book_text("books/frankenstein.txt"))
    #print(f"{number_words("books/frankenstein.txt")} words found in the document")
    sorted_chars = sort_func(count_characters(inputx))
    #print(count_characters("books/frankenstein.txt"))
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    #print(f"Found {number_words(f"{}")} total words")
    for i in sorted_chars:
        print(f"{i["char"]}: {i['num']}")
    #print(sort_func(count_characters(f"{inputx}")))
    print("============= END ===============")
main()