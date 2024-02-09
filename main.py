def bubble(ls: list) -> list:  #сортування методом бульбашки
    len_list = len(ls)
    for i in range(len_list):
        for r in range(len_list - i - 1):
            print(r)
            if ls[r] > ls[r + 1]:
                ls[r], ls[r + 1] = ls[r + 1], ls[r]
    return ls  #return sorted(ls)


def sum_list(ls: list) -> int:  #знаходження суми списку
    sum_ls = 0
    for number in ls:
        sum_ls += number
    return sum_ls  # return sum(ls)
