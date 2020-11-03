def foo():
    """Have this method return True."""
    pass


def concatenadd(a, b):
    """Change the following line such that this function
    returns the concatenation of a and b if they contain strings, and the sum
    if they contains ints or floats
    """
    pass


def cf_color(frogs, clutch):
    cfc = "white"
    if frogs >= 0 and frogs <= 2:
        cfc = "blue"
    if clutch >= 0:
        cfc = "green"
    if clutch >= frogs:
        cfc = "yellow"
    elif frogs <= 0 and frogs >= -2:
        cfc = "black"
    if clutch >= 0:
        cfc = "orange"
    elif frogs + clutch >= -2:
        cfc = "red"
    return cfc


def collatz(n):
    """
    Indent this code correctly
    such that it computes the number of steps needed
    to reach 1 (https://oeis.org/A006577)
    """
    counter = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    counter += 1
    return counter


def even_steven(word):
    """This function returns a string with every second letter of
    the word, starting at the second letter."""
    new_word = ""
    pass
    return new_word


def extend_e(word):
    """This function inserts the letter 'e' after each vowel in word."""
    vowels = "aeiouyAEIOUY"
    new_word = ""
    pass


def reply2argument(argument):
    """Given an input string it will return an argument."""
    reply = ""
    pass
    return reply


def argument_clinic():
    """This function will repeatedly ask for input, and try to
    be argumentative about it. It stops if the user types 42."""
    pass
    print("---> You're welcome.")
    return None
