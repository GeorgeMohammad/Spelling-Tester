

class FileProcessing:
#Reads data from a file into a variable.
    def FileReader(self, fileName):
        try:
            open(fileName, "r")
        except IOError:
            print("Invalid file name.")
        else:
            fileI = open(fileName, "r")
            fileContents = fileI.read()
            return fileContents

#fileContents is a string
#Splits fileContents into a list at the character, delimiter.
    def FileSplitter (self, fileContents, delimiter):
        try:
            if type(fileContents) is not str:
                print(type(fileContents))
                raise ArgumentException1
            
        except Exception as ArgumentException1:
            print("Must enter a string for fileContents.")
        else:
            try:
                if ((type(delimiter) is not str) or (delimiter == "")):
                    raise ArgumentException2
            except Exception as ArgumentException2:
                print("Invalid Delimiter")
            else:
                return fileContents.split(delimiter)

#Test code
##obj = FileProcessing()
##
##print(obj.FileSplitter("s s", ""))
##data = obj.FileReader("words1.txt")
##
##
