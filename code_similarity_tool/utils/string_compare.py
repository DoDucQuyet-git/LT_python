import difflib

def calculate_string_similarity(text1, text2):
    """So sánh phần trăm giống nhau giữa 2 chuỗi văn bản."""
    if not text1 or not text2:
        return 0.0
    return difflib.SequenceMatcher(None, text1, text2).ratio() * 100