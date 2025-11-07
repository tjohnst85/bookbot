def get_num_words(text):
    word_list = text.split()
    word_count = len(word_list)
    print(f"Found {word_count} total words")


def get_letter_count(text):
    unique_letter_set = set()
    unique_letter_counter = {}
    textlower = text.lower()
    letters = list(textlower)
    for l in letters:
        unique_letter_set.add(l)

    unique_letter_count = {item:0 for item in unique_letter_set}

    for l in letters:
        if l in unique_letter_count:
            unique_letter_count[l] += 1




