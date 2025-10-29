def count_words(text: str) -> int:
    """Return number of words in text (simple split on whitespace)."""
    return len(text.split())

def count_characters(text: str) -> dict[str,int]:
    """Return a mapping of character->count (lowercased)."""
    char_count = {}
    lower_text = text.lower()
    for char in lower_text:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count

def sort_characters(char_count: dict[str,int]) -> list[dict]:
    """Return list of dicts sorted by count desc: [{"char": c, "num": n}, ...]."""
    char_list = [{"char":key, "num":item} for key, item in char_count.items()]
    char_list.sort(reverse=True, key=lambda x: x["num"])
    return char_list