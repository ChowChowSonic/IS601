from calculator.tokenizer import Tokenizer
import sys

def parse_args(*args):
    content = "".join(map(str, args))
    tokenizer = Tokenizer(content)
    arr=[]
    while tokenizer.has_next():
        token = tokenizer.get_token()
        if not token:
            break
        arr.append(token)
    return arr
 
if __name__ == "__main__":
    tokens = parse_args(*sys.argv[1:])
	