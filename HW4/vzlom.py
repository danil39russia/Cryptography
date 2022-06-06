def fast_exp(num: int, exp: int, mod: int):
    bin_exp = bin(exp)
    result = num
    for j in range(3, len(bin_exp)):
        result = (result ** 2) % mod
        if int(bin_exp[j]) == 1:
            result = (result * num) % mod
    return result

#c = 663
c = 539960
#e, d, n = 17, 1817, 2479
e, d, n = 87553, -59903, 762079
#m = 49
#m = 122
#print(int('0000000001111010', 2))
#print(int('10000011110100111000', 2))
c_exp = fast_exp(c, e, n)
i = 0
while c_exp != c:
    c_exp = fast_exp(c_exp, e, n)
    i+=1
#print (i-1)
c_exp = fast_exp(c, e, n)
for j in range(0, i-1):
    c_exp = fast_exp(c_exp, e, n)
print (c_exp)

