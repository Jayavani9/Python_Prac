print("Welcome to the Quiz !!")

playing = input(" Do you want to play ?")

if playing.lower() != "yes":
    quit()

print("Let's Play !!")
score = 0
ans = input("What is the acronym of VPN?")

if ans.lower() == "virtual private network":
    print("Wohoo!!! Correct answer")
    score += 1
else:
    print("Incorrect!")

ans = input("What is the acronym of GPU?")

if ans.lower() == "graphics processing unit":
    print("Wohoo!!! Correct answer")
    score += 1
else:
    print("Incorrect!")

ans = input("What is the acronym of CPU?")

if ans.lower() == "central processing unit":
    print("Wohoo!!! Correct answer")
    score += 1
else:
    print("Incorrect!")

ans = input("What is the acronym of CC?")

if ans.lower() == "carbon copy":
    print("Wohoo!!! Correct answer")
    score += 1
else:
    print("Incorrect!")

print("Your score is:", score)
print("You scored",(score*100)/4, "%")