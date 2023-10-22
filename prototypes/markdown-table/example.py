#####################
## Formatting Algo ##
#####################


def format_markdown_table(data: list[list], header: bool = True) -> str:
    """Formats a markdown table from a matrix data struture."""
    output = []

    for row in data:
        output.append("| " + " | ".join(map(str, row)) + " |")

    if header:
        output.insert(1, "| " + " | ".join(["---"] * len(data[0])) + " |")

    return "\n".join(output)


#############
## Example ##
#############

result = format_markdown_table(
    [
        ["name", "age", "active"],
        ["tim", 25, True],
        ["mary", 21, True],
        ["bob", 56, False],
    ]
)

print(result)
