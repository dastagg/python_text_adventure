def pretty_print_unordered(to_print):
    for item in to_print:
        print("* " + str(item))


def pretty_print_ordered(to_print):
    for i, value in enumerate(to_print, 1):
        print(str(i) + ". " + str(value))


def pretty_print_ordered1(to_print):
    i = 1
    for item in to_print:
        print(i + ". " + str(item))
        i = i + 1


def pretty_print_ordered2(to_print):
    for i in range(len(to_print)):
        print(str(i + 1) + ". " + str(to_print[i]))


favorites = []
more_items = True
while more_items:
    user_input = input("Enter something you like: ")
    if user_input == "":
        more_items = False
    else:
        favorites.append(user_input)

print("Here are all the things you like!")
pretty_print_unordered(favorites)
pretty_print_ordered(favorites)
