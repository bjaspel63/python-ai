name = input("Hi! What's your name? ")
print(f"Nice to meet you, {name}!")

while True:
    ask = input("Do you remember my name? (yes/no/exit): ")
    if ask == "exit":
        break
    elif ask == "yes":
        print(f"Yes! It's {name}.")
    elif ask == "no":
        print(f"Oops! It's {name}.")
