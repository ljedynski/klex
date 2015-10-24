import re

class Rule:
	r''
	def __init__(self):
		self._process()
	
	def _process(self):
		self.pattern = re.compile(self.__doc__)
		
	def Match(self, data):
		self._data = data
		return self.pattern.match(data)
	
	def Eval(self):
		self_data = eval(self._data)
			 	
	
class Left_Bracket(Rule):
	r'\('

class Right_Bracket(Rule):
	r'\)'
	
class Assignment(Rule):
	r'='	
	
class Number(Rule):
	r'[0-9]+\.?[0-9]+'

class Identifier(Rule):
	r'[a-zA-Z][a-zA-Z0-9_]+'
	
class Addition(Rule):
	r'\+'
	def __init__(self, left, right)
		self.left = left
		self.right = right
		super(Addition, self).__init__()
	
	def Eval(self):
		self._data = eval(str(self.left._data)+self.)


		
		



