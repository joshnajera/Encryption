import Matrix
chunkSize = len(Matrix.encypter)

def stringToIntBlocks (stringToConvert):
    tempNumString = []
    numString = []

    for char in stringToConvert:
        tempNumString.append(ord(char))

    while len(tempNumString)%chunkSize > 0:
        tempNumString.append(0)
    print(tempNumString)

    for x in range(0,int(len(tempNumString)/chunkSize)):
        numString.append([])
        for y in range(0,chunkSize):
            numString[x].append(0)
            numString[x][y]=tempNumString[(chunkSize*x)+y]

    print(numString)

def encrypt(numStringToEncrypt):
    return 0