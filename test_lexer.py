from lexer import *
import re

def test_RuleMatch():
	r=Rule()
	r.__doc__ = r"[0-9]+"
	r._process()
	assert r.Match('2') != None	
	assert r.Match('21') != None	
	assert r.Match('a') == None

def test_Left_Bracket():
	lb=Left_Bracket()
	assert lb.Match('(') != None
	assert lb.Match('abc') == None
	
def test_Right_Bracket():
	lb=Right_Bracket()
	assert lb.Match(')') != None
	assert lb.Match('abc') == None
	
def test_Number():
	n=Number()
	assert n.Match('3213') != None
	assert n.Match('-12') == None
	assert n.Match('12.2') != None 
	
def test_Identifier():
	i = Identifier()
	assert i.Match('var') != None
	assert i.Match('var1') != None
	assert i.Match('1var') == None


	
