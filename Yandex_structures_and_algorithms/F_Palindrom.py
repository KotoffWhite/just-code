def check_palindrom(text: str) -> bool:
    import re
    text = re.sub('[^A-Za-z]', '', text)
    text = text.lower()
    if text == text[::-1]:
        return True
    return False


if __name__ == '__main__':
    req_text = input()
    print(check_palindrom(req_text))
