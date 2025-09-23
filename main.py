import drawing
import random

life = 6
x = 0

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
while x != wordlen:
    progress.append("")
    x += 1  
while life != 0:
    drawing.drawstickman(life)
    print(f"The category is {pickedcat}")
    print(progress)
    drawing.drawlines(wordlen)
    guess = input("Try to guess a letter, or the whole word: ")
    if len(guess) == 1:
            indexguess = separatedword.index(guess)
            indexguessend = separatedword.index(guess, indexguess)
            progress.pop(indexguess)
            progress.pop(indexguessend)
            progress.insert(indexguess, guess)
            progress.insert(indexguessend, guess)
            