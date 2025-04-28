from textwrap import dedent
from google.adk.agents import Agent


def reverse_string(input_string: str) -> str:
    """Reverses the input string.

    Examples:
        >>> reverse_string("hello")
        'olleh'
        >>> reverse_string("Python")
        'nohtyP'

    Args:
        input_string (str): The string to be reversed.

    Returns:
        str: The reversed string.
    """
    return input_string[::-1]


def to_uppercase(input_string: str) -> str:
    """Converts the input string to uppercase.

    Examples:
        >>> to_uppercase("hello world")
        'HELLO WORLD'
        >>> to_uppercase("Python Programming")
        'PYTHON PROGRAMMING'

    Args:
        input_string (str): The string to be converted.

    Returns:
        str: The uppercase string.
    """
    return input_string.upper()


def to_lowercase(input_string: str) -> str:
    """Converts the input string to lowercase.

    Examples:
        >>> to_lowercase("HELLO WORLD")
        'hello world'
        >>> to_lowercase("Python Programming")
        'python programming'

    Args:
        input_string (str): The string to be converted.

    Returns:
        str: The lowercase string.
    """
    return input_string.lower()


def capitalize_string(input_string: str) -> str:
    """Capitalizes the first letter of the input string.

    Examples:
        >>> capitalize_string("hello world")
        'Hello World'
        >>> capitalize_string("python programming")
        'Python Programming'

    Args:
        input_string (str): The string to be capitalized.

    Returns:
        str: The capitalized string.
    """
    return input_string.capitalize()


def to_spongebob_case(input_string: str) -> str:
    """Converts the input string to Spongebob case.

    Examples:
        >>> to_spongebob_case("hello")
        'HeLlO'
        >>> to_spongebob_case("spongebob")
        'SpOnGeBoB'

    Args:
        input_string (str): The string to be converted.

    Returns:
        str: The Spongebob case string.
    """
    return "".join(
        char.upper() if i % 2 == 0 else char.lower()
        for i, char in enumerate(input_string)
    )


root_agent = Agent(
    name="textman",
    model="gemini-2.0-flash",
    description="Helps you manipulate text.",
    instruction=dedent(
        """
        You are a helpful agent who can help users manipulate text. This typically 
        involves tasks like reversing strings, convering cases, etc. Do not 
        provide any explanations or additional information. Just return the 
        result of the operation. If the input is not a string, return an error
        message. If the input is empty, return an error message. Do not try to 
        perform any tasks you don't have a tool for. "
        """
    ),
    tools=[
        reverse_string,
        to_uppercase,
        to_lowercase,
        capitalize_string,
        to_spongebob_case,
    ],
)
