import sys
import typing as t
from pathlib import Path


class Plox:
    had_error = False

    def main(self, args: t.List[str]) -> IOError | None:
        if len(args) > 1:
            print("Usage: plox [script]")
            sys.exit(64)
        elif len(args) == 1:
            self.__run_file(args[0])
        else:
            self.__run_prompt()

    def __run_file(self, path: str) -> IOError | None:
        canonical_path = Path(path)
        if canonical_path.exists():
            source_bytes = canonical_path.read_bytes()
            self.__run(source_bytes)  # TODO: Convert bytes to string here

            if self.had_error:
                sys.exit(65)
        else:
            raise IOError("Panic! File not found.")

    def __run_prompt(self) -> EOFError | None:
        try:
            while True:
                input_buffer = input("> ")
                if input_buffer == "exit":
                    break
                self.__run(input_buffer)
                # if there is an error, the session shouldn't break
                self.had_error = False
        except EOFError:
            print("\n")
            sys.exit(64)

    def __run(self, source: str) -> None:
        print(source)  # Just print the source for now

    @classmethod
    def error(cls, line: int, message: str) -> None:
        cls._report(line, "", message)

    @classmethod
    def _report(cls, line: int, where: str, message: str) -> None:
        print(f"[line {line}] Error{where}: {message}")
        cls.had_error = True
