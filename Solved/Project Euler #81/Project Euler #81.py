from time import time as t 

class Solution:
	def __init__(self, matrix):
		self.matrix = matrix
		self.runtime = 0
	def reduce(self):
		start = t()

		for i in range(1, len(self.matrix)):
			self.matrix[0][i] += self.matrix[0][i-1]
			self.matrix[i][0] += self.matrix[i-1][0]

		for i in range(1, len(self.matrix) - 1):
			self.matrix[i][i] += min(self.matrix[i-1][i], self.matrix[i][i-1])

			for j in range(i + 1, len(self.matrix)):
				self.matrix[i][j] += min(self.matrix[i-1][j], self.matrix[i][j-1])
				self.matrix[j][i] += min(self.matrix[j-1][i], self.matrix[j][i-1])

		self.matrix[-1][-1] += min(self.matrix[-1][-2], self.matrix[-2][-1])
		end = t()
		self.runtime = end - start

	def vals(self):
		for i in self.matrix:
			print(i)

	def answer(self):
		print(self.matrix[-1][-1])
		print(self.runtime)

matrix = []

with open('Matrix.txt', 'r') as file:
	for line in file:
		matrix.append([int(i) for i in line.split(',')])

solution = Solution(matrix)
solution.reduce()
solution.answer()