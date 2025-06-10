wordCount = int(input())
listOfWords = []
for i in range(wordCount):
    word  = input()
    if(len(word) > 10):
        listOfWords.append(word[0] + str(len(word) - 2) + word[-1])
    else:
        listOfWords.append(word)
        
for word in listOfWords:
    print(word)    