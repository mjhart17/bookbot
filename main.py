from stats import get_num_words, build_char_dict, sort_on
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        # Read the file
        with open(sys.argv[1]) as f:
            file_contents = f.read()

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]} ...")

        # Call get_num_words and print the word count
        word_count_result = get_num_words(file_contents)
        print("----------- Word Count ----------")
        print(word_count_result)

        # Build the character dictionary and calculate sorted character counts
        unsorted_dict = build_char_dict(file_contents)
        sorted_result = sort_on(unsorted_dict)

        # Print the formatted Character count report
        print("--------- Character Count -------")
        for entry in sorted_result:
            print(f"{entry["char"]}: {entry["count"]}") # format the report line by line
        print("============= END ===============")

# Call main function
if __name__ == "__main__":
    main()
