import sys

from stats import (
    get_num_words, 
    get_chars_dict,
    chars_dict_to_sorted_list
)


# print("hello world")

# def main():
#     with open("/Users/mire87/workspace/github.com/miARTre/bookbot/books/frankenstein.txt") as f:
#         file_contents = f.read()
#     print(file_contents)

# main()    

# def main():
#     book_path = "books/frankenstein.txt"
#     text = get_book_text(book_path)
#     print(text)

#     count_words = get_num_words(text)
#     # print(count_words)
#     print(f"{count_words} words found in the document")

#     count_char = get_count_char(text)
#     print(count_char)

#     char_list = convert_dict_to_list(count_char)
#     char_list.sort(reverse=True, key=sort_on)
#     print(char_list)

#     print_report(char_list, count_words, book_path)
   
# def convert_dict_to_list(char_dict):
#     char_list = []
#     for char, count in char_dict.items():
#         if char.isalpha():  
#             char_list.append({"char": char, "num": count})
#     return char_list

# def print_report(char_list, word_count, book_path):
#     print(f"--- Begin report of {book_path} ---")
#     print(f"{word_count} words found in the document\n")
    
#     for char_dict in char_list:
#         if char_dict["char"].isalpha(): 
#             print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")
    
#     print("--- End report ---")
 
# def sort_on(dict):
#     return dict["num"]

# def get_count_char(text):
    
#     char_lower = text.lower()
#     dict = {}    

#     for char in char_lower:
#         if char in dict:
#             dict[char] += 1
#         else:
#             dict[char] = 1
#     return dict


# def get_book_text(path):
#     with open(path) as f:
#         return f.read()



def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print_report(book_path, num_words, chars_sorted_list)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


main()
