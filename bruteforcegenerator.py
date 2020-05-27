def splice(text, insert, location):
    locCounter = 0
    preText = ''
    while(locCounter < location):
        preText += text[locCounter]
        locCounter += 1
    postText = ''
    while(locCounter < len(text)):
        postText += text[locCounter]
        locCounter += 1
    result = str(str(preText) + str(insert) + str(postText))
    return result

path = input("Path to input file: ");
#lettersList = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
lettersList = "abcdefghijklmnopqrstuvwxyz"
if(path == ''):
    path = "swords.txt"
output = open("output.txt", "w+")
i = 0
swordListFile = open(path, 'r')
swords = swordListFile.readlines()
swordCounter = 0
print(len(swords))
while(i < len(swords)):
    posCounter = 1

    while(posCounter < len(swords[i])):
        letterCounter = 0
        while(letterCounter < len(lettersList)):
            sword = splice(swords[i], lettersList[letterCounter], posCounter)
            print(sword.upper())
            output.write(sword.upper())
            letterCounter += 1
        posCounter += 1
    

    
    i += 1


output.flush()
output.close()
