from lexer import *

class Token:
	def __init__(self, token):
		self.name = token[0]
		self.type = token[1][0]

	
		
	def Eval(self):
		return eval(self.value)


class AST:
	def __init__(self, name, ptype, cpos, lvl):
		self.name = name
		self.type = ptype
		self.code_position = cpos
		self.level = lvl
	
def fParse(tokens):
	ast = []
	step = 0
	level = 0
	for n in tokens:
		step +=1
		cur = Token(n)
		if cur.type == 'LBR':
			level +=1
			print('level', level)
			step +=1
		elif cur.type == 'RBR':
			level -=1
			step +=1		
		ast.append(AST(cur.name, cur.type, step, level))
	return ast
		


