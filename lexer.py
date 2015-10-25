import re
import sys

class lexerError(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return self.value

rulesdb=(
	(r'[ \n\t]+' , (None, )),
	(r'\+', ('ADD', '+')),
	(r'\-', ('SUB', '-')),
	(r'\*', ('MUL', '*')),
	(r'\/', ('DIV', '/')),
	(r'\==', ('EQU', '==')),
	(r'\<\=', ('LEQ', '<=')),
	(r'\>\=', ('GEQ', '>=')),
	(r'\;', ('SCL', ';')),
	(r'\>', ('GT', '>')),
	(r'\<', ('LT', '<')),	
	(r'\(' , ('LBR', '(')),
	(r'\)' , ('RBR', ')')),
	(r'[a-zA-Z][a-zA-Z0-9_]+' , ('ID',)),
	(r'[0-9]+\.?[0-9]+' , ('NUM',)),
	(r'\=' , ('SET',)),
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
					tokens.append((data[0], match.group(0), pos))
					print(pattern)
				break
		if not match:
			raise lexerError("Invalid character at pos %d" % pos)
			sys.exit(1)
		else:
			pos = match.end(0)
	return tokens

