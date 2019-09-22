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

scoreboard = {} #Only run if you want to reset the scoreboard


#Input is # of turns remaining. Will return a hangman diagram.
def judgment_day(turn):
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
def remaining_chances(turn):
    chances = abs(turn - 6)
    if chances > 1:
        print("You have", chances, "chances remaining.", judgment_day(turn))
    if chances == 1:
        print("You have", chances, "chance remaining.", judgment_day(turn))

#Input is how many times the user has input something that is not a valid option.
#Program responses get increasingly frustrated and sad as time goes on.
def growing_frustration(wrongentry, guess, prevguess, turn):
    wrongentry +=1
    if wrongentry <= 5:
        if guess in prevguess:
            print("\n\nYou've already guessed that letter! Please guess again!")
            remaining_chances(turn)
        else:
            print("\n\nPlease try again and just enter a single letter.")
            remaining_chances(turn)
    if wrongentry >5 and wrongentry <= 10:
        if guess in prevguess:
            print("\n\nPay attention to the previous guesses. Come on now. Please guess again!")
            remaining_chances(turn)
        else:
            print("\n\nCome on, you know that's not a single letter. You can do this. Please enter just a single letter.\n")
            remaining_chances(turn)
    if wrongentry >10 and wrongentry <=20:
        if guess in prevguess:
            print("\n\nAre you trying to test me or something? You've tried that already. It's not going to help you anymore. I'm starting to get irritated. Try again. Correctly this time.")
            remaining_chances(turn)
        else:
            print("\n\nWhy are you doing this? Do you not know what a letter is? I'll help. A, B, C, D, E...those are all letters. You're getting annoying. Now try again.\n")
            remaining_chances(turn)
    if wrongentry > 20 and wrongentry < 50:
        despair = ["\n\nStop. Please stop.", 
                   "\n\nWhy are you doing this? Don't actually tell me. Just enter a correct value.", 
                   "\n\nWhat is wrong with you? Do you not want to play?", 
                   "\n\nWhy? Just why? Actually, don't tell me why, because that will still not be doing what I'm asking.",
                   "\n\nI think I might hate you? And I'm not sentient...", 
                   "\n\nWhat's the point of this? Or anything, really.",
                   "\n\nI'm disappointed in you.",
                   "\n\nENTER THE CORRECT VALUE.",
                   "\n\nI wish you never played this game."]
        print(despair[random.randint(0,len(despair)-1)])
        remaining_chances(turn)
    if wrongentry >= 50:
        print("\n\n ;_;")
        remaining_chances(turn)
    return wrongentry

#Get user's name
def get_name():
    name = input("Please enter your name:")
    if len(name) > 15:
        name = name[0:14]
    name = name + " " + strftime("%H:%S:%M", gmtime())
    return name

#Input is a string that should be easy, medium, or hard.
#will download and select a word according to difficulty
def word_difficulty(response):
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
        word = word.upper()
    else:
        word = "ZEBRA"
        print(word)
        points = 0
    return word, points

#Choose a word dependent upon the desired difficulty level. Also assign point values
def get_word():
    n = 1
    while n==1:
        difficulty = input("Please type in a word difficulty level: Easy, Medium, or Hard.")
        if difficulty.isalpha():
            difficulty = difficulty.upper()
            difficultylevel = ["EASY", "MEDIUM", "HARD", "E", "M", "H", "ADMIN"]
            if difficulty in difficultylevel:
                word, points = word_difficulty(difficulty)
                n+=1
                return word, points
            else:
                print("Not a valid difficulty level. Please try again.")
        else:
            print("Not a valid difficulty level. Please try again.")

#Show scoreboard for participant and previous participants at the end
def show_scores(scoreboard):
    print("\nCurrent Scoreboard")
    order = sorted(scoreboard, key=scoreboard.get, reverse=True)
    for i in range(len(order)):
        if i <10:
            print(order[i][0:(len(order[i])-8)], 
                  "."*(35-len(str(scoreboard[order[i]]))-len(order[i])+8), 
                  scoreboard[order[i]])
        else:
            del scoreboard[order[i]] #Keep scoreboard only 10 names long.


#### ACTUAL PROGRAM  ####
def hang_man():
    for turn in range(6):
        if turn == 0: 
            print("\n\nWelcome to Hangman!\n") #Only shown once
            wrongentry=0 #keep track of how many times someone has entered the wrong thing
            name = get_name()
            word, points = get_word()
            scoreboard[name] = 0
            tempword = [] #placeholder to show progress in checking the word
            prevguess = [] #display previous guesses.
            for char in word:
                tempword.append("_") #make spaces equal to number of characters in word
        remaining_chances(turn) #Show user how many chances are remaining
        print("Your word is:")
        while turn <=5: #This loop checks if input is correct. If not, it rejects it.
            print("\n", *tempword, sep=" ")
            print("Previously guessed:", *prevguess, sep=" ")
            guess = input("Please guess a letter:")
            if guess.isalpha():
                guess = guess.upper()
                if len(guess)==1 and guess not in prevguess: #if it's a single letter, it's correct
                    prevguess.append(guess)
                    break #kill the infinite loop.
                else:
                    wrongentry = growing_frustration(wrongentry, guess, prevguess, turn)
            else:
                wrongentry = growing_frustration(wrongentry, guess, prevguess, turn)
        newturn = turn #I want to continue this cycle and not deduct a turn unless they guess wrong.
        while newturn == turn: #this loop actually checks if the guess is in the word
            if guess in word:
                for i in range(len(word)):
                    if guess == word[i]:
                        tempword[i]=guess
                        scoreboard[name] += points
                if "".join(tempword) == word: #identify if guess now matches the full word
                    print("\n", *tempword, sep=" ")
                    print("\n\nCongratulations! You won!", alive)
                    scoreboard[name] += 5*points + points*abs(6-turn)
                    newturn -= 1
                    break #break to end loop and end game
                else:
                    print("\n\nGood job, now guess again!")
                    remaining_chances(turn)
                while turn <=5: #Need to add this so additional turns don't count if they keep being correct.
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
                            wrongentry = growing_frustration(wrongentry, guess, prevguess, turn)
                    else:
                        wrongentry = growing_frustration(wrongentry, guess, prevguess, turn) 
            if guess not in word:
                if turn < 5:
                    print("\n\nSorry, try again!")
                    newturn -= 1
                if turn == 5:
                    print("\n\nYou lose!", dead)
                    print("Your word was:", word)
                    show_scores(scoreboard)
                    break
        if "".join(tempword) == word: #If you've won, kill the game
            show_scores(scoreboard)
            break

hang_man()