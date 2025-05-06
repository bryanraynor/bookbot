def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(d):
    return d["num"]

def sorted_list(char_count):
    char_list = []
    for char in char_count:
        char_list.append({"char": char, "num": char_count[char]})
        char_list.sort(reverse=True, key=sort_on)
    return char_list

