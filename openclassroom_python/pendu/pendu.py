from data import dictionary
from random import randrange
from functions import check_for_victory, check_for_fail, ask_and_check_letter

def main():
    print("HANGMAN\n")
    tries_left = 8
    found_letters = set()
    tried_letters = set()
    keep_on_playing = True
    while keep_on_playing:
        keep_on_playing = False
        print("New Game\n")
        word = dictionary[randrange(len(dictionary))].casefold()
        game_over = False
        while not game_over:
            answer = set(word)
            print("Already tried letters :", ' '.join(tried_letters))
            for letter in word:
                if "".join(found_letters).find(letter) == -1:
                    print('*', end='')
                else:
                    print(letter, end='')
                print(' ', end='')
            choosen_letter = ask_and_check_letter(found_letters, tried_letters, tries_left)
            if word.find(choosen_letter) != -1:
                 game_over = check_for_victory\
                 (choosen_letter, found_letters, answer, word.upper())
            else:
                tries_left -= 1
                game_over = check_for_fail\
                (choosen_letter, tried_letters, tries_left, word.upper())
        keep_on_playing = False

if __name__ == "__main__":
    main()
