"""Some smarts to try to find the item being referenced like Git does.

It's really annoying trying to figure out the rank of the item in a list to
either update or remove it. The logic within this module provides a rudamentary
"fuzzy" lookup to provide a better UX.
"""


def fuzzy_match(value, list_to_lookup, algorithm="leading_partial"):
    """Attempts to fuzzy match the value in the provided list."""
    available_algorithms = {
        "leading_partial": leading_partial_exact_match,
    }

    algo = available_algorithms.get(algorithm, False)
    if algo:
        return algo(value, list_to_lookup)
    else:
        valid_algorithms = list(available_algorithms.keys())
        raise ValueError(
            f"Couldn't find algorithm '{algorithm}'. "
            f"Valid algorithms: {valid_algorithms}"
        )


def leading_partial_exact_match(value, list_to_lookup):
    """Attempts to fuzzy match using a leading partial exact match.

    This implementation looks for a partial match. In particular, it sees if any
    of the items *start* with the value provided. Will only succeed if there is
    a single partial match. 
    """
    potential_matches = [item for item in list_to_lookup if item.startswith(value)]
    if len(potential_matches) == 0:
        raise ValueError("Couldn't find a match in the list.")
    elif len(potential_matches) >= 2:
        raise LookupError("Ambiguous input. Failing")
    else:
        return potential_matches[0]
