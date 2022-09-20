import sys


def docret(input_string: str) -> str:
    """
    Just returns the input string.

    Args:
        input_string (str): An input string.

    Returns:
        str: Returns the input string.
    """
    return input_string


def main() -> None:
    """
    Just prints the input string or default string.

    Returns:
        None: Nothing is returned.
    """
    input_string = sys.argv[1] if len(sys.argv) > 1 else "Hello, doctall!"
    print(docret(input_string))
