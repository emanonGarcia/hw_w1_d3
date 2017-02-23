import sys
from palindrome import is_palindrome


def main():
    try:
        print("\nChecking: " + sys.argv[1])
        with open(sys.argv[1], 'r') as f:
            for each_line in f:
                if is_palindrome(each_line.strip()):
                    print("is a palindrome")
                else:
                    print("is not a palindrome")
    except FileNotFoundError:
        print("FileNotFoundError: Are you in the right directory?")
    except IndexError:
        print("IndexError: You didn't give me a file")


if __name__ == "__main__":
    main()
