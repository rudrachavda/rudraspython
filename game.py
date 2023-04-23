from colorama import init #color library
from termcolor import colored #color text
import random
#gameword is the random word that the computer chooses from the lists as the word that can be changed or colored

#ALGORITHM
# 1. Ask user for the guess input word
# 2. If input word is same as game word then print something and exit
# 3. If input word is not same as game word then apply character match logic
# 4. If number of tries are less than the guessCount then repeat from step 1
# 5. Print something if the user doesn't guess the word. 


def startGame(): #start game function (used in the beginning user interface)
  wordCount = input('Would you like to play a 5 letter or 6 letter game?(type 5 or 6)\n') #ask user for 5 or 6 letter game
  gameWord = "" #resets the gameword
  guessCount = 0 #resets the amount of guesses the user had
  
  if wordCount == "5": #this reads the 5 words 
    lines = open("./5words.txt").readlines() #opens the 5 words text document and reads the document word list
    gameWord = random.choice(lines) #chooses a random word from the list
    guessCount = 5 #sets the guesscount to 5 if you choose a 5 letter wordle
    
    

  if wordCount == "6": #6 letters
    lines = open("./6words.txt").readlines()  #opens the 6 words text document
    gameWord = random.choice(lines)  #opens the 6 words text document
    guessCount = 6 #sets the guesscount to 6 if you choose a 6 letter wordle

  gameWord = gameWord.lower().strip() #makes the chosen word lowercase and removes the invisible \n at the end (strip function) (for minor debugging)

  listOfNum = ['first','second','third','fourth','fifth'] #this is a list for puncuation at the end when you finish guessing the word
  if guessCount == 6: #if you choose the six letter word then this would add the sixth guess punctuation
    listOfNum.append('sixth') #^^^^
  for x in range(0,guessCount): 
    promptValue = "\nEnter your "+str(listOfNum[x])+" guess: "
    userInput = ""
    while True:      
      userInput=input(promptValue)
      userInput = userInput.strip()
      if len(userInput) != guessCount: #compares the amount of letters in the user input so see if it has more or less than the amount of letters you should input (basicaly makes sure you have 5 or 6 letters in your input.)
        print (colored("Input must have "+str(guessCount)+" letters.",'magenta'))
        continue
      else:
        break

    status = matchCharacters(gameWord, userInput)#compares the user input to the gameword
    if status == True: #prints the ending text if user gets the word right
      print("\nCongratulations : You guessed "+gameWord+" in "+str(x+1)+" tries")
      return
  
  print("\nOut of Guesses! Word was "+gameWord) #ending input if players doens't get the word guess 
  print("Better luck next time..")
 
def matchCharacters(gameWord, userInput): #compares the gameword and the userinput to eachother
  colorOfWord =  ['white' for i in range(len(gameWord))] #default color of gameword will be white
  userInputList = list(userInput) #turns the user input into a list so the computer can read each letter
  gameWordList = list(gameWord) #turns the selected game word into a list so that it can be compared
  
  for x in range(0, len(userInput)): #this loop colors the code accordingly to each letter that you input
    if userInputList[x] in gameWordList : #checks if the letter is in the gameword but not in the right location
      colorOfWord[x] = 'red' #colors letter red
    if userInputList[x] == gameWordList[x]: #checks if the letter is in the right location and in the word. 
      colorOfWord[x] = 'green' #colors letter green

  
  for x in range(0, len(userInput)):
    print(colored(userInputList[x],colorOfWord[x]),end="")

  # Check the colors array and if any of the color is not green 
  # that means that word is not guessed yet, so return false
  for x in range(0, len(colorOfWord)):
    if colorOfWord[x] != 'green':
      return False

  # If not returned False yet that means that all colors are green, so return True
  return True
    
        
      
