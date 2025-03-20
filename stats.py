def get_num_words(file_contents):
    clean_words = file_contents.replace("  ", " ").replace('""', " ")
    words = clean_words.split()
    word_count = len(words)
    return f"Found {word_count} total words"

def build_char_dict(text):
    letter_count = {}
    for char in text:
        char = char.lower()
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1
    return letter_count


def sort_on(char_dict):
    dict_list = []
    for key, value in char_dict.items():
        if key.isalpha():
            new_dict = {"char": key, "count": value}
            dict_list.append(new_dict)
    dict_list.sort(reverse=True, key=lambda counts: counts["count"])
    return dict_list




    

    