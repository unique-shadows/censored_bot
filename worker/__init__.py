def load_words_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def censored(input_string):
    file_name = 'worker/censored.txt'
    word_list = load_words_from_file(file_name)

    for word in word_list:
        if word.lower() in input_string.lower():
            return True

    return False