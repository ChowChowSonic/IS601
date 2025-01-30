import tokenizer

def test_tokenizer():
	assert tokenizer.getToken("1234") == 1234
	assert tokenizer.getToken("0") == 0
	assert tokenizer.getToken("+") == '+'