# returns the given string with chars reversed
def reverse_string(s):
    reversed_s = ""
    for char in s[::-1]:
        reversed_s += char
    return reversed_s

def main():
    print reverse_string("This will be reversed.")

if __name__ == "__main__":
    main()
