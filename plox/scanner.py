import typing as t
from plox.token_type import TokenType
from plox.token import Token

class Scanner:
    def __init__(self, source: str):
        self.source: str = source
        self.tokens: t.List[Token] = []

        self.start = 0
        self.current = 0
        self.line = 1

    def scan_tokens(self) -> t.List[Token]:
        while not self.__is_at_end():
            self.start = self.current
            self.scan_token()

        self.tokens.append(Token(
            type=TokenType.EOF,
            lexeme="",
            literal=None,
            line=self.line
        ))
        return self.tokens

    def __is_at_end(self) -> bool:
        return self.current >= len(self.source)
