import re

def count_words(string):
    """Return the number of words in the string."""
    lis = []
    for char in string:
        if char.isalnum() or char.isspace():
            lis.append(char)
        else:
            lis.append(" ")
    new_string = "".join(lis)
    new_string_words = new_string.split()
    return len(new_string_words)

def main():
    assert count_words("This is a string.") == 4
    assert count_words("Jesus Christ is LORD!!!") == 4
    assert count_words("Blessed are the poor in spirit: for theirs is the"\
                       " kingdom of heaven.") == 13

if __name__ == "__main__":
    main()
