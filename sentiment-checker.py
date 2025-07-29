happy = ["happy", "good", "awesome", "great", "love"]
sad = ["sad", "bad", "terrible", "hate", "angry"]

text = input("How are you feeling today? ").lower()

if any(word in text for word in happy):
    print("Sounds positive! 😊")
elif any(word in text for word in sad):
    print("Oh no! Stay strong 💪")
else:
    print("Hmm… I can't tell 🤔")
