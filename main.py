from stats import get_num_words
from stats import get_letter_count

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(get_letter_count(text))
    

def get_book_text(book):
    with open(book) as f:
        return f.read()

main()
