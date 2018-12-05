def load_sheet(filename: str) -> list:
    """open x file, take each element separated by the newline character and put it into a list labled contents"""
    with open(filename, "r") as f:
        contents = f.read().splitlines()
    return contents
