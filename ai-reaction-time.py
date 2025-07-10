import time, random

print("Get ready...")
time.sleep(random.randint(2, 5))
print("Go!")

start = time.time()
input("Press Enter as fast as you can!")
end = time.time()

print("Your reaction time:", round(end - start, 3), "seconds")