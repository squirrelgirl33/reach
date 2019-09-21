# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 18:14:07 2019

@author: Kathryn
"""



##Actual code

########    RUN BEFORE RUNNING PROGRAM    ###########
import requests
import random

difficultylevel = ["EASY", "MEDIUM", "HARD"]

#Input is a string that should be easy, medium, or hard.
#will download and select a word according to difficulty
def worddifficulty(response):
    if response == "EASY":
        a = random.randint(1,3)
    if response == "MEDIUM":
        a=random.randint(4,7)
    if response == "HARD":
        a=random.randint(8,10)
    parameters={"difficulty": a}
    poswords = requests.get("http://app.linkedin-reach.io/words", params=parameters)
    word = poswords.text.splitlines()[random.randint(0, (len(poswords.text.splitlines())))]
    return word

def judgmentday(turn):
    if turn==0:
        hang = r"""\
        
              _____
              |   |
                  |
                  |
                  |
               ___|___
                """
    if turn==1:
        hang = r"""\
        
              _____
              |   |
              O   |
                  |
                  |
               ___|___
                """
    if turn==2:
        hang = r"""\
        
              _____
              |   |
              O   |
              |   |
                  |
               ___|___
                """
    if turn==3:
        hang = r"""\
        
              _____
              |   |
              O   |
             -|   |
                  |
               ___|___
                """
    if turn==4:
        hang = r"""\
        
              _____
              |   |
              O   |
             -|-  |
                  |
               ___|___
                """
    if turn ==5:
        hang = r"""\
        
              _____
              |   |
              O   |
             -|-  |
             /    |
               ___|___
                """

    return hang


dead = r"""\

              _____
              |   |
              O   |
             -|-  |
             / \  |
               ___|___
                """
                
alive = r"""\

              _____
              |   |
                  |
         \O/      |
          |       |
         / \   ___|___
                """


#### ACTUAL PROGRAM  ####

for turn in range(6):
    if turn == 0: #If I decide to do difficulty levels, lets do this, but it's not necessary
        print("Welcome to Hangman!\n") #Find a way where this is only exprsesed the first time
        n = 1
        while n == 1: 
            difficulty = input("Please type in a word difficulty level: Easy, Medium, or Hard.")
            difficulty = difficulty.upper()
            if difficulty in difficultylevel:
                word = worddifficulty(difficulty)
                n+=1
            else:
                print("Not a valid difficulty level. Try again.")
        word = word.upper() #want everything in caps to make things consistent
        print(word) #delete this later, but need this to test out certain cases
        tempword = []
        prevguess = []
        for char in word:
            tempword.append("_")
    chances = abs(turn - 6)
    if chances > 1:
        print("You have", chances, "chances remaining.", judgmentday(turn))
    if chances == 1:
        print("You have", chances, "chance remaining.", judgmentday(turn))
    print("Your word is:")
    #print("\n", *tempword, sep=" ")
    blank = ""
    while turn <=6: #Need this inside of while so if someone enters more than a single letter, it does not count against them.
        print("\n", *tempword, sep=" ")
        print("Previously guessed:", *prevguess, sep=" ")
        guess = input("Please guess a letter:")
        if guess.isalpha():
            guess = guess.upper()
            if len(guess)==1 and guess not in prevguess: #if it's a single letter, it's correct
                prevguess.append(guess)
                break #kill the infinite loop.
            if guess in prevguess:
                print("\n\nYou've already guessed that letter! Guess again!") #this one will not reprint spaces
                print("You have", chances, "chances remaining.", judgmentday(turn))
            else:
                print("\n\nPlease try again and just enter a single letter. You can do better than this.") #this one does not show spaces
                print("You have", chances, "chances remaining.", judgmentday(turn))
        else:
            print("\n\nPlease try again and just enter a single letter. Why would you do otherwise?\n")
            print("You have", chances, "chances remaining.", judgmentday(turn))
    newturn = turn #I want to continue this cycle and not deduct a turn unless they guess wrong.
    while newturn == turn:
        if guess in word: #Identify if guess is in word
            for i in range(len(word)):
                if guess == word[i]:
                    tempword[i]=guess
            blank = ""
            if blank.join(tempword) == word: #identify if guess now matches the full word
                print("\n", *tempword, sep=" ")
                print("\n\nCongratulations! You won!", alive)
                newturn -= 1
                break #break to end loop and end game
            else:
                print("\n\nGood job, now guess again!")
                print("You have", chances, "chances remaining.", judgmentday(turn))
            while turn <=6: #Need this inside of while so if someone enters more than a single letter, it does not count against them.
                print("\n", *tempword, sep=" ")
                print("Previously guessed:", *prevguess, sep=" ")
                guess = input("Please guess a letter:")
                if guess.isalpha():
                    guess = guess.upper() #Need to prevent prevguess from counting capital and lowercase
                    if len(guess)==1 and guess not in prevguess: #if it's a single letter, it's correct
                        guess = guess.upper()
                        prevguess.append(guess)
                        break #kill the infinite loop.
                    if guess in prevguess:
                        print("\n\nYou've already guessed that letter! Guess again! \n")
                        print("You have", chances, "chances remaining.", judgmentday(turn))
                    else:
                        print("\n\nPlease try again and just enter a single letter. Do not prolong this agony. \n")
                        print("You have", chances, "chances remaining.", judgmentday(turn))
                else:
                    print("\n\nPlease try again and just enter a single letter. I beg you.\n") #does not show spaces
                    print("You have", chances, "chances remaining.", judgmentday(turn))
        if guess not in word:
            if turn < 5:
                print("\n\nSorry, try again!")
                newturn -= 1
            if turn == 5:
                print("\n\nYou lose!", dead)
                print("Your word was:", word)
                break
    if blank.join(tempword) == word:
        break
    


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

if x not in prac:
    print("gosl")

a = ""
prac = ["G", "H", "C"]

a.join(prac)

letter = "j"

inputcheck(letter, prac, 6)

letter, prac = inputcheck(letter, prac, 6)


def inputcheck(guess, prevgues):
    if guess.isalpha():
        guess = guess.upper()
        if len(guess)==1 and guess not in prevguess: #if it's a single letter, it's correct
            return guess, prevguess
        
        if guess in prevguess:
            print("You've already guessed that letter! Guess again!")
            print("You have", chances, "chances remaining.")
        else:
            print("Please try again and just enter a single letter. Imagine me saying this in the saddest, most disappointed voice possible.")
            print("You have", chances, "chances remaining.")
    else:
        print("Please try again and just enter a single letter. Imagine me saying this in the saddest, most disappointed voice possible.")
        print("You have", chances, "chances remaining.")
