from calculator.tokenizer import Tokenizer
import sys

def parse_args(*args):
    content = "".join(map(str, args))
    tokenizer = Tokenizer(content)
    arr=[]
    while True:
        token = tokenizer.get_token()
        if not token:
            break
        arr.append(token) # appends each token to the array
    return arr
 
if __name__ == "__main__":
    tokens = parse_args(*sys.argv[1:])
	