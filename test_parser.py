from kelxparser import fParse


def test_Parser():
	code = 'a=42423;'
	c = fParse(lexer(code))
	assert c[0].type == 'ID'
	assert c[1].type == 'SET'
	assert c[2].type == 'NUM'
