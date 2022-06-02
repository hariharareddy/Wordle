def isword(user_word,wordly_word):
    for x in user_word:
        print(x,end="  ")
    print()
    for i in range(len(user_word)):
        if user_word[i] == wordly_word[i]:
            print("🟩",end ="")
        elif user_word[i] in wordly_word:
            print("🟨",end="")
        else:
            print("⬛",end="")
    if user_word == wordly_word:
        return 1
    else:
        return 0

import random
words = open('words.txt')
words_list = []
for x in words:
    words_list.append(x.strip())
random_word = random.choice(words_list)
print(random_word)
for i in range(1,7):
    ip = input("\nEnter a five letter word:")
    ip = ip.lower()
    word = ip[0:5]
    if i==1:
        if isword(word,random_word):
            print("\nGenius")
            break
        else:
            continue
    elif i==2:
        if isword(word,random_word):
            print("\nMagnificent")
            break
        else:
            continue
    elif i==3:
        if isword(word,random_word):
            print("\nImpressive")
            break
        else:
            continue
    elif i==4:
        if isword(word,random_word):
            print("\nSplendid")
            break
        else:
            continue
    elif i==5:
        if isword(word,random_word):
            print("\nGreat")
            break
        else:
            continue
    else:
        if isword(word,random_word):
            print("\nPhew")
            break
else:
    print("End of Game, the correct word is:",random_word)