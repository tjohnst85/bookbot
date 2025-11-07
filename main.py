from stats import get_num_words

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(get_num_words(text))
    

def get_book_text(book):
    with open(book) as f:
        return f.read()

main()
