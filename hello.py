name = input("What is your name? ")
print("Hello, " + name + "!")
sleep = input("How many hours do you sleep? ")
hours_on_minutes = float(sleep) * 60
print("You sleep for " + str(hours_on_minutes) + " minutes.")
if hours_on_minutes > 7 * 60:
    print("you slept enough")
else:
    print("you should sleep more")
