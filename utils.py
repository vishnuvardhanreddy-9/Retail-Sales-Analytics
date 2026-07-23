def format_currency(value):
    """
    Format currency values in a professional way.
    """

    if value is None:
        return "₹0"

    if value >= 1_000_000_000:
        return f"₹{value/1_000_000_000:.2f} Billion"

    elif value >= 1_000_000:
        return f"₹{value/1_000_000:.2f} Million"

    else:
        return f"₹{value:,.0f}"


def format_number(value):
    """
    Format numbers with commas.
    """

    if value is None:
        return "0"

    return f"{int(value):,}"