def get_num_words(text):
    word_list = text.split()
    word_count = len(word_list)
    return word_count


def get_letter_count(text):
    textlower = text.lower()
    unique_letter_set = set()
    unique_letter_counter = {}
            
    letters = list(textlower)
    for l in letters:
        unique_letter_set.add(l)

    unique_letter_count = {item:0 for item in unique_letter_set}

    for l in letters:
        if l in unique_letter_count:
            unique_letter_count[l] += 1

    return unique_letter_count


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list




