def get_file_content(file_path):
   with open(file_path) as f:
    file_contents = f.read()
   return file_contents

def get_word_count(text):
    words = text.split()
    return len(words) 

def get_character_count(text):
    characters = {}
    lower_case_text = text.lower()

    for word in lower_case_text:
        if word in characters:
            characters[word]+=1
        else:
            characters[word] = 1

    return characters

def sort_dictionary(dictionary):
    temp_dic = dictionary
    sorted_dic = {}
    while len(temp_dic) > 0:
        current_max_key = ""
        current_max_found = 0
        for item in temp_dic:
            if(temp_dic[item] > current_max_found):
                current_max_key = item
                current_max_found  = temp_dic[item]

        sorted_dic[current_max_key] = temp_dic[current_max_key]
        del temp_dic[current_max_key]

    return sorted_dic



def print_report(file_path, word_count, character_count):
    title_string = f"--- Begin report of {file_path} ---"
    word_count_string = f"{word_count} words found in the document\n"

    print(title_string)
    print(word_count_string)

    sorted_character_count = sort_dictionary(character_count)
    
    
    for character in sorted_character_count:
        if(character.isalpha()):
            num_found = sorted_character_count[character]
            character_string = f"The '{character}' was found {num_found} times"
            print(character_string)
    print("--- End report ---")

def main():
    file_path = "books/frankenstein.txt"

    content =get_file_content(file_path)

    word_count = get_word_count(content)

    char_count = get_character_count(content)
    
    print_report(file_path, word_count, char_count)

main()
