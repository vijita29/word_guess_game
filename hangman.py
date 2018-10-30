##### Hangman Game
import random
words = ["virat","ms dhoni","rohit","ashwin","rahane","raina","kl rahul","dhawan"]
word = random.choice(words)
no_of_guess = 7
display_word = ''
for i in word:
	if i == ' ':
		display_word = display_word + ' '
	else:
		display_word = display_word + '_'
while no_of_guess !=0:
	print("Guess the name "+display_word+" Number of guess remaining:"+ str(no_of_guess))
	ch = raw_input()
	if word.count(ch) == 0:
		no_of_guess = no_of_guess - 1
		print(ch+" is not present in the word")
	else:
		print(ch+" is present in the word")
		foo = ( [pos for pos, char in enumerate(word) if char == ch])
		# print foo
		for r in foo:
			l1 = list(display_word)
			l1[r] = ch
			display_word = "".join(l1)
		# print word,foo,display_word
		if display_word.count('_') == 0:
			no_of_guess = 0
			break
if display_word.count('_') == 0:
	print("You won")
else:
	print("You lost. The name is "+ word)
