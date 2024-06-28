def oklitMesafesi(m1,m2):
    oklid = 0
    
    for k in range(len(m1)):
        oklid += (m1[k]- m2[k])*(m1[k]- m2[k])
    oklid **= (1/2)
    return oklid

matris = [-1, 2, 1]
matris1 = [-1, 4, 6]
sonuc = oklitMesafesi(matris,matris1)
print(sonuc)