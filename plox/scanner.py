import sys
import typing as t
from plox.token_type import TokenType
from plox.token import Token
from plox.plox import Plox


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
            self._scan_token()

        self.tokens.append(
            Token(type=TokenType.EOF, lexeme="", literal=None, line=self.line)
        )
        return self.tokens

    def _scan_token(self):
        c: str = self.__advance()
        match c:
            case "(":
                self.__add_token(TokenType.LEFT_PAREN)
            case ")":
                self.__add_token(TokenType.RIGHT_PAREN)
            case "{":
                self.__add_token(TokenType.LEFT_BRACE)
            case "}":
                self.__add_token(TokenType.RIGHT_BRACE)
            case ",":
                self.__add_token(TokenType.COMMA)
            case ".":
                self.__add_token(TokenType.DOT)
            case "-":
                self.__add_token(TokenType.MINUS)
            case "+":
                self.__add_token(TokenType.PLUS)
            case "*":
                self.__add_token(TokenType.STAR)
            case "/":
                self.__add_token(TokenType.SLASH)
            case ";":
                self.__add_token(TokenType.SEMICOLON)
            case _:
                Plox.error(self.line, "Unexpected character.")
                sys.exit(65)

    def __advance(self) -> str:
        self.current += 1
        return self.source[self.current - 1]

    def __add_token(self, type: TokenType, literal: t.Dict[str, t.Any] | None = None):
        text: str = self.source[self.start : self.current]
        self.tokens.append(
            Token(type=type, lexeme=text, literal=literal, line=self.line)
        )

    def __is_at_end(self) -> bool:
        return self.current >= len(self.source)
