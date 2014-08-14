# this function takes a string and returns True if string is palindrome
def is_palindrome(string):
    return (string == string.reversed())

def main():

    test_strings = [
            "Not a palindrome",
            "racecar",
            "RaceCar",
            "10001888088810001",
            "!@#$%^&*()*&^%$#@!",
            ]

    for test_string in test_strings:
        print "{0} : {1}".format(test_string, is_palindrome(test_string))

if __name__ == "__main__":
    main()
