import pyttsx3
class Text2Speech:
#The speak function was based on some code on:
#https://www.devdungeon.com/content/text-speech-python-pyttsx3
    def Speak(self, speechStr, volumeFloat = .9, speechRate = 250):
        msg = pyttsx3.init()
        msg.setProperty("rate", speechRate)
        msg.setProperty("volume", volumeFloat)
        msg.say(speechStr)
        msg.runAndWait()
