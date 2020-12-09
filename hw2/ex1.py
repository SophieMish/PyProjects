# ---------------- ex1.1 -----------------------------#
import functools


def compare_num(n1: int, n2: int):
    if n1 > n2:
        return 1
    elif n1 < n2:
        return -1
    else:
        return 0


#   l=[n1,n2]; min(l); max(l)


def compare_str(str1: str, str2: str):
    if str1 > str2:
        return 1
    elif str1 < str2:
        return -1
    else:
        return 0


def compare_list(l1: list, l2: list):
    if len(l1) > len(l2):
        return 1
    elif len(l1) < len(l2):
        return -1
    for i in range(0, len(l1)):
        if isinstance(l1[i], str) ^ isinstance(l2[i], str):
            res = compare_str(str(l1[i]), str(l2[i]))
        elif ((type(l1[i]) == "str") and (type(l1[i]) == "str")):
            res = compare_str(l1[i], l2[i])
        else:
            res = compare_num(l1[i], l2[i])

        if res != 0:
            return res
    return 0


def comparator(*args):
    args = list(args)
    if type(args) == str or type(args) == int:
        return min(args), max(args)
    else:
        sorted(args,key=functools.cmp_to_key(compare_list))
        return args[0],args[len(args)-1]


#
# def compare_lists():
#     tmp_str=input()
#     for i in tmp_str:


x = ['abc', -1,'zzzz']
abc1 = ['abc', 1,'hjh']
# min, max = comparator_list()
print(comparator(x, abc1))
# print("Максимум:", max_num, "\nМинимум:", min_num)
