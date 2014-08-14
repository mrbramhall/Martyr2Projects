# count the vowels in a string, returns dict of <letter, count>
def count_vowels(s):

    counts = {}

    for letter in s.lower():
        if letter in "aeiouy":
            if letter in counts:
                counts[letter] += 1
            else:
                counts[letter] = 1

    return counts

def main():
    print count_vowels("Jesus Christ is LORD.")

if __name__ == "__main__":
    main()
