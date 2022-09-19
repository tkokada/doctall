import sys


def _doctall(input_string: str) -> str:
    """
    Just returns the input string.

    Args:
        input_string (str): An input string.

    Returns:
        str: Returns the input string.
    """
    return input_string


def main() -> None:
    input_string = sys.argv[1] if len(sys.argv) > 1 else "Hello, doctall!"
    print(_doctall(input_string))
