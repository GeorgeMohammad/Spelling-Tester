import Random
class Words:
    def getRandVal(self, targetList):
        randNumObj = Random.Random()
        randNum = randNumObj.randNumMaker(0, len(targetList))
        return targetList[randNum]


        
