def countwordsFile():
    fileName = input(" Enter The File Name :- ")
    number_of_words = 0 
    file = open(fileName,"r")
    for line in file: 
        words = line.split()
        number_of_words += len(words)
    print("Number Of Words: ")
    print(number_of_words)

countwordsFile()


       