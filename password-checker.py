pwd = input("Enter a password: ")
print ("Password: " + "*" * len(pwd))

if len(pwd) < 4:
    print("Very weak ❌")
elif len(pwd) < 8:
    print("Medium 🔸")
else:
    print("Strong ✅")
