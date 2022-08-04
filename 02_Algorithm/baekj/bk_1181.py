words_list = list(set(input() for i in range(int(input()))))
words_list = sorted(words_list, key=lambda x:(len(x),x))
for word in words_list:
    print(word)



for word in sorted(list(set(input() for i in range(int(input())))),key=lambda x:(len(x),x)):
    print(word)