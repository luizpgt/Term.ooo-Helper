from generate_dictionary.dictionary_generator import make_dictionary 

def make_set():
    word_list = []
    line_break = '\n'
    try:
        with open("dictionary.txt") as palavras:
            for line in palavras.readlines():
                word_list.append(line.replace(line_break, '').lower())
        word_set = set(word_list)
        return word_set
    except:
        make_dictionary()
        return make_set()

def print_set(set):
    for word in set:
        print("Word : {}\n".format(list(word)))

def get_contained_letters(word_set): 
    known_letters = input("Enter the known letters in the word: ")
    return filtered_by_contained_letters(list(known_letters), word_set)

def filtered_by_contained_letters(known_letters, word_set):
    # known_letters is a list of char
    result_list = []
    for word in word_set:
        present_letter_count = 0
        for letter in known_letters:
            if letter in word:
                present_letter_count += 1
            if present_letter_count == len(known_letters):
                result_list.append(word)
    result_set = set(result_list)
    return result_set

def get_not_contained_letters(word_set):
    known_not_contained_letters = input("Enter the known letters not in the word: ")
    return filtered_by_not_contained_letters(known_not_contained_letters, word_set)

def filtered_by_not_contained_letters(known_not_in, word_set):
    result_list = []
    for word in word_set:
        present_letter_count = 0
        for letter in known_not_in:
            if letter in word:
                present_letter_count += 1
        if present_letter_count > 0:
            continue
        else:
            result_list.append(word)
    result_set = set(result_list)
    return result_set

def get_right_placed_letters(word_set):
    # wildcard = @
    examplemsg = 'AUDIO'.center(20) + '\n' + 'a@@i@'.center(20)
    print("Example: \n{}".format(examplemsg))
    known_part_of_word = input("Enter the right placed letters you already have: ")
    return filtered_by_right_placed_letters(known_part_of_word, word_set)

def filtered_by_right_placed_letters(known_part, word_set):
    # known_part is a string
    wildcard = '@'
    result_list = []
    
    known_chars_no_wildcards = ''.join(filter(lambda char: char != wildcard, known_part))

    for word in word_set:
        right_placed_letters_count = 0
        for char in known_part:
            if char != '@':
                if known_part.index(char) == word.index(char):
                    right_placed_letters_count += 1
                if right_placed_letters_count == len(known_chars_no_wildcards):
                    result_list.append(word)
    result_set = set(result_list)
    return result_set  
        
def get_wrong_placed_letters():
    print("")

def filtered_by_wrong_placed_letters():
    print("")

def search_result():
    print('teste')

def write_result(resulted_word_set):
    result_file = open("result-file.txt", "w")
    for word in resulted_word_set:
        word += '\n'
        result_file.writelines(word)
    
if __name__ == "__main__":
    
    initial_word_set = make_set()
    #print_set(word_set)
    word_set = get_contained_letters(initial_word_set)
    word_set = get_right_placed_letters(word_set)
    word_set = get_not_contained_letters(word_set)

    print_set(word_set)
    write_result(word_set)
    #right_placed_letters_word_set = get_right_placed_letters(word_set)
    
