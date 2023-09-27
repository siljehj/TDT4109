def multiplication_table(n):
    table = []
    list1 = []
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            a = j*i
            list1.append(a)
        table.append(list1)
        list1 = []
    return table

multiplication_table(4)