import random
class Random:
    def randNumMaker(self, startInt, stopInt):
        try:
            if ((type(startInt) is not int) or (type(stopInt) is not int)):
                raise Exception
        except:
            print("Error. One or more arguments is not an integer.")
        else:
            randomNum = random.randrange(startInt, stopInt)
            return randomNum

#Test code
##randObj = Random()
##print(randObj.randNumMaker(1, 20))
##print(randObj.randNumMaker("f", 20))
##print(randObj.randNumMaker(1, "f"))
##print(randObj.randNumMaker("f", "f"))
##print(randObj.randNumMaker(1.0, 20.0))
##print(randObj.randNumMaker(1.0, 20))
##print(randObj.randNumMaker(1, 20.0))
##print(randObj.randNumMaker(True, 20))
##print(randObj.randNumMaker(1, True))
##print(randObj.randNumMaker(True, True))
##print(randObj.randNumMaker(1, 20))
