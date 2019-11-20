import pyttsx3
class Text2Speech:
#The speak function was based on some code on:
#https://www.devdungeon.com/content/text-speech-python-pyttsx3
    def Speak(self, speechStr, volumeFloat = .9, speechRate = 250):
        msg = pyttsx3.init()
        try:
            float(volumeFloat)
        except:
            print("You should use a float for the volume value.")
        else:
            msg.setProperty("volume", volumeFloat)

        try:
            int(speechRate)
        except:
            print("You should use an int for the speech rate")
        else:
            msg.setProperty("rate", speechRate)
        try:
            str(speechStr)
        except:
            print("You should use a string for the speech string message")
        else:
            msg.say(speechStr)
            
        msg.runAndWait()
