import re
import sys 

class Rule:
	r''
	def __init__(self):
		self._process()
	
	def _process(self):
		self.pattern = re.compile(self.__doc__)
		
	def Match(self, data):
		self._data = data
		return self.pattern.match(data)
	

class Left_Bracket(Rule):
	r'\('

class Right_Bracket(Rule):
	r'\)'
	
class Number(Rule):
	r'[0-9]+\.?[0-9]+'

class Identifier(Rule):
	r'[a-zA-Z][a-zA-Z0-9_]+'

class Operand(Rule):
	def __init__(self, _type, left, right):
		self.left = _type()
		self.left._process()
		self.pattern = _type.__doc__
		self.Match()
		self.left.pattern = left.debug_data
		self.left._process()	# For the first calling of _process()
								# only creates empty Rule
		

		
		
		



