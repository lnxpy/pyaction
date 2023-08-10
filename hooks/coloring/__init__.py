"""
Ideas used here were originally taken from the
repository below, kudos to the author!

https://github.com/nanato12/term-printer
"""

from dataclasses import dataclass
from typing import List, Union, Optional

from coloring.constants import Color, Format


@dataclass
class Text:
    text: str
    options: Optional[List[Union[Color, Format]]] = None

    def __str__(self) -> str:
        if self.options is None:
            return self.text

        attr_codes = ";".join(str(opt.value) for opt in self.options)
        return f"\033[{attr_codes}m{self.text}\033[0m"


def cprint(*args, options: List[Union[Color, Format]] = [], **kwargs) -> None:
    formatted_output = [Text(str(arg), options) for arg in args]
    print(*formatted_output, **kwargs)
