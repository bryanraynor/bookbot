def get_num_words(text):
    words = text.split()
    num_words = len(words)
    return num_words

def character_count(text):
    counts = {}
    for ch in text.lower():
        if ch in counts:
            counts[ch] += 1
        else:
            counts[ch] = 1
    return counts

def sort_on(item):
    return item["num"]

def sorted_character_report(char_dict):
    report = []

    for ch, count in char_dict.items():
        if ch.isalpha():  # skip non‑alphabetical characters
            report.append({"char": ch, "num": count})

    report.sort(key=sort_on, reverse=True)
    return report
