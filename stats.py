def count_words(book_contents):

    words = book_contents.split()
    num_words = len(words)
    return num_words

def get_chars_dict(text):
    chars = {}                  
    for c in text:  
        lowered = c.lower()
        if lowered in chars:     
            chars[lowered] += 1 
        else:                    
            chars[lowered] = 1  
    return chars

def sort_on(items):
    return items["num"]

def sorting(chars):
    new_list = []
    for c in chars:  
        if c.isalpha():  
            temp_dict = {}
            temp_dict["char"] = c           
            temp_dict["num"] = chars[c]
            new_list.append(temp_dict) 
    new_list.sort(reverse=True, key=sort_on)
    return new_list
