"""A class for a string of contents with ability to automatically parse values out of it"""


class Tokenizer:
    """Consumes a string of contents with ability to automatically parse values out of it"""

    def __init__(self, content):
        """Initializer"""
        self.index = 0
        self.content = content.replace(' ', '').replace('\t', '')

    def _get_num_const(self):
        """Retrieves a number constant starting from the current index in the string"""
        ret = ""
        while (
            self.index < len(self.content) and self.content[self.index] in "1234567890."
        ):
            ret += self.content[self.index]
            self.index += 1
        return int(ret)

    def _get_operator(self):
        """Retrieves an operator (+,-,*,/) starting from the current index in the string"""
        self.index += 1
        return self.content[self.index - 1]

    def get_token(self):
        """Retrieves a generic token from the current index in the string"""
        if self.index >= len(self.content):
            return ""
        functions = {}
        functions["+"] = self._get_operator
        functions["-"] = self._get_operator
        functions["*"] = self._get_operator
        functions["/"] = self._get_operator
        functions["^"] = self._get_operator
        functions["\\"] = self._get_operator
        for i in "1234567890.":
            functions[i] = self._get_num_const
        return functions[self.content[self.index]]()

    def get_string(self):
        """returns the raw contents of the tokenizer"""
        return self.content

    def has_next(self):
        """Checks if there are more tokens to be retrieved"""
        return self.index < len(self.content)