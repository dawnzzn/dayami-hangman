1. imports the **`random`** module, allowing the program to use functions for generating random numbers
2. print a welcome to hangman 
3. a list called **`wordDictionary`** is defined, containing several words. The **`random.choice()`** function is then used to randomly select one word from this list and store it in the variable **`randomWord`**.
4. This loop displays underscores for each letter in the randomly chosen word, creating an initial hidden version of the word for the player.
5. a function to print the hangman figure based on the number of wrong numbers. the function uses ASCII art to display the hangman figure. the argument ‘wrong’  represents the number of wrong attempts
6. These lines initialize various variables to keep track of the game state. **`length_of_word_to_guess`** stores the length of the word to be guessed, **`amount_of_times_wrong`** keeps track of the number of incorrect guesses, **`current_guess_index`** represents the current position in the word being guessed, **`current_letters_guessed`** is a list of letters guessed by the player, and **`current_letters_right`** tracks the number of correctly guessed letters.
7. This **`while`** loop continues as long as the player has not made 6 incorrect guesses (**`amount_of_times_wrong != 6`**) and has not guessed all the letters in the word (**`current_letters_right != length_of_word_to_guess`**).
8. prints the letters that the player has guessed so far.
9. This line takes user input for a guessed letter.
10. This block checks if the guessed letter matches the letter at the current position in the word.
11. If the guessed letter is correct, it prints the hangman figure, increments the current guess index, appends the guessed letter to the list of guessed letters, updates the count of correctly guessed letters, and prints lines underneath the word.
12. If the guessed letter is incorrect, it increments the count of incorrect guesses, appends the guessed letter to the list of guessed letters, prints the hangman figure, updates the count of correctly guessed letters, and prints lines underneath the word.
13. line prints a message indicating the end of the game.
