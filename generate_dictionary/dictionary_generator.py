import os 

def make_dictionary():
    word_list = []
    line_break = '\n'
    slash = '/'
    path = os.getcwd()
    path += '/generate_dictionary/original-dic.txt'
    with open(path) as palavras:
        for line in palavras.readlines():
            slash_count = 0
            line = line.replace(line_break, '')
            for char in line:
                if char == slash:
                    slash_count += 1
                if slash_count > 0:
                    line = line.replace(char, '')
            word_list.append(line)
        word_set = set(word_list)
        filtered_word_set = filter_words(word_set)
    return write_result(filtered_word_set)

def filter_words(word_set):
    filtered_list = []
    for word in word_set:
        word = word.lower()
        # only 5 char words will be filtered
        if is_right_lenght(word) == False:
            continue
        # only words with no special char will be filtered
        special_char_count = 0
        for char in word:
            if char.isalpha() == False:
                special_char_count += 1
        if special_char_count > 0:
            continue
        # remove accents
        word = remove_accent(word)
        filtered_list.append(word)
    filtered_set = set(filtered_list)
    return filtered_set

def write_result(resulted_w_set):
    path = os.getcwd()
    path += '/dictionary.txt'
    result_file = open(path, "w")
    for word in resulted_w_set:
        word += '\n'
        result_file.writelines(word)
 
def is_right_lenght(word):
    return True if len(word) == 5 else False

def remove_accent(word):
    accented_chars = 'áàâãéêíóôúüç'
    for char in word:
        if char in accented_chars:
            if char in accented_chars[0:4]:
                word = word.replace(char, 'a')
            elif char in accented_chars[4:6]:
                word = word.replace(char, 'e')
            elif char in accented_chars[6:7]:
                word = word.replace(char, 'i')
            elif char in accented_chars[7:9]:
                word = word.replace(char, 'o')
            elif char in accented_chars[9:11]:
                word = word.replace(char, 'u')
            elif char in accented_chars[11:12]:
                word = word.replace(char, 'c') 
    return word

if __name__ == "__main__":
    print("You're not meant to run this from here! Run the main file instead!")
