import stats
import sys

def get_boot_text(file):
    with open(file) as f:
        return f.read()

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_text = get_boot_text(sys.argv[1])
    words_count = stats.count_words(file_text)
    character_count = stats.count_characters(file_text)
    sorted_char_count = stats.sort_characters(character_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")
    for i in sorted_char_count:
        if i["char"].isalpha():
            print(f"{i['char']}: {i['num']}")
    print("============= END ===============")
if __name__ == "__main__":
    main()