from lexer import *
import re

def test_RuleMatch():
	r=Rule()
	r.__doc__ = r"[0-9]+"
	r._process()
	r.Match('2')
	assert r.value != None
	r.Match('21')
	assert r.value !=None
	r.Match('a')
	assert r.value == None


def test_Addition_value():
	n1=Number()
	n2=Number()
	n1.Match('125')
	n2.Match('100')
	Addition = Add()
	Addition.Match('+')
	testadd = Operation(n1, Addition, n2)
	assert testadd .Eval()== 225
	assert not testadd .Eval()== 2251
	
