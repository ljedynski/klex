from lexer import *
import re


def test_lexer():
	assert lexer('=') != []
	assert lexer('(') != []
	assert lexer(')') != []
	assert lexer('abc') != []
	assert lexer('abc=12') != []
	dc = """
var1=321;
var2=100;
fun=(var1 * var2);

"""
	assert lexer(dc) == [('ID', 'var1', 1), ('SET', '=', 5), ('NUM', '321', 6), ('SCL', ';', 9), ('ID', 'var2', 11), ('SET', '=', 15), ('NUM', '100', 16), ('SCL', ';', 19), ('ID', 'fun', 21), ('SET', '=', 24), ('LBR', '(', 25), ('ID', 'var1', 26), ('MUL', '*', 31), ('ID', 'var2', 33), ('RBR', ')', 37), ('SCL', ';', 38)]

