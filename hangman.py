##### Hangman Game
import random
### names
words = ["virat","ms dhoni","rohit","ashwin","rahane","raina","kl rahul","dhawan"]
word = random.choice(words)

### number of guess
no_of_guess = 7

### making a the display word in screen
display_word = ''
for i in word:
	if i == ' ':
		display_word = display_word + ' '
	else:
		display_word = display_word + '_'

### while loop till number of guess is not equal to zero
while no_of_guess !=0:
	print("Guess the name "+display_word+" Number of guess remaining:"+ str(no_of_guess))
	## letter input
	ch = raw_input()
	## checking if input is present or not
	if word.count(ch) == 0:
		no_of_guess = no_of_guess - 1
		print(ch+" is not present in the word")
	else:
		print(ch+" is present in the word")
		## making the display word with the letter in place
		foo = ( [pos for pos, char in enumerate(word) if char == ch])
		l1 = list(display_word)
		for r in foo:
			l1[r] = ch
		display_word = "".join(l1)
		## checking if more letter are present to guess
		if display_word.count('_') == 0:
			no_of_guess = 0
			break

### Result of the game
if display_word.count('_') == 0:
	print("You won")
else:
	print("You lost. The name is "+ word)
