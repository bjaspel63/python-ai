import speech_recognition as sr
import webbrowser

rec = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something:")
    audio = rec.listen(source)

try:
    command = rec.recognize_google(audio).lower()
    if "youtube" in command:
        print("Opening YouTube...")
        webbrowser.open("https://www.youtube.com")
    else:
        print("Command not recognized.")
except:
    print("Couldn't understand you.")