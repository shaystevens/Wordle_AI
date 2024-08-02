def get_words(file_path='valid-wordle-words.txt'):
    """
    Reads Wordle words from a file and returns them as a list.

    Parameters:
    file_path (str): The path to the file containing the Wordle words.

    Returns:
    list: A list of valid Wordle words.
    """
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
            words = contents.split('\n')
            words_list = [word for word in words if word] 
        return words_list
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
    

def get_letters(file_path='alphabet.txt'):
    """
    Reads alphabet from a file and returns them as a dict.

    Parameters:
    file_path (str): The path to the file containing alphabet letters.

    Returns:
    list: A dict of valid english letters.
    """
    letters_dict = {}
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
            letters = contents.split('\n')
            letters_list = [letter for letter in letters if letter] 
            letters_dict = {letter: 0 for letter in letters_list}

        return letters_dict
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}
