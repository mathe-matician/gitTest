def search4vowels(word:str) -> set:
    """Display any vowels found in supplied word."""
    vowels = set('aeiou')
    return vowels.intersection(set(word))
    
def search4letters(phrase:str="Millenium", letters:str="aeiou") -> set:
    """ Return a set of letters found in phrase"""
    return set(letters).intersection(set(phrase))
