'''
    CTCI question 1.5
'''


def one_away(s1, s2):
    if len(s1) - len(s2) > 1:
        return False
    diff = 1
    i = j = 0

    while(i < len(s1) and j < len(s2)):
        if s1[i] != s2[j]:
            diff -= 1
            if len(s1) > len(s2):
                i += 1
            elif len(s1) < len(s2):
                j += 1
            else:
                i += 1
                j += 1

        else:
            i += 1
            j += 1
        if diff < 0:
            return False
    return True


if __name__ == "__main__":
    print(one_away('pale', 'bake'))
