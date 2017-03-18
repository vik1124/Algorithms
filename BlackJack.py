import random

#suite = [str(x) for x in range(2,11)] + ['A','J','K','Q']
#deck = reduce(lambda x,y: x+y, [suite for x in range(4)])
scoring = {str(x): x for x in range(2,11)}
scoring['A'] = 11
scoring['J'] = 10
scoring['K'] = 10
scoring['Q'] = 10

class BlackJack:

	def __init__(self, numDecks, numPlayers):
		self.blackjack = 21
		self.dealerThres = 17
		self.playerThres = 15
		self.deck = self.getDeck(numDecks)
		self.numPlayers = numPlayers
		self.players = [[] for x in range( numPlayers+1) ]
		self.score = {x: '' for x in range(numPlayers) }
		self.score['dealer'] = ''
		random.seed()
		self.shuffle()

	def getDeck(self, n):
		suite = [str(x) for x in range(2,11)] + ['A','J','K','Q']
		deck = reduce(lambda x,y: x+y, [suite for x in range(4)])
		return reduce(lambda x,y: x+y, [deck for x in range(n)])

	def shuffle(self):
		random.shuffle(self.deck)

	def getScore(self, l):
		return sum([scoring[x] for x in l])

	def play(self):
		for j in range(2):
			for i in range(self.numPlayers+1):
				self.players[i].append(self.deck.pop())
		players = [self.getScore(l) for l in self.players[:-1]]
		
		dealer = self.getScore(self.players[-1])
		for i in range(self.numPlayers):
			while( self.getScore(self.players[i]) < self.playerThres ):
				self.players[i].append(self.deck.pop())
			if self.getScore(self.players[i]) > 21:
				self.score[i] = 'l'
			elif self.getScore(self.players[i]) == 21 and len(self.players[i]) == 2:
				self.score[i] = 'w'
		while( self.getScore(self.players[-1]) < self.dealerThres ):
				self.players[-1].append(self.deck.pop())
		#print self.score
		if self.getScore(self.players[-1]) > 21:
			self.score = {x: 'w' for x in self.score.keys() if self.score[x] != 'l' }
			self.score['dealer'] = 'l'
		else:
			for i in range(self.numPlayers):
				if self.getScore(self.players[i]) > self.getScore(self.players[-1]) and self.score[i] != 'l':
					self.score[i] = 'w'
				elif self.getScore(self.players[i]) == self.getScore(self.players[-1]) and self.score[i] != 'l':
					self.score[i] = 's'
				elif self.getScore(self.players[i]) < self.getScore(self.players[-1]):
					self.score[i] = 'l'		



if __name__ == "__main__":
	a = BlackJack(1, 4)
	a.play()
	print "Outcome:", a.score
	print "Scores:", [a.getScore(a.players[i]) for i in range(len(a.players))]
	print "Cards:", a.players
	g = []
	cnt = 0
	numGames = 100000
	for i in range(numGames):
		game = BlackJack(1, 4)
		game.play()
		if game.score['dealer'] == 'l':
			cnt = cnt + 1
	print "dealer lost ", cnt, " times, ", cnt/(numGames * 1.0)*100, "percent loss"

