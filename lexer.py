import re

class NoMatch:
	def __init__(self):
		self.group = lambda n : None

class Rule:
	r''
	def __init__(self):
		self._process()
		self.value = None
		
	def _process(self):
		self.pattern = re.compile(self.__doc__)
		
	def Match(self, data):
		self._match_data = self.pattern.match(data)
		if self._match_data == None:
			self._match_data = NoMatch()
		self.value = self._match_data.group(0)
		return self._match_data
	
	def Eval(self):
		return eval(str(self.value))
			 	
	
class Left_Bracket(Rule):
	r'\('

class Right_Bracket(Rule):
	r'\)'
	
class Assignment(Rule):
	r'='	
	
class Add(Rule):
	r'\+'

class Subtraction(Rule):
	r'\-'

class Multiplication(Rule):
	r'\*'

class Division(Rule):
	r'\/'
	
class Number(Rule):
	r'[0-9]+\.?[0-9]+'

class Identifier(Rule):
	r'[a-zA-Z][a-zA-Z0-9_]+'
	
	
class Operation:
	def __init__(self, left, mid, right):
		self.left = left
		self.right = right
		self.mid = mid

	def Eval(self):
		self.value = eval(self.left.value+self.mid.value+self.right.value)
		return self.value
	


		
		



