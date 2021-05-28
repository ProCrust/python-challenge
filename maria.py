"""
	Manang Maria
	#Manang Maria is an example of Weighted Interval Scheduling (WIS)
	#This algorithm uses Dynamic Programming to solve the maximum profit Manang Maria can get
	#Profit is based on the number of people in that game following the assumption
	#	that 'more people = more possible customers = more income'
	#nonOverlapGame() addressed the premise where Manang Maria can't go to a game that has already started
	#getMaxProfit() searches the given list of game schedule
	#	and outputs the game sequence that will result to maximum profit

	#Kent Joash A. Zamudio
	#CMSC 142 (Lab) - Exercise 4a
"""


from copy import deepcopy #imports deep copy from copy module, replaces '=' operator in getMaxProfit()

#nonOverlapGame() function searches for the latest game schedule that doesnt overlap with the current game
#accepts gamelist (list of games) and currentGameIndex (index of current game), then returns the index of latest non-overlapping game
def nonOverlapGame(gamelist, currentGameIndex):
	for game in gamelist[currentGameIndex-1::-1]:
		if game['end'] <= gamelist[currentGameIndex]['start']:
			return gamelist.index(game)
	return -1

#getMaxProfit() function gets the maximum profit based on the number of people in that game
#accepts gamelist (list of games) and games (no. of games), then returns profit and list of games
def getMaxProfit(gamelist, games):
	
	profitTable = [0] * games #table for the profits for the first nth job
	gamesAdded = [[] for _ in range(games)]	#list of games included in maximum profit
	
	gamelist.sort(key = lambda end_time : end_time['end']) #sorting by end time of each game

	#append the first game in profitTable[0] and gamesAdded[0]
	profitTable[0] = gamelist[0]['people']
	gamesAdded[0].append(0)


	for currentGameIndex in range(1, len(gamelist)):

		index = nonOverlapGame(gamelist, currentGameIndex) #find the index of last non-overlapping game

		currentProfit = gamelist[currentGameIndex]['people'] #the profit of the current game

		#if there is a non-overlapping game, we add the profit from that game to the profit of the current game
		if index != -1: 
			currentProfit += profitTable[index]

		#this if-else block ensures that the last index contains the highest profit possible
		#same as profitTable[currentGameIndex] = max(profitTable[currentGameIndex -1], currentProfit)
		#if the profit in the previous index is less than the currentProfit
		if profitTable[currentGameIndex-1] < currentProfit:
			profitTable[currentGameIndex] = currentProfit

			#if there is a non-overlapping game, we have to copy the games included to arrive to that profit
			#	this is done since we also added that profit to the currentProfit
			if index != -1: 
				#gamesAdded is a 2D-list and using the assignment operator (=) is only a shallow copy
				#	this means any manipulation to the copied data is also done in the original data
				#	using deepcopy removes that issue
				gamesAdded[currentGameIndex] = deepcopy(gamesAdded[index])
			#we append the currentGameIndex since it is included in the currentProfit
			gamesAdded[currentGameIndex].append(currentGameIndex)

		#if previousProfit > currentProfit, we exclude the current game and the currentProfit
		else: 
			#the following lines ensures that the latest index is gamesAdded and profitTable contains the highest profit
			gamesAdded[currentGameIndex] = deepcopy(gamesAdded[currentGameIndex-1])
			profitTable[currentGameIndex] = profitTable[currentGameIndex-1]

	#since gamesAdded is a list of indices included in the maximum profit, we convert it to list of names
	gamesName = [gamelist[i]['name'] for i in gamesAdded[games-1]]
	print profitTable[games-1], '-'.join(gamesName) #printing of profit and games included in that profit
	#garbage collection
	del profitTable
	del gamesAdded
	del gamesName
	return




if __name__ == '__main__':

	case = int(raw_input().strip()) #reads number of test cases

	for test in range(case):

		games = int(raw_input().strip()) #reads number of games
		gamelist = []	#list of dictionaries. the game is a dictionary with keys 'name', 'start', 'end', 'people'

		for x in range(games): #reads the inut and converts it to a dictionary then appends it to gamelist

			thisLine = raw_input().strip().split()
			newGame = {'name' : thisLine[0], 'start': int(thisLine[1]), 'end': int(thisLine[2]), 'people': int(thisLine[3])}
			gamelist.append(newGame)

		#process the current test case
		getMaxProfit(gamelist, games)

