def count_words_in_file(file_path: str) -> int:
    with open(file_path, 'r') as file:
        text = file.read()
    words = text.split()
    return len(words)

# Example:
if __name__ == "__main__":
    file_path = "accounts.txt"
    # testing
    word_count = count_words_in_file(file_path)
    print(f"Number of words in '{file_path}': {word_count}")
