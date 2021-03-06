
import operator

class SieveOfEratothense:

	def __init__(self, max_range):
 		self.max_range = max_range
		self.initializeSieve() 		
		self.runSieve()

 	def initializeSieve(self):
 		self.data = [i for i in range(0, self.max_range+1)]
 		self.data_length = len(self.data)
 		self.data[1] = 0
 		
 	def runSieve(self):
 		index = 2
 		completed = False
 		while not completed:
			p = self.data[index]  
			self.markMultiples(p)
			index = self.findNextP(index)
			print index
			if index == -1:
				completed = True
	
	def findNextP(self, start_at):
		for i in range(start_at + 1, self.data_length):
			if self.data[i] != 0:
				return i
		return -1

 	def markMultiples(self, p):
 		count = 2
 		p_product = p * count
 		while p_product < self.data_length:
			self.data[p_product] = 0
			count += 1
			p_product = count * p 

	def printSieve(self):
		print self.data

	def getSumOf(self):
		return sum(self.data)

def main():
	sieve = SieveOfEratothense(2000000)
	print sieve.getSumOf()
	
if __name__=="__main__":
	main()



