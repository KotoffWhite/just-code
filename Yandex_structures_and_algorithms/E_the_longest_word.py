def get_the_longest_word(text: str) -> tuple:
    max_len = 0
    max_word = ''
    for word in text.split():
        if len(word) > max_len:
            max_len = len(word)
            max_word = word
    return (max_word, max_len)


if __name__ == '__main__':
    text_len = int(input())
    req_text = input()
    print(*get_the_longest_word(req_text), sep='\n')
