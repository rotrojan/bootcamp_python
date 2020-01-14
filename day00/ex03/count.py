import sys


def text_analyzer(text=None):
    """This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text."""
    if text is None:
        print("What is the text to analyse?")
        string = input()
    else:
        string = text
    upper_case = 0
    lower_case = 0
    white_space = 0
    punctuation = 0
    nb_char = 0
    for elem in string:
        if elem.isupper():
            upper_case += 1
        elif elem.islower():
            lower_case += 1
        elif elem.isspace():
            white_space += 1
        elif not elem.isdigit():
            punctuation += 1
        nb_char += 1
    print("The string contains", nb_char, "characters:")
    print("-", upper_case, "upper letter")
    print("-", lower_case, "lower letter")
    print("-", punctuation, "punctuation marks")
    print("-", white_space, "spaces")
