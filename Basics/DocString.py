def geert(name):
    """
    Greet a person with their name.

    Parameters:
    name (str): The name of the person to greet.

    Returns:
    str: A greeting message.
    """
    return f"Hello,{name}"
print(geert("Alice"))
print(geert.__doc__)