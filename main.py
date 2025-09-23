import drawing
import random
import pathlib

highscore = 0

scorepath = pathlib.Path(__file__)
scorefile = scorepath.parent / "highscore.txt"

try:
    if scorefile.exists():
        with open("highscore.txt", "r") as h:
            highscore = h.read()
except FileNotFoundError:
    with open("highscore.txt", "x") as h:
        h.write("0")


life = 6
x = 0
y = 0
score = 0


categoryr = random.randint(0,2)
wordr = random.randint(0,4)

categories = ["Food", "Items", "Animals"]
pickedcat = categories[categoryr]

Food = ["hamburger", "fries", "salad", "soup", "rice"]
Items = ["lamp", "desk", "pen", "paper", "computer"]
Animals = ["cat", "dog", "jaguar", "elephant", "tiger"]

if pickedcat == "Food":
    pickedword = Food[wordr]
elif pickedcat == "Items":
    pickedword = Items[wordr]
else:
    pickedword = Animals[wordr]

separatedword = list(pickedword)
progress = []
wordlen = len(pickedword)
print(f"Highscore is {highscore} (the less the better)")
while x != wordlen:
    progress.append("_")
    x += 1  
while (life != 0) and (progress != separatedword):
    score = score + 1
    drawing.drawstickman(life)
    print(f"The category is {pickedcat}")
    print(" ".join(progress))
    guess = input("Try to guess a letter, or the whole word: ")
    if len(guess) == 1:
        if guess in separatedword:
            for y in range(wordlen):
                if separatedword[y] == guess:
                    progress[y] = guess
                else:
                    pass
        else:
            print("That guess was wrong..")
            life = life - 1
    elif guess == pickedword:
        progress = separatedword
    else:
        life = life - 1

if progress == separatedword:
    print("Congrats on beating the game!")
else:
    print("Better luck next time")

if score < int(highscore):
    with open("highscore.txt", "w") as b:
        b.write(str(score))    