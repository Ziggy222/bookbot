def get_word_count(text):
    return len(text.split())

def get_character_count(text):
    char_counts = {}
    for char in text:
        temp_char = char.lower()
        if temp_char in char_counts:
            char_counts[temp_char] += 1
        else:
            char_counts[temp_char] = 1
    return char_counts

def get_count(list_member):
    print(list_member)
    return list_member["num"]

def create_sorted_list(char_counts):
    sorted_list = []

    # for each character in our dictionary,
    # we check if that character is alpha since we
    # only care about alpha characters for this report
    for char_count in char_counts:
        if char_count.isalpha():
            char = char_count
            count = char_counts[char_count]
            sorted_list.append({
                "char": char,
                "num": count
            })
    
    # Sort by num value

    sorted_list.sort(key=lambda character: character["num"], reverse=True)

    return sorted_list
      