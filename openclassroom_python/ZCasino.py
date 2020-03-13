from random import randrange
from math import ceil

def betting(credit):
    """ Take the bet and check if it is possible."""
    print("Your current credit is", credit, end='$.\n')
    bet = input("How much do you want to bet ?\n")
    print()
    try:
        bet = int(bet)
        assert bet <= credit
        assert bet > 0
    except AssertionError:
        if bet <= 0:
            print("You cannot bet a null orn negative value.")
        elif bet > credit:
            print("You don't have enough money to bet that much.")
        betting(credit)
    except:
        print("You entered an incorrect input.")
        betting(credit)
    return bet


def choose_nbr():
    choosen_nbr = input("Which number from 0 to 50 do you want to bet on ?\n")
    print()
    try:
        choosen_nbr = int(choosen_nbr)
        assert choosen_nbr >= 0
        assert choosen_nbr < 50
        return (choosen_nbr)
    except AssertionError:
        print("You entered an incorrect value.")
        choose_nbr()
    except:
        print("You entered an incorrect input.")
        choose_nbr()


def game_and_gain(choosen_nbr, bet):
    """Launch the roulette and return the gain (or the loss if negative)."""
    roulette = int(randrange(50))
    print("The roulette nbr is :", roulette, end=".\n")
    if roulette == choosen_nbr:
        print("You won the jackpot ! :D")
        return bet * 3
    elif (roulette % 2) == (choosen_nbr % 2):
        print("You won ! :)")
        return ceil(bet / 2)
    else:
        print("You lost ! :(")
        return -1 * bet


def main():
    print("WELCOME TO THE ZCASINO\n")
    credit = 1000
    while (credit > 0):
        bet = betting(credit)
        choosen_nbr = choose_nbr()
        gain = game_and_gain(choosen_nbr, bet)
        credit += gain
        if gain > 0:
            print("You earned", gain, end = '$.\n')
        else:
            print("You lost", bet, end = '$.\n')
        print("Your current credit is now", credit, end='$.\n')
        print()
        if input("Do you want to keep on playing (Yes/No) : ") is not ("y" or "Y" or "yes" or "Yes" or "YES"):
            print()
            print("You are leaving the Zcasino.")
            if (credit >= 1000):
                print("You earned", credit - 1000, end='$.\n'  )
            else:
                print("You lost", 1000 - credit, end='$.\n'  )
            print()
            print("Goodbye. :)");
            break
    if credit == 0:
        print("You do not have anything left to bet ... GAME OVER X(")


if __name__ == "__main__":
    main()
