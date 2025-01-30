from tokenizer import tokenizer

def test_tokenizer():
	t=tokenizer("1234+0")
	assert t.getToken() == 1234
	assert t.getToken() == '+'
	assert t.getToken() == 0