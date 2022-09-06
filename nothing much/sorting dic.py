dic = {
    "kozludui" : 19738,
    'silistra' : 47000,
    "lom" : 25500,
    "ahtopol" : 1300,
    "tutrakan" : 9000,
    "kazanluk" : 49000,
    "burgas" : 202000,
    "kapitan" : 828,
    "ruse" : 144936,
    "kukata" : 843,
    "malko" : 3400,
    "veliko" : 87000,
    "kawarna" : 14000,
    "sozopol" : 12739,
    "dewnq" : 8600,
    "carewo" : 9000,
    "obzor" : 2100
}
bye = {value : key for (key, value) in dic.items()}
hi = bye.items()
sort = sorted(hi)
print(sort)
x = 0
for k in range(len(dic)):
    res = sort[x][0]
    res1 = sort[x][1]
    x += 1
    if res > 100000:
        vid = " golqmo"
        print(res1 + " e s naselenie " + str(res) + vid)
    elif res <100000 and res > 25000:
        vid = " sredno"
        print(res1 + " e s naselenie " + str(res) + vid)
    elif res < 25000:
        vid = " malko"
        print(res1 + " e s naselenie " + str(res) + vid)