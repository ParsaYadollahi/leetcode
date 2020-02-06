'''
    CTCI question 1.6
'''


def compress(s):
    dic = {}
    for c in s:
        if c not in dic:
            dic.setdefault(c, 1)
        else:
            dic[c] += 1
    ret_string = ''
    for e in dic:
        ret_string = ret_string + e + str(dic[e])
    if len(ret_string) == len(s):
        return s
    else:
        return ret_string


if __name__ == "__main__":
    print(compress('helloooooooo'))
