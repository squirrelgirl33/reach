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
word

len(word)

input("Write something.")

word.isalpha()

ex = 4

pig = ex

prac = "zebra"

prac2 = ["a", "b", "c", "d"]
prac2[0]
prac2[0] = dog

dog = "g"

prac[2] = "j"

prac[2]

ex=ex-1
##Actual code
allwords = requests.get("http://app.linkedin-reach.io/words")

for turn in range(6): #I might need to change this to a while statement and subtract 1 to turn during
    print("Welcome to Hangman!")
    chances = abs(turn - 6)
    print("You have", chances, "chances remaining.")
    if turn == 0: #If I decide to do difficulty levels, lets do this, but it's not necessary
#        difficulty = int(input("Please select a difficult level: Easy, Medium, or Hard."))
#        difficulty = difficulty.upper()
        #ADD BELOW BACK LATER
        #word = allwords.text.splitlines()[random.randint(0, (len(allwords.text.splitlines())))] #randomly select a word
        word = "zebra"
        word = word.upper() #want everything in caps to make things consistent
        tempword = []
        for char in word:
            tempword.append("_")
    print("Your word is:", *tempword, sep=" ")
    while turn <=6: #Need this inside of while so if someone enters more than a single letter, it does not count against them.
        guess = input("Please guess a letter:")
        if guess.isalpha() and len(guess)==1: #if it's a single letter, it's correct
            guess = guess.upper()
            break #kill the infinite loop.
        else:
            print("Please try again and just enter a single letter.")
    newturn = turn #I want to continue this cycle and not deduct a turn unless they guess wrong.
    while newturn == turn:
        if guess in word:
            for i in range(len(word)):
                if guess == word[i]:
                    tempword[i]=guess
            print("Good job, now guess again!", *tempword, sep=" ")
            while turn <=6: #Need this inside of while so if someone enters more than a single letter, it does not count against them.
                guess = input("Please guess a letter:")
                if guess.isalpha() and len(guess)==1: #if it's a single letter, it's correct
                    guess = guess.upper()
                    break #kill the infinite loop.
                else:
                    print("Please try again and just enter a single letter.")
        if guess not in word:
            newturn -= 1
    
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

update("z", "zebra")