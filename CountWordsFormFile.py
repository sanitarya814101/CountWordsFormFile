def CountWordsFormFile():
    filename = input("Enter the file name: ")
    file = open(filename, 'r')
    numbreOfWords = 0
    numbreOfLines = 0

    for line in file:
        words = line.split()
        lines = line.splitlines()
        numbreOfWords = numbreOfWords+len(words)
        numbreOfLines = numbreOfLines+len(lines)

    print("Number of words: ", numbreOfWords)
    print("Number of lines: ", numbreOfLines)


CountWordsFormFile()
