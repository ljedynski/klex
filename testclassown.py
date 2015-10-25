import ast
source = open(__file__, 'r').read()

class Rule: None

class Operand: None
	
class Assignment(Rule, Operand):
	r'='	
	
class Add(Rule, Operand):
	r'\+'

class Subtraction(Rule, Operand):
	r'\-'

class Multiplication(Rule, Operand):
	r'\*'

class Division(Rule, Operand):
	r'\/'
	
class Number(Rule):
	r'[0-9]+\.?[0-9]+'

class Identifier(Rule):
	r'[a-zA-Z][a-zA-Z0-9_]+'

class Whitespace(Rule):
	r'[ \n\t]+'

p = ast.parse(source)
classes = [node.name for node in ast.walk(p) if isinstance(node, ast.ClassDef)]
print(classes)
