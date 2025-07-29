import random

items = ["🍒","🍋","⭐","🍇"]

while True:
    spin = [random.choice(items) for _ in range(3)]
    print(" | ".join(spin))
    if len(set(spin)) == 1:
        print("Jackpot! 🎉")
        break
    if input("Spin again? (y/n): ") == "n":
        break
