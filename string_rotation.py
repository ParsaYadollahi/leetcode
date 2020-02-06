'''
    CTCI question 1.9
'''


def string_rotation(s1, s2):
    if len(s1) != len(s2):
        return False

    s1 = s1+s1
    if s2 in s1:
        return True
    else:
        return False


if __name__ == "__main__":
    print(string_rotation('waterBottle', 'erBottlewat'))
