import re
import sys 

class Rule:
	r''
	def __init__(self):
		self._process()
		self._interpreter = True
	
	def _process(self):
		self.pattern = re.compile(self.__doc__)
		
	def Match(self, data):
		self._data = data
		return self.pattern.match(data)
	
	def Eval(self):
		if self._interpreter:
			if isinstance(self._data, int):
				return self._data		
			return eval(str(self._data))
		else:
			return self._data
			 	
	

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

class Operand(Rule):
	def __init__(self, _type, left, right):
		pass
		

		
		
		



