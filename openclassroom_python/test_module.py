"""Test module"""

def print_float(nbr):
    """Print floating point number shorten at third decimal
    and replace '.' by ','."""
    if type(nbr) is not float:
        raise TypeError("Type float expected.")
    nbr = str(nbr)
    nbr = nbr.split('.')
    print(nbr[0] + ',' + nbr[1][:3])

def is_bisextile(year):
    year = input("Choose a year : ")
    year = int(year)
    if not year % 4:
        if not year % 100:
            if not year % 400:
                print("bissexile")
            else:
               print("not bissexile")
        else:
            print("bissexile")
    else:
        print("not bissexile")

def my_print(*values, sep=' ', end='\n'):
    string = ''
    for elem in values:
        string = string + str(sep) + str(elem)
    string += str(end)
    string = string[1:]
    print(string, end='', sep='')

inventaire = [
    ("pommes", 22),
    ("melons", 4),
    ("poires", 18),
    ("fraises", 76),
    ("prunes", 51),
]
