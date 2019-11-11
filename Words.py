import Random
class Words:
    def getRandVal(self, targetList):
        randNumObj = Random.Random()
        try:
            if type(targetList) is not list:
                raise Exception
        except:
            print("Enter a value of type list.")
        else:
            randNum = randNumObj.randNumMaker(0, len(targetList))
            return targetList[randNum]

        
