import re

def clean_line(line):
    return re.sub(r'[^\u0F00-\u0FFF\s]', '', line.strip())

def clean_text(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
            unique_words = set()
            for line in infile:
                words = clean_line(line).split()
                unique_words.update(words)
            outfile.write('\n'.join(sorted(unique_words)) + '\n')
        print(f"Successfully cleaned the text. Output saved to {output_file}.")
    except (FileNotFoundError, IOError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    clean_text('dictionary.txt', 'cleaned_dictionary.txt')

