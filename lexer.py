import re
import sys

class lexerError(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return self.value

rulesdb=(
	(r'[ \n\t\s]+' , (None, )),
	(r'\+', ('ADD', '+')),
	(r'\-', ('SUB', '-')),
	(r'\*', ('MUL', '*')),
	(r'\/', ('DIV', '/')),
	(r'\==', ('EQU', '==')),
	(r'\<\=', ('LEQ', '<=')),
	(r'\>\=', ('GEQ', '>=')),
		(r'\=' , ('SET',)),
	(r'\;', ('SCL', ';')),
	(r'\>', ('GT', '>')),
	(r'\<', ('LT', '<')),	
	(r'\(' , ('LBR', '(')),
	(r'\)' , ('RBR', ')')),
	(r'[0-9]+' , ('NUM',)),
	(r'[a-zA-Z][a-zA-Z0-9_]+' , ('ID',)),
	(r'[a-zA-Z]', ('ID',)),

)


def lexer(source):
	pos = 0
	tokens = []
	while pos < len(source):
		match = None
		for rule in rulesdb:
			pattern, data = rule
			token = re.compile(pattern)
			match = token.match(source, pos)
			if match:
				if data[0] != None:
					tokens.append((match.group(0), data))
					
				break
		if not match:
			sys.exit(0)
		else:
			pos = match.end(0)
	return tokens
	


