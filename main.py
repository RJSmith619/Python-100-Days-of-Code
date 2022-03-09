#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
for word in word_list:
  random_word = random.choice(word_list)
  
#print(random_word)
print(random_word)


#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
print("Welcome!")
guess = input("Please guess a letter. \n").lower()

#print(guess) 
print(guess)


#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
if guess in (random_word):
  print("Yes")
else:
  print("No")
