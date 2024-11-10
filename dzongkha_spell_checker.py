import re

def load_words_from_dictionary(file):
    with open(file, 'r', encoding='utf-8') as f:
        return set(f.read().splitlines())

def ordinal(n):
    return f"{n}{'th' if 10 <= n % 100 <= 20 else {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')}"

def check_incorrect_words(text, dictionary):
    with open(text, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, start=1):
            for pos, word in enumerate(re.findall(r'\S+', line), start=1):
                if word not in dictionary:
                    print(f"Line {line_num}, {ordinal(pos)} word '{word}' is incorrect.")

if __name__ == "__main__":
    check_incorrect_words('364.txt', load_words_from_dictionary('cleaned_dictionary.txt'))
