import random


# Императивный код
def sort_list_imperative(number):
    if len(number) <= 1:
        return number
    else:
        q = random.choice(number)
        s_nums = []
        m_nums = []
        e_nums = []
        for n in number:
            if n < q:
                s_nums.append(n)
            elif n > q:
                m_nums.append(n)
            else:
                e_nums.append(n)
        return sort_list_imperative(s_nums) + e_nums + sort_list_imperative(m_nums)


# Декларативный
def sort_list_declarative(number):
    print(sorted(number, reverse=True))



if __name__ == '__main__':
    numbers = [1, 4, 6, -7, 10, 0, 4, 6, 3]
    lst = sort_list_imperative(numbers)
    lst1 = lst[::-1]
    print(lst1)
    sort_list_declarative(numbers)

