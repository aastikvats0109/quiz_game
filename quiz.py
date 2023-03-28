import json
def createQuiz():
    print("Welcome to the quiz")
    n = int(input("Enter the no of questions you want to set for quiz!!!: "))
    dict = {}
    for i in range(n):  # loop for adding the questiions
        k = input("Enter the question: ")
        v = input("Enter the answer: ")
        dict.update({k: v})
    with open('./data.json', "w") as dataFile:
        json.dump(dict, dataFile)


def playQuiz():
    # print("Quiz Started")
    myQuizData = open("./data.json", "r")
    allQuestions = json.load(myQuizData)
    question = len(allQuestions)
    score = 0
    for x in allQuestions:
        print(x)
        answer = input("Ans: ")
        if allQuestions[x] == answer:
            print("correct")
            score +=1
        else:
            print("Incorrect")

    myQuizData.close()

    print((score/question)*100)


def start():  # To call the strat funtion
    print("press 1 to create a quiz\npress 2 to play quiz.")
    userInput = input().strip()
    if userInput == "1":
        createQuiz()
    elif userInput == "2":
        playQuiz()
    else:
        print("You entered wrong digit.")


start()
