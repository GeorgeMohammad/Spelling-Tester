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
