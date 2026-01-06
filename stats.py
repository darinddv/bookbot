# Write a new function that accepts the text from the book as a string, and returns the number of words in the string. The .split() method will be helpful here.
def get_num_words(text):
    words = text.split()
    return len(words)


def get_char_counts(text):
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts


def get_sorted_char_counts(char_counts):
    char_list = [{"char": char, "num": count} for char, count in char_counts.items() if char.isalpha()]
    char_list.sort(key=lambda x: x["num"], reverse=True)
    return char_list

