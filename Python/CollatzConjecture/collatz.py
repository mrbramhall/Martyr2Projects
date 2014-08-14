# an algorithm that processes an input according to the collatz
# conjecture
def collatz(num):

    if num < 1:
        raise Exception("Input integer needs to be greater than 0.")
    else:
        count = 0
        while num != 1:
            if num % 2 == 0:
                num /= 2
            else:
                num = (num * 3) + 1
            count += 1
        return count

def main():

    x = range(100)
    y = [collatz(i) for i in x]

if __name__ == "__main__":
    main()
