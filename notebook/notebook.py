def convert(my_name):
    """
        Print a line about converting a notebook.
        Args:
            my_name (str): person's name
        Returns:
            None
    """
    try:
        print(f"I'll convert a notebook for you some day, {my_name}")
    except TypeError:
        print(f"{my_name} не является строкой")
