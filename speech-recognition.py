import speech_recognition as sr

rec = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something:")
    audio = rec.listen(source)

try:
    text = rec.recognize_google(audio)
    print("You said:", text)
except:
    print("Sorry, I didn't get that.")