t = (19, 42, 21)

string_tuple = ', '.join(tuple(str(elem) for elem in t))
string = "The " + str(len(t)) + " numbers are " + string_tuple
print(string)
