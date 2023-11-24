def correlate(X, Y):
    return ((len(X) * sum(map(lambda z: z[0] * z[1], zip(X, Y))) - sum(X) * sum(Y)) /
            ((len(X) * sum(map(lambda x: x ** 2, X)) - sum(X) ** 2) *
             (len(Y) * sum(map(lambda y: y ** 2, Y)) - sum(Y) ** 2)) ** 0.5)


lst1 = [17, 7, 17, 28, 27, 31, 20, 17, 35, 43, 10, 28, 13, 43, 45, 24, 45, 26, 16, 26]
lst2 = [19, 32, 33, 44, 28, 35, 39, 39, 44, 44, 24, 37, 29, 40, 42, 32, 48, 42, 33, 47]

print(correlate(lst1, lst2))