# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 15:52:43 2019

@author: Kathryn
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 18:14:07 2019

@author: Kathryn
"""

##Actual code

########    RUN BEFORE RUNNING PROGRAM    ###########
import requests
import random
from time import gmtime, strftime

difficultylevel = ["EASY", "MEDIUM", "HARD", "E", "M", "H", "ADMIN"]

scoreboard = {} #Only run if you want to reset the scoreboard

#Input is a string that should be easy, medium, or hard.
#will download and select a word according to difficulty
def worddifficulty(response):
    if response == "EASY" or response=="E":
        points=1
        a = random.randint(1,2)
    if response == "MEDIUM" or response =="M":
        points=1.5
        a=random.randint(3,6)
    if response == "HARD" or response == "H":
        points = 2
        a=random.randint(7,10)
    if response != "ADMIN":
        parameters={"difficulty": a}
        poswords = requests.get("http://app.linkedin-reach.io/words", params=parameters)
        word = poswords.text.splitlines()[random.randint(0, (len(poswords.text.splitlines())-1))]
    else:
        word = "zebra"
        print(word)
        points = 0
    return word, points


#Input is # of turns remaining. Will return a hangman diagram.
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

#Input is integer for # of chances. Will return grammatically correct statement on how many are left.
def remainingchances(chances):
    if chances > 1:
        print("You have", chances, "chances remaining.", judgmentday(turn))
    if chances == 1:
        print("You have", chances, "chance remaining.", judgmentday(turn))

#Input is how many times the user has input something that is not a valid option.
#Program responses get increasingly sad as time goes on.
def growingfrustration(wrongentry):
    wrongentry +=1
    if wrongentry <= 5:
        if guess in prevguess:
            print("\n\nYou've already guessed that letter! Please guess again!")
            remainingchances(chances)
        else:
            print("\n\nPlease try again and just enter a single letter.")
            remainingchances(chances)
    if wrongentry >5 and wrongentry <= 10:
        if guess in prevguess:
            print("\n\nPay attention to the previous guesses. Come on now. Please guess again!")
            remainingchances(chances)
        else:
            print("\n\nCome on, you know that's not a single letter. You can do this. Please enter just a single letter.\n")
            remainingchances(chances)
    if wrongentry >10 and wrongentry <=20:
        if guess in prevguess:
            print("\n\nAre you trying to test me or something? You've tried that already. It's not going to help you anymore. I'm starting to get irritated. Try again. Correctly this time.")
            remainingchances(chances)
        else:
            print("\n\nWhy are you doing this? Do you not know what a letter is? I'll help. A, B, C, D, E...those are all letters. You're getting annoying. Now try again.\n")
            remainingchances(chances)
    if wrongentry > 20 and wrongentry < 50:
        despair = ["Stop. Please stop.", "Why are you doing this? Don't actually tell me. Just enter a correct value.", 
                   "What is wrong with you? Do you not want to play?", 
                   "Why? Just why? Actually, don't tell me why, because that will still not be doing what I'm asking.",
                   "I think I might hate you? And I'm not sentient...", 
                   "What's the point of this? Or anything, really.",
                   "I'm disappointed in you.",
                   "ENTER THE CORRECT VALUE.",
                   "I wish you never played this game."]
        print(despair[random.randint(0,len(despair)-1)])
        remainingchances(chances)
    if wrongentry >= 50:
        print(";_;")
        remainingchances(chances)
    return wrongentry


#input is an aritrary number 1 to maintain the loop until a difficulty level and word is chosen
def determineword(n):
    while n == 1: 
        name = input("Please enter your name:")
        name = name + " " + strftime("%H:%S:%M", gmtime())
        difficulty = input("Please type in a word difficulty level: Easy, Medium, or Hard.")
        if difficulty.isalpha():
            difficulty = difficulty.upper()
            if difficulty in difficultylevel:
                word, points = worddifficulty(difficulty)
                n+=1
                return name, word, points
            else:
                print("Not a valid difficulty level. Please try again.")
        else:
            print("Not a valid difficulty level. Please try again.")

determineword(1)

def showscores(scoreboard):
    print("Current Scoreboard")
    order = sorted(scoreboard, key=scoreboard.get, reverse=True)
    for i in range(len(order)):
        print(order[i][0:(len(order[i])-8)], "--------", scoreboard[order[i]])

#### ACTUAL PROGRAM  ####

for turn in range(6):
    if turn == 0: #If I decide to do difficulty levels, lets do this, but it's not necessary
        print("\n\nWelcome to Hangman!\n") #Find a way where this is only exprsesed the first time
        wrongentry=0 #keep track of how many times someone has entered the wrong thing
        n = 1 #must be 1 for determineword loop
        name, word, points = determineword(n)
        scoreboard[name] = 0
        print(points)
        word = word.upper() #want everything in caps to make things consistent
        tempword = [] #placeholder to show progress in checking the word
        prevguess = [] #display previous guesses.
        for char in word:
            tempword.append("_") #make spaces equal to number of characters in word
    chances = abs(turn - 6) 
    remainingchances(chances) #Show user how many chances are remaining
    print("Your word is:")
    blank = ""
    while turn <=6: #This loop checks if input is correct. If not, it rejects it.
        print("\n", *tempword, sep=" ")
        print("Previously guessed:", *prevguess, sep=" ")
        guess = input("Please guess a letter:")
        if guess.isalpha():
            guess = guess.upper()
            if len(guess)==1 and guess not in prevguess: #if it's a single letter, it's correct
                prevguess.append(guess)
                break #kill the infinite loop.
            else:
                wrongentry = growingfrustration(wrongentry)
        else:
            wrongentry = growingfrustration(wrongentry)
    newturn = turn #I want to continue this cycle and not deduct a turn unless they guess wrong.
    while newturn == turn: #this loop actually checks if the guess is in the word
        if guess in word:
            for i in range(len(word)):
                if guess == word[i]:
                    tempword[i]=guess
                    scoreboard[name] += 1*points
            if blank.join(tempword) == word: #identify if guess now matches the full word
                print("\n", *tempword, sep=" ")
                print("\n\nCongratulations! You won!", alive)
                newturn -= 1
                break #break to end loop and end game
            else:
                print("\n\nGood job, now guess again!")
                remainingchances(chances)
            while turn <=6: #Need to add this so additional turns don't count if they keep being correct.
                print("\n", *tempword, sep=" ")
                print("Previously guessed:", *prevguess, sep=" ")
                guess = input("Please guess a letter:")
                if guess.isalpha():
                    guess = guess.upper() #Need to prevent prevguess from counting capital and lowercase
                    if len(guess)==1 and guess not in prevguess: #if it's a single letter, it's correct
                        guess = guess.upper()
                        prevguess.append(guess)
                        break #kill the infinite loop.
                    else:
                        wrongentry = growingfrustration(wrongentry)
                else:
                    wrongentry = growingfrustration(wrongentry) 
        if guess not in word:
            if turn < 5:
                print("\n\nSorry, try again!")
                scoreboard[name] -= .25
                newturn -= 1
            if turn == 5:
                print("\n\nYou lose!", dead)
                print("Your word was:", word)
                scoreboard[name] -= .25
                showscores(scoreboard)
                break
    if blank.join(tempword) == word: #If you've won, kill the game
        showscores(scoreboard)
        break
