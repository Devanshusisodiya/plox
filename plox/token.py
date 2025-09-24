import typing as t

from plox.token_type import TokenType

class Token:
    def __init__(
        self,
        type: TokenType,
        lexeme: str,
        literal: t.Dict[str, t.Any] | None,
        line: int
    ):
        self.type = type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

    def to_string(self) -> str:
        return self.type.value + " " + self.lexeme + " " + self.literal
