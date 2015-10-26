from lexer import *
import re


def test_lexer():
	assert lexer('=') != []
	assert lexer('(') != []
	assert lexer(')') != []
	assert lexer('abc') != []
	assert lexer('abc=12') != []

