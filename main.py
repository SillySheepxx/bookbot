def count_words(txt):
    words_num = len(txt.split())
    return words_num

def count_characters(txt):
    raw_data_lower = txt.lower()
    char_dict = dict()
    for char in raw_data_lower:
        if char not in  char_dict.keys():
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

def generate_report(txt, file_url):
    print(f"--- Begin report of {file_url} ---")
    print(f"{count_words(txt)} words found in the document")
    print()
    report_word_dict = count_characters(txt)
    tmp_dict = dict()
    for letter, times in report_word_dict.items():
        if letter.isalpha():
           tmp_dict[letter] = times
    sort_letters_list =  sorted(tmp_dict.items(), key=lambda x:x[1], reverse=True)
    for letter in sort_letters_list:
        print(f"The '{letter[0]}' character was found {letter[1]} times")
    print("--- End report ---")
def main():
    url = "books/frankenstein.txt"
    with open(url) as f:
        file_contents = f.read()
        generate_report(file_contents, url)
    
main()
