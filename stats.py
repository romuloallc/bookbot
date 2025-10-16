def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()

    return file_contents


def count_words(book_path):
    num_words = 0
    text = get_book_text(book_path)
    for word in text.split():
        num_words += 1

    return num_words

def count_chars(book_path):
    text = get_book_text(book_path).lower()
    char_count = {}
    for word in text.split():
        for char in word:
            char_count[char] = char_count.get(char, 0) + 1

    return char_count

def sort_on(items):
    return items['num']
            
def sort_dict(book_path):
    text_dict = count_chars(book_path)
    list_dict = []
    for k, v in text_dict.items():
        list_dict.append({"char": k, "num": v})
    
    list_dict.sort(reverse=True, key=sort_on)
    return list_dict

def report(book_path):
    sorted_dict = sort_dict(book_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(book_path)} total words")
    print("--------- Character Count -------")
    list_dict = sort_dict(book_path)
    for item in list_dict:
        if item['char'].isalpha(): 
            print(f"{item['char']}: {item['num']}")

    print("============= END ===============")
