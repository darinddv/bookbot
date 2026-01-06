import sys

def get_book_text(path):
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path = sys.argv[1]
book_text = get_book_text(path)

from stats import get_num_words, get_char_counts, get_sorted_char_counts

print("============ BOOKBOT ============")
print(f"Analyzing book found at {path}...")
print("----------- Word Count ----------")
num_words = get_num_words(book_text)
print(f"Found {num_words} total words")
print("--------- Character Count -------")
char_counts = get_char_counts(book_text)
sorted_char_counts = get_sorted_char_counts(char_counts)
for item in sorted_char_counts:
    print(f"{item['char']}: {item['num']}")
print("============= END ===============")