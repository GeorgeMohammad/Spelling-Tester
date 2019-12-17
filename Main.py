import Words
import User
import Text2Speech
import Score

#test data
wordList = ["test", "test2", "test3"]

words = Words.Words()
user1 = User.User()
speech = Text2Speech.Text2Speech()
score = Score.Score()

testChoice = input("q)uit, anything else to continue: ")

while (testChoice.lower() != "q"):
    word = words.getRandVal(wordList)
    userGuess = user1.GetStrInput("Enter your answer to :" + word)
    userScore = score.ComputeScore(userGuess, word)
    print("Score:", userScore)
    testChoice = input("q)uit, anything else to continue: ")
