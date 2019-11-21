class Score:
    def computeScore(self, userAnswer, answerKeyVal):
        if len(userAnswer) <= len(answerKeyVal):
            correctChars = [i for i in userAnswer if i in answerKeyVal]
            correctCharsNum = len(correctChars)
            percentCorrect = correctCharsNum/len(answerKeyVal)
            return percentCorrect
        else:
            print("Error. Answer Key contains less characters than user's \
                    answer")