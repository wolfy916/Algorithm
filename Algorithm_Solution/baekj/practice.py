my_word = input()

def is_palindrome(some_word):
    if len(some_word) < 2:
        return True, some_word
    elif some_word[0] != some_word[-1]:
        return False, some_word
    else:
        some_word = some_word[1:-1]
        return is_palindrome(some_word)
constant = len(my_word)
count = 0
while True:
    if is_palindrome(my_word)[0]:
        print(constant + count)
        break
    else:
        my_word = my_word + my_word[0]
        count += 1
        my_word = is_palindrome(my_word)[1]