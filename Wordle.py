import random
import soundfile as sf
import soundcard as sc
default_speaker = sc.default_speaker()
with open('words.txt') as f:
    lines = f.readlines()
    words = [line.strip() for line in lines]
def isword(user_word,wordly_word):
    for x in user_word:
        print(x,end=" ")
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

random_word = random.choice(words)
print(random_word)
print("Let's Play Wordle")
message,i  = {5:"Marvelluos",4:"Excellent",3:"Very good",2:"Nice",1:"Good",0:"Ok"},6
while i>0:
    user_word=input("\nEnter word: ")
    user_word = user_word.lower()
    if (len(user_word)==5 and user_word.isalpha()):
        i = i-1
        if isword(user_word,random_word):
                print("\n",message[i])
                samples, samplerate = sf.read('rightanswer.wav')
                default_speaker.play(samples, samplerate=samplerate)
                break
        else:
            samples, samplerate = sf.read('wronganswer.wav')
            default_speaker.play(samples, samplerate=samplerate)
            continue
    else:
        print("Please enter a valid word")
else:
    print("Game over")
