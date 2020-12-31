def solution(x):
    l = len(x)
    final = []
    for i in range(l):
        c = x[i]
        if 'a' <= c <= 'z':
            pos = ord(c) - ord('a')
            final.append(chr(ord('a') + 25 - pos))
        else:
            final.append(c)
    return ''.join(final)


if __name__ == "__main__":
    t1 = "wrw blf hvv ozhg mrtsg'h vkrhlwv?"
    print(solution(t1))

    t2 = "Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"
    print(solution(t2))