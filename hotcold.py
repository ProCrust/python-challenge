"""
Hotter/Colder
#Divide and Conquer Approach

Kent Joash A. Zamudio
CMSC 142 (Lab) - Exercise 3

"""

from random import randint

"""
The opponent is an instantiation of the Opponent class.
The ask() function compares the player's guess with the secret number
		-returns 'correct', 'colder', 'hotter' or 'same' depending on the secret number and the player's guess
"""

class Opponent:
	def __init__(self, number):
		self.number = number
		self.tries = 0
		self.prevDiff = None

	def ask(self, guess):
		self.tries += 1
		if guess == self.number:
			return 'correct'

		currDiff = abs(guess - self.number)
		prevDiff = self.prevDiff

		if prevDiff is None or prevDiff == currDiff:
			result = 'same'
		elif currDiff < prevDiff:
			result = 'hotter'
		elif currDiff > prevDiff:
			result = 'colder'

		self.prevDiff = currDiff
		return result


"""
	dcPlayer() accepts an instance of Opponent class
		then tries to gues the hidden number through the ask() function of that object
	returns 'timeout' when trying 100 times without guessing the hidden number
	otherwise, it returns the hidden number
"""

def dcPlayer(opponent, limit):
	upper = limit
	lower = 0
	mid =  (lower+upper)/2
	prevRes = opponent.ask(mid) #base case
	if prevRes == 'correct':
		return mid

	for guess in range(0, limit):
		
		lowerHalf = (lower+(mid-1))/2 #first evaluate the lower half of the limit (if limit=100, evaluate [0-50])
		result = opponent.ask(lowerHalf)

		if result == 'correct':
			return lowerHalf
		elif result == 'hotter': #if the result is hotter it means it is somewhere in the lower half
			upper = mid-1		 #making the mid-1 the upperbound limit
			mid = lowerHalf
			prevRes = result
		else:	#otherwise, it means it is in the upper half, making the mid+1 the lowerbound limit
			upperHalf = (upper+(mid+1))/2
			tempRes = opponent.ask(upperHalf)
			if tempRes is 'correct':
				return upperHalf
			elif tempRes == 'hotter':
				lower = mid+1
				mid = upperHalf
				prevRes = tempRes
			elif tempRes == 'same' and result == 'same':
				#if there are two numbers left to evaluate, the result will always be 'same'
				#so try the upperbound limit, otherwise the lowerbound limit must me the number
				if opponent.ask(upper) == 'correct':
					return upper 
				else:
					return lower

	return 'timeout' #for-loop ends without guessing the number

"""
	evaluate() function evaluates the performance of the dcPlayer()
		it creates an instance of Opponent class with hidden number of 1-100
		then feeds that object to dcPlayer()
	prints out the performance of dcPlayer() for each number
	also prints out the average no. of Guesses
"""

def evaluate(player,limit):
	correct = [] #
	wrong = 0
	timeout = 0

	for number in range(0,limit+1):
		print str(number).ljust(5),
		opponent = Opponent(number)
		answer = player(opponent, limit)
		if answer == 'timeout':
			timeout += 1
			print 'timeout'
		elif answer == number: # correct
			correct.append(opponent.tries)
			print opponent.tries, 'guesses'
		else:
			wrong += 1
			print 'wrong:', answer

	if len(correct) > 0:
		print 'Guess Count Frequency:'
		for guessCount in sorted(set(correct)):
			print '\t',str(guessCount).ljust(5),
			print correct.count(guessCount)

	print 'Correct:', len(correct)
	print 'Wrong:', wrong
	print 'Timeout:', timeout
	if len(correct) == 0:
		correct.append(0)
	print 'Min Guess:', min(correct)
	print 'Max Guess:', max(correct)
	aveGuess = sum(correct) / float(len(correct))
	print 'Ave Guess: %.2f' %  aveGuess

"""
	the main() function
"""
if __name__ == '__main__':
	limit = 100
	#Line 138: generates one random number using randint() function 
		#then creates an instance of the opponent class
	# opponent = Opponent(randint(0,100)) 
	#Line 140: calls the dcPlayer() function to guess the number generated in line 140
	# dcPlayer(opponent, limit)
	evaluate(dcPlayer, limit) #this evaluates the divide and conquer algorithm used in the dcPlayer() function

