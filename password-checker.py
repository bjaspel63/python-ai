pwd = input("Enter a password: ")

if len(pwd) < 4:
    print("Very weak ❌")
elif len(pwd) < 8:
    print("Medium 🔸")
else:
    print("Strong ✅")
