class Braille:
    space = '000000'
    upper = '000001'
    alpha = [
        '100000', # a
        '110000', # b
        '100100', # c
        '100110', # d
        '100010', # e
        '110100', # f
        '110110', # g
        '110010', # h
        '010100', # i
        '010110', # j
        '101000', # k
        '111000', # l
        '101100', # m
        '101110', # n
        '101010', # o
        '111100', # p
        '111110', # q
        '111010', # r
        '011100', # s
        '011110', # t
        '101001', # u
        '111001', # v
        '010111', # w
        '101101', # x
        '101111', # y
        '101011', # z
    ]

    @staticmethod
    def get_value(c: chr) -> str:
        if c == ' ':
            return Braille.space
        diff = 0
        s = ''
        if c >= 'A' and c <= 'Z':
            diff = ord(c) - ord('A')
            s += Braille.upper
        else:
            diff = ord(c) - ord('a')
        s += Braille.alpha[diff]
        return s


def solution(plaintext):
    characters = list(plaintext.strip())
    braille = [Braille.get_value(c) for c in characters]
    return ''.join(braille)

if __name__ == "__main__":
    plaintext1 = "code"
    print(solution(plaintext1))

    plaintext2 = "Braille"
    print(solution(plaintext2))