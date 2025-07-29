#!/bin/python3

print("Think of an animal, I will try to guess! 🐾")

legs = int(input("How many legs (2 or 4)? "))
sound = input("Does it meow or bark? ")

if legs == 4 and "meow" in sound:
    print("You’re thinking of a Cat 🐱")
elif legs == 4 and "bark" in sound:
    print("You’re thinking of a Dog 🐶")
elif legs == 2:
    print("Maybe a Bird 🦜")
else:
    print("Hmm… I’m not sure 🤔")
