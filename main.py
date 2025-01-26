def open_file(file_path):
   with open(file_path) as f:
    file_contents = f.read()
   return file_contents

def word_count_book(text):
    words = text.split()
    return len(words) 

def main():
    content = open_file("books/frankenstein.txt")
    print(content)

    num_words = word_count_book(content)
    print(num_words)


main()
