
def get_book_text(path):
  with open(path) as f:
        file_contents = f.read()
        return file_contents
    
def get_character_dict(string):

    character_dict = {}

    for char in string.lower():
        if not char.isalpha():
            continue

        if char in character_dict:
            character_dict[char] += 1
        else:
            character_dict[char] = 1
    return character_dict

def sort_on(dict):
    return dict["count"]


def dict_to_sorted_list(dict):
    sorted_list = []

    for char in dict:
        sorted_list.append({"count": dict[char], "char": char})

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def main():

    book_file_name = "books/frankenstein.txt"

    book_content = get_book_text(book_file_name)
    character_dict = get_character_dict(book_content)
    sorted_list = dict_to_sorted_list(character_dict)

    
    print(f"--- Begin report of {book_file_name} ---")

    for i in sorted_list:
        count = i["count"]
        char = i["char"]
        print(f"The '{char}' character was found {count} times")

    print("--- End report ---")
main()