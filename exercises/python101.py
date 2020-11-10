#Solutions Tutorial 1

def foo():
    """Have this method return True."""
    return True


def concatenadd(a, b):
    """Change the following line such that this function
    returns the concatenation of a and b if they contain strings, and the sum
    if they contains ints or floats
    """
    return a + b


def cf_color(frogs, clutch):
    """Indent this code correctly."""
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


def collatz_unsafe(n):
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


def collatz(n):
    """
    If this function is called with an integer >=1 it should
    return the correct answer, for floats >=1 is should provide
    the correct answer after rounding down the input value to the
    nearest integer, and in all other cases it should print a
    warning and return None.
    """
    if not (isinstance(n, int) or isinstance(n, float)):
        return None
    elif n < 1:
        return None
    else:
        return collatz_unsafe(int(n))


def even_steven(word):
    """This function returns a string with every second letter of
    the word, starting at the second letter."""
    new_word = ""
    for i in range(1, len(word), 2):
        new_word += word[i]
    return new_word


def extend_e(word):
    """This function inserts the letter 'e' after each vowel in word."""
    vowels = "aeiouyAEIOUY"
    new_word = ""
    for letter in word:
        new_word += letter
        for v in vowels:
            if letter == v:
                new_word += "e"
    return new_word


def reply2argument(argument):
    """Given an input string it will return an argument."""
    reply = ""
    if argument.find("Yes") == 0:
        reply = reply + "No! "
    elif argument.find("No") == 0:
        reply = reply + "Yes! "
    if argument.find("?") == len(argument) - 1:
        reply = reply + "None of your business. "
    elif argument.find("I ") >= 0:
        reply = reply + "No, you aren't."
    elif argument.find("You") >= 0 or argument.find("you") >= 0:
        reply = reply + "No, I'm not. "
    elif argument.find("It ") >= 0 or argument.find(" it ") >= 0:
        reply = reply + "No, it isn't. "
    elif argument.find("This ") >= 0 or argument.find(" this ") >= 0:
        reply = reply + "No, not true. "
    else:
        reply = reply + "Ooooh! " + extend_e(argument)
    return reply


def argument_clinic():
    """This function will repeatedly ask for input, and try to
    be argumentative about it. It stops if the user types 42."""
    answer = input("---> Hulloo, stranger." + ".>? ")
    while answer != "42":
        answer = input("---> " + reply2argument(answer) + ".>? ")
    print("---> You're welcome.")
    return None


if __name__ == "__main__":
    argument_clinic()