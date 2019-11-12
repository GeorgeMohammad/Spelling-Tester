#User is a class describing a user of a spelling test progam.
class User:
#Input function for getting a string from the user. Also performs exception
#handling.
    def GetStrInput(self, prompt):
        try:
            if type(prompt) is not str:
                raise Exception
        except:
            print("Argument should be of type string.")
        else:
            userI = input(prompt)
            return userI
