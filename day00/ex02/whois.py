from sys import argv


def is_even(nbr):
    if int(argv[1]) == 0:
        print("I'm Zero.")
    elif int(argv[1]) % 2 == 0:
        print("I'm Even.")
    else:
        print("Im Odd.")


def main():
    try:
        assert len(argv) == 2
        nbr = int(argv[1])
        is_even(argv)
    except AssertionError:
        print("ERROR")
    except ValueError:
        print("ERROR")


if __name__ == "__main__":
    main()
