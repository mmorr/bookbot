def character_count(s):
    lower_s = s.lower()
    char_count = {}
    for char in lower_s:
        if char in 'abcdefghijklmnopqrstuvwxyz':
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def word_count(s):
    return len(s.split())

def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
    
    wordCount = word_count(file_contents)
    char_count = character_count(file_contents)
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{wordCount} words found in the document.")
    for char, count in char_count.items():
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")
main()