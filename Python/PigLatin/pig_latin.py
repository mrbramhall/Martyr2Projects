import re

# These are the needed Pig Latin initial to final letter conversions.
pl_conversions = {
    "a": "-ay",
    "b": "-bay",
    "c": "-cay",
    "d": "-day",
    "e": "-ey",
    "f": "-fay",
    "g": "-gay",
    "h": "-hay",
    "i": "-iy",
    "j": "-jay",
    "k": "-kay",
    "l": "-lay",
    "m": "-may",
    "n": "-nay",
    "o": "-oy",
    "p": "-pay",
    "q": "-quay",
    "r": "-ray",
    "s": "-say",
    "t": "-tay",
    "u": "-uy",
    "v": "-vay",
    "w": "-way",
    "x": "-xay",
    "y": "-yay",
    "z": "-zay",
}

def pig_latin(string):
    """Return Pig Latin version of the given string."""
    word_conversions = {}
    words_of_string = re.sub("[^\w]", " ", string).split()
    for word in words_of_string:
        word_conversions[word] = _pig_latin_word(word)
    return replace_all(string, word_conversions)

def _pig_latin_word(word):
    """Return the Pig Latin version of the given word."""
    pl_word = ""
    if word[0].isupper():
        pl_word = word[1].upper() + word[2:]\
                  + pl_conversions.get(word[0].lower())
    else:
        pl_word = word[1:] + pl_conversions.get(word[0])
    return pl_word

def replace_all(text, dic):
    for i, j in dic.iteritems():
        text = text.replace(i, j)
    return text

def main():
    print pig_latin("Jesus is Lord!")
    print pig_latin("Fear not, only believe.")
    print pig_latin("STRING")
    print pig_latin("He that dwelleth in the secret place of the most High"\
                    " shall abide under the shadow of the Almighty.")

if __name__ == "__main__":
    main()
