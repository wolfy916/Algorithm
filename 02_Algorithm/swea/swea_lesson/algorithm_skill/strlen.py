def strlen(s):
    i = 0
    while s[i] != '\0':
        i += 1
    return i

a = ['a', 'b', 'c', '\0']
print(strlen(a))