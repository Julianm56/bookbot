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
        

def main():
    content =get_file_content("books/frankenstein.txt")
    print(content)

    word_count = get_word_count(content)
    print(word_count)

    char_count = get_character_count(content)
    print(char_count)


main()
