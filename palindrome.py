################ Can you explain this? #######################
#                                                            #
# regex = re.compile('[%s]' % re.escape(string.punctuation)) #
# clean_str = regex.sub('', dirty_str)                       #
#                                                            #
################ Can you explain this? #######################

import string


def clean_up(dirty_str):
    for i in dirty_str:
        if i in string.punctuation:
            dirty_str = dirty_str.replace(i, '')

    return dirty_str.replace(" ", "").lower()


def is_palindrome(sentence):
    sentence = clean_up(sentence)
    if len(sentence) < 2:
        return True
    if sentence[0] != sentence[-1]:
        return False
    return is_palindrome(sentence[1:-1])


def main():
    user_input = input("enter some text to determine if it is a palindrome: ")
    if is_palindrome(user_input):
        print("is a palindrome")
    else:
        print("is not a palindrome")


if __name__ == "__main__":
    main()
