from stats import count_words, get_chars_dict, sort_on, sorting
import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    filepath = sys.argv[1]
    book_contents = get_book_text(filepath)
    num_words = count_words(book_contents)
    chars = get_chars_dict(book_contents)
    sorted_report = sorting(chars)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {filepath}...\n----------- Word Count ----------\nFound {num_words} total words\n--------- Character Count -------")
    for l in sorted_report:
        num = l["num"]
        char = l["char"]
        print(f"{char}: {num}")
    print("============= END ===============")
if __name__ == "__main__":
    main()
