# the plural form if they appear more than oncein the list


def pluralize(words: list) -> set:
    if not isinstance(words, list):
        raise TypeError("Expected a list")
    
    return set([word + "s" for word in words if words.count(word) > 1])
print(pluralize(["cat", "cat", "dog"]))

# create a uncton that takes a dictionary of objects like {"name": "John", "notes": [3, 5, 4]}
# and returns a dictionary of objects like {"name": "John", "top_notes": 5}
# def top_note(dictionary: dict) -> dict:
#     if not isinstance(dictionary, dict):
#         raise TypeError("Expected a dictionary")
    
#     for key, value in dictonary