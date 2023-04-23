from game import startGame

print('Hello, Welcome To The Word Game!')

directions = input('Would you like directions on how to play?(yes or no): ')


if directions == ("yes"): #code for directions
  print("\nDIRECTIONS:")
  print("If the color of your letter is 'red' then your letter is in the word,but not in the right area.")
  print("\nIf your letter is white, then your letter is not in the word.")
  print("\nIf your letter is green, then your letter is in the word and in theright area.")
  print("\nIf you choose a 5 letter word then you have 5 guesses and if you choose a 6 letter word you will have 6 guesses")

  continueChoice = input("\nWould you like to continue?: ")
  if continueChoice == "yes":
    startGame()
  
if directions == ("no"):
  startGame()





