import random

def random_add():
    """
    Return the result obtained from adding two random numbers, each
    ranging from 0.0 to 1.0.
    """
    first_num = random.random()
    second_num = random.random()
    result = first_num + second_num
    return result

def main():

    # print 10 results generated by random_add
    for x in xrange(10):
        print random_add()

if __name__ == "__main__":
    main()
