class FileIO:
    def Write2CSV(self, fileName, dataItem):
        if (fileName[len(fileName) - 3: len(fileName)] != "csv"):
            print("Invalid file name. Exiting.")
        else:
            fileO = open(fileName, 'a')
            fileO.write(dataItem + '\n')
            fileO.close()

