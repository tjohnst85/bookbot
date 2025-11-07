def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_list = text.split()
    word_count = len(word_list)
    print(f"Found {word_count} total words")

def get_book_text(book):
    with open(book) as f:
        return f.read()

main()
