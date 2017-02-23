from palindrome import clean_up


def is_palindrome(sentence):
    verdict = False
    clean_sentence = clean_up(sentence)
    if clean_sentence == clean_sentence[::-1]:
        verdict = True
    return verdict


def main():
    user_input = input("enter some text to determine if it is a palindrome: ")
    if is_palindrome(user_input):
        print("is a palindrome")
    else:
        print("is not a palindrome")


if __name__ == '__main__':
    main()
