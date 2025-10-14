def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()

    return file_contents


def count_words():
    num_words = 0
    text = get_book_text("./books/frankenstein.txt")
    for word in text.split():
        num_words += 1

    return num_words

def count_chars():
    text = get_book_text("./books/frankenstein.txt").lower()
    char_count = {}
    for word in text.split():
        for char in word:
            char_count[char] = char_count.get(char, 0) + 1

    return char_count

def sort_on(items):
    return items['num']
            
def sort_dict():
    text_dict = count_chars()
    list_dict = []
    for k, v in text_dict.items():
        list_dict.append({"char": k, "num": v})
    
    list_dict.sort(reverse=True, key=sort_on)
    return list_dict

def report():
    sorted_dict = sort_dict()
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count_words()} total words")
    print("--------- Character Count -------")
    list_dict = sort_dict()
    for item in list_dict:
        if item['char'].isalpha(): 
            print(f"{item['char']}: {item['num']}")

    print("============= END ===============")
