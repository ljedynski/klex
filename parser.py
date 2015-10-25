from lexer import *

class Token:
	def __init__(self, value):
		self.value = value
	def Eval(self):
		return self.value

class Number(Token):
	def Eval(self):
		self.number = eval(self.value)
		return self.number
		
class Identifier(Token):
	def Eval(self):
		self.name = self.value
		return self.name

class Evaluate(Token):
	def __init__(self, left, right, operator):
		self.left = left
		self.right = right
		self.operator = opertator
	
	def Eval(self):
		return eval(self.left+self.operator+self.right)

code = "12+3"

def fParse(tokens):
	for token in tokens:
		
