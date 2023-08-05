import os
import sys
from typing import List

from actions import io


def main(args: List[str]) -> None:
    """main function

    Args:
        args: STDIN arguments
    """

    # now you can access the inputs like:
    #    f"Hello {os.environ["INPUT_NAME"]}"

    # you can write to output like:
    #   io.write_to_output({var: val, ...})

    pass


if __name__ == "__main__":
    main(sys.argv)
