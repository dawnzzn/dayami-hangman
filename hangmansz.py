import random
print("Welcome to Hsnagman")
print("-------------------------------------------"

wordDictionary = ["dream", "sunflower", "sunflower", "milkyway", "diamond", "sapphire", "rainbow", "lucky", "angels", "heaven"]
randomWord = random.choice(wordDictionary)
for x in randomWord:
	print("_", end=" ")
def print hangman(wrong):
		 if(wrong == 0)
			print("\n+---+")
			print("     |")
			print("     |")
			print("     |")
			print("    ===")
		elif(wrong == 1):
			print("\n+---+")
			print(" O   |")
			print("     |")
			print("     |")
			print("    ===")
		elif(wrong ==2):
			print("\n+---+")
			print(" O   |")
			print("/   |")
			print("     |")
			print("    ===")
		elif(wrong == 3):
			print("\n+---+")
			print(" O    |")
			print("/|   |")
			print("     |")
			print("    ===")
		elif(wrong == 4):
			print("\n+---+")
			print(" O   |")
			print("/|\  |")
			print("     |")
			print("    ===")
		elif(wrong == 5):
			print("\n+---+")
			print(" O   |")
			print("/|\  |")
			print("/    |")
			print("    ===")
			
		elif(wrong == 6):
			print("\n+---+")
			print(" O   |")
			print("/|\  |")
			print("/ \  |")
			print("    ===")
			
def printWord(guessedLetters):
	counter = 0
	RightLetters = 0
	for char in randomWord:
		if(char in guessedLetters):
			print(randomWord[counter], end=" ")
			rightLetters+=1
		else:
			print(" ", end=" ")
		counter+=1
	return rightLetters
	
	def printlines():
		print("\r")
		for char in randomword:
			print("\u203E", end=" ")
			
length_of_word-to-guess = len(randomWord)
amount_ of_time_wrong = 0
current_guess_index = 0
current_letters_guessed = []
current_letters_right = 0

while(amount-of_times_wrong != 6 and current_letters_right != length_of_word_to_guess)

	print("letters guessed so far: ")
	for letter in current_letters_guessed:
		print(letter, end=" ")

letterGuessed = input("\nGuess a letter: ")
 
if(randomWord[current_guess-index] == letterGuessed):
	print_hangman(amount_of_times_wrong)
current_guess_index+=1
current_letters_guessed.append(letterGuessed)
current_letters_right = printWord(current-letters-guessed)
printLines()

else:
	amount_of_times_wrong+=1
	current_letters_guessed.append(letterGuessed)
	print_hangman(amount_of_times_wrong)
	current_letters_right = printWord(current_letters_guessed)
	printLines()
print("Game is over! THANKS FOR PLAYING <333")
	
	
			
		 
		 
		
