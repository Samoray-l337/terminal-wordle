from ..config import WORDS_LIST_FILE_PATH

# TODO: make it more efficient
def does_word_exists_inside_words_list(word):
    with open(WORDS_LIST_FILE_PATH, 'r') as f:
        words = [word.strip() for word in f.readlines()]

        return word in words