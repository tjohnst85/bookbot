from stats import get_num_words, get_letter_count, chars_dict_to_sorted_list



def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    text3 = get_num_words(text)
    text2 = get_letter_count(text)
    text4 = chars_dict_to_sorted_list(text2)
    print_report(book_path, text3, text4)
    
    

def get_book_text(book):
    with open(book) as f:
        return f.read()

def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()
