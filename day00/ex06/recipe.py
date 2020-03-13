from cookbook import cookbook


def print_recipe(name_recipe):
    """Print the recipe given in parameter or an error message."""
    global cookbook
    for name in cookbook.keys():
        if name == name_recipe:
            print("\nRecipe for", name_recipe, end=':\n')
            print("Ingredients list:", cookbook[name]['ingredients'])
            print("To be eaten for", cookbook[name]['meal'], end='.\n')
            print("Takes {} minutes of cooking."
                  .format(cookbook[name]['prep_time']))
            return
    print("This recipe does not exist.")


def print_cookbook():
    global cookbook
    for name in cookbook.keys():
        print_recipe(name)
    input()


def add_recipe(name_recipe, ingredients, meal, prep_time):
    global cookbook
    cookbook[name_recipe] = {
        'ingredients':  ingredients,
        'meal': meal,
        'prep_time': prep_time
    }


def ask_for_new_recipe():
    global cookbook
    name_recipe = input("\nWhat is the name of the new recipe ? ")
    ingredients = list()
    user_input = input("What are the ingredients of your recipe\n"
                       "(Type OK when done) ? ")
    while user_input.casefold() != 'ok'.casefold():
        ingredients.append(user_input)
        user_input = input("New ingredient is {}.\n".format(user_input) +
                           "What is the next ingredient ? ")
    meal = input("What kind of meal is it ? ")
    user_input = input("How long does it take to cook it (in minutes) ? ")
    is_int = False
    while not is_int:
        is_int = True
        try:
            int(user_input)
            is_int = True
        except ValueError:
            is_int = False
            print("Invalid number of minutes.")
            user_input = input("How long does it take to cook it "
                               "(in minutes) ? ")
    prep_time = user_input
    return (name_recipe, ingredients, meal, prep_time)


def del_recipe(name_recipe):
    global cookbook
    try:
        cookbook.pop(name_recipe)
    except KeyError:
        print("Error, this recipe does not exist.")


def main():
    """Display menu and ask user's choice."""
    quit = False
    while not quit:
        str_first_display = ("Please select an option by typing the "
                             "corresponding number:\n" "1: Add a recipe\n"
                             "2: Delete a recipe\n" "3: Print a recipe\n"
                             "4: Print the cookbook\n" "5: Quit\n")
        str_ask_again = ("\nThis option does not exist, please type the "
                         "corresponding number.\n" "To exit, enter 5.\n")
        ask_again = True
        user_input = input(str_first_display)
        while ask_again:
            ask_again = False
            if user_input == '1':
                new = ask_for_new_recipe()
                add_recipe(new[0], new[1], new[2], new[3])
            elif user_input == '2':
                del_recipe(input("\nWhat recipe do you want to delete ? "))
            elif user_input == '3':
                print_recipe(input("\nPlease enter the recipe's name to get "
                                   "its details:\n"))
                input()
            elif user_input == '4':
                print_cookbook()
            elif user_input == '5':
                print("\nCookbook closed.")
                quit = True
            else:
                ask_again = True
                user_input = input(str_ask_again)


if __name__ == "__main__":
    main()
