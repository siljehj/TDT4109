def vector_dot_product(vec1, vec2):
    summen = 0
    for i in range(0, 3):
        a = vec1[i]*vec2[i]
        summen += a
    return summen

vec1 = [1, 4, 3]
vec2 = [2, 3.1, 5]
print(vector_dot_product(vec1,vec2))