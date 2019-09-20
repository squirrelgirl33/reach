# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 18:14:07 2019

@author: Kathryn
"""

import requests
import random

parameters={"difficulty": 10} #setting up difficulty

allwords = requests.get("http://app.linkedin-reach.io/words", params=parameters) #get the word dictionary


word = allwords.text.splitlines()[random.randint(0, (len(allwords.text.splitlines())))] #randomly select a word

##Actual code
allwords = requests.get("http://app.linkedin-reach.io/words")

for turn in range(6): #I might need to change this to a while statement and subtract 1 to turn during
    if turn == 0: #If I decide to do difficulty levels, lets do this, but it's not necessary
        print("Welcome to Hangman!") #Find a way where this is only exprsesed the first time
#        difficulty = int(input("Please select a difficult level: Easy, Medium, or Hard."))
#        difficulty = difficulty.upper()
        ###########ADD BELOW BACK LATER
        word = allwords.text.splitlines()[random.randint(0, (len(allwords.text.splitlines())))] #randomly select a word
        #word = "meatball"
        word = word.upper() #want everything in caps to make things consistent
        tempword = []
        prevguess = []
        for char in word:
            tempword.append("_")
    chances = abs(turn - 6)
    if chances > 1:
        print("You have", chances, "chances remaining.")
    if chances == 1:
        print("You have", chances, "chance remaining.")
    print("Your word is:")
    print(*tempword, sep=" ")
    while turn <=6: #Need this inside of while so if someone enters more than a single letter, it does not count against them.
        print("Previously guessed:", *prevguess, sep=" ")
        guess = input("Please guess a letter:")
        if guess.isalpha():
            guess = guess.upper()
            if len(guess)==1 and guess not in prevguess: #if it's a single letter, it's correct
                prevguess.append(guess)
                break #kill the infinite loop.
            if guess in prevguess:
                print("You've already guessed that letter! Guess again!")
            else:
                print("Please try again and just enter a single letter. Imagine me saying this in the saddest, most disappointed voice possible.")
        else:
            print("Please try again and just enter a single letter. Imagine me saying this in the saddest, most disappointed voice possible.")
    newturn = turn #I want to continue this cycle and not deduct a turn unless they guess wrong.
    while newturn == turn:
        if guess in word: #Identify if guess is in word
            for i in range(len(word)):
                if guess == word[i]:
                    blank = ""
                    tempword[i]=guess
                    if blank.join(tempword) == word:
                        print(*tempword, sep=" ")
                        print("Congratulations! You won!")
                        newturn -= 1
                    else:
                        print("Good job, now guess again!")
                        print("You have", chances, "chances remaining.")
                        print(*tempword, sep=" ")
            if blank.join(tempword) == word:
                break
            while turn <=6: #Need this inside of while so if someone enters more than a single letter, it does not count against them.
                print("Previously guessed:", *prevguess, sep=" ")
                guess = input("Please guess a letter:")
                if guess.isalpha():
                    guess = guess.upper() #Need to prevent prevguess from counting capital and lowercase
                    if len(guess)==1 and guess not in prevguess: #if it's a single letter, it's correct
                        guess = guess.upper()
                        prevguess.append(guess)
                        break #kill the infinite loop.
                    if guess in prevguess:
                        print("You've already guessed that letter! Guess again!")
                        print("You have", chances, "chances remaining.")
                    else:
                        print("Please try again and just enter a single letter.")
                        print("You have", chances, "chances remaining.")
                else:
                    print("Please try again and just enter a single letter. Imagine me saying this in the saddest, most disappointed voice possible.")
                    print("You have", chances, "chances remaining.")
        if guess not in word:
            if turn < 5:
                print("Sorry, try again!")
                newturn -= 1
            if turn == 5:
                print("You lose!")
                print("Your word was:", word)
                break
    if blank.join(tempword) == word:
        break
    
#need to add more statements, need to have it recognize when it's completed


def update(guess, word):
    tempword = []
    for char in word:
        tempword.append("_")
    for i in range(len(word)):
        if word[i]==guess:
            tempword[i]=guess
    print(*tempword, sep=" ")
    return

"cats".isalpha()

update("z", "zebra")

if x not in prac:
    print("gosl")

a = ""
prac = ["g", "h", "c"]

a.join(prac)