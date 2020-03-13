def check_for_victory(choosen_letter, found_letters, answer, word):
    found_letters.add(choosen_letter)
    if found_letters == answer:
        print("Congratulations, you won ! :D")
        print("The word was {}.".format(word))
        return True
    else:
        print("Well played !\n")
        return False

def check_for_fail(choosen_letter, tried_letters, tries_left, word):
    if not tries_left:
        print("GAME OVER X(\n")
        print("The word was {}.".format(word))
        return True
    else:
        tried_letters.add(choosen_letter)
        tried_letters = list(dict.fromkeys(tried_letters))
        print("Missed.\n")
        return False

def ask_and_check_letter(found_letters, tried_letters, tries_left):
    input_is_valid = False
    while input_is_valid == False:
        print("\nYou have {} tries left".format(tries_left))
        choosen_letter = input("Choose a letter : ").casefold()
        try:
            if choosen_letter.isalpha() == False:
                raise ValueError("Input is not a letter.")
            assert len(choosen_letter) == 1
            if found_letters.isdisjoint(choosen_letter) is False or \
            tried_letters.isdisjoint(choosen_letter) is False:
                raise ValueError("You already tried this letter.")
            input_is_valid = True
        except AssertionError:
            print("\nWrong Input : "
            "you did not choose a single letter.")
        except ValueError as error:
            print("\nWrong Input :", error)
    return (choosen_letter)
