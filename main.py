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
    
    # return filtered set + list of known_letters since its going to
    # be used afterwards to eliminate possibly mistakes from user if
    # he type as "not contained letter" one letter in this known_list
    return filtered_by_contained_letters(list(known_letters), word_set), known_letters

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

def get_not_contained_letters(contained_letters, word_set):
    known_not_contained_letters = input("Enter the known letters not in the word: ")
    # find possibly contained letters possibly mistakenly 
    # typed into "not contained" list by the user
    filtered_not_contained_letters = [''.join(char) for char in known_not_contained_letters if contained_letters.find(char) == -1]
    return filtered_by_not_contained_letters(filtered_not_contained_letters, word_set)

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
    return filtered_by_right_placed_letters(known_part_of_word, word_set) if known_part_of_word else word_set

def filtered_by_right_placed_letters(known_part, word_set):
    def get_time_char_appears_in_string(char, string):
        times_char_appeared = 0
        for each in string:
            if char == each:
                times_char_appeared += 1
        return times_char_appeared   

    result_list = []
    wildcard = '@'
    known_chars = ''.join(filter(lambda char: char != wildcard, known_part))
    
    # removing repeated chars
    known_chars_not_repeated = known_chars 
    for char in known_chars:
        known_chars_not_repeated.replace(char, '', 1)

    # known_part and word:
    # case: 1 and 1
    for word in word_set:
        compatibility_lv = 0
        for char in known_chars:
            
            # get times char apears in known_part:
            times_at_known_chars = get_time_char_appears_in_string(char, known_chars)
            # get times char appears in word
            times_at_word = get_time_char_appears_in_string(char, word)
            
            # if 1 and 1
            if times_at_known_chars == 1 and times_at_word == 1:
                if known_part.index(char) == word.index(char):
                    compatibility_lv += 1
            
            # if 1 and 2
            if times_at_known_chars == 1 and times_at_word == 2:
                if known_part.index(char) == word.index(char) or known_part.index(char) == word.rindex(char):
                    compatibility_lv += 1
            
            # if 2 and 1
            if times_at_known_chars == 2 and times_at_word == 1:
                continue

            # if 2 and 2
            if times_at_known_chars == 2 and times_at_word == 2:
                if known_part.index(char) == word.index(char) and known_part.rindex(char) == word.rindex(char):
                    compatibility_lv += 1
        
        if compatibility_lv == len(known_chars_not_repeated):
                result_list.append(word)
    result_set = set(result_list)
    return result_set  
        
def get_wrong_placed_letters(word_set, col_index=0):
    columns = (0,1,2,3,4)
    wrong_placed_chars = input("Enter which letter cannot be in the {} column: ".format(columns[col_index]+1)) 
    column = columns[col_index]

    word_set = filtered_by_wrong_placed_letters(column, wrong_placed_chars, word_set)
    
    return get_wrong_placed_letters(word_set, col_index+1) if col_index != 4 else filtered_by_wrong_placed_letters(columns[col_index], wrong_placed_chars, word_set)

def filtered_by_wrong_placed_letters(column, wrong_placed_chars, word_set):
    result_list = []
    for word in word_set:
        wrong_placed_char_count = 0
        for char in wrong_placed_chars:
            if word.index(char) == column:
                wrong_placed_char_count += 1
        if wrong_placed_char_count > 0:
            continue
        else:
            result_list.append(word)

    result_set = set(result_list)
    return result_set

def search_result():
    print('teste')

def write_result(resulted_word_set):
    result_file = open("result-file.txt", "w")
    for word in resulted_word_set:
        word += '\n'
        result_file.writelines(word)
    
if __name__ == "__main__":
    
    word_set = make_set()
    word_set, known_letters = get_contained_letters(word_set)
    word_set = get_right_placed_letters(word_set)
    word_set = get_not_contained_letters(known_letters, word_set)
    word_set = get_wrong_placed_letters(word_set)

    print_set(word_set)
    write_result(word_set)    
